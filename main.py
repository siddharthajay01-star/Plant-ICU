
import machine
import dht
import time
 
sensor     = dht.DHT22(machine.Pin(15))
grow_light = machine.Pin(12, machine.Pin.OUT)
pump       = machine.Pin(14, machine.Pin.OUT)
mister     = machine.Pin(27, machine.Pin.OUT)
soil_led   = machine.Pin(2,  machine.Pin.OUT)
 
ALL = [grow_light, pump, mister, soil_led]
 
def all_on():
    for p in ALL: p.value(1)
 
def all_off():
    for p in ALL: p.value(0)
 

all_off()
for _ in range(3):
    all_on()
    time.sleep_ms(200)
    all_off()
    time.sleep_ms(200)
time.sleep_ms(500)
 
HUMIDITY_LOW  = 65.0
HUMIDITY_HIGH = 75.0
TEMP_HOT      = 32.0
SOIL_DRY      = 30
 
soil           = 55
loop_count     = 0
mister_is_on   = False
emergency      = False
 
while True:
    loop_count += 1
    soil = max(0, soil - 5)

    is_day = (loop_count % 20) < 10
 
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum  = sensor.humidity()
 
        if temp > TEMP_HOT:
            emergency = True
            for _ in range(4):
                all_on()
                time.sleep_ms(100)
                all_off()
                time.sleep_ms(100)
            
            grow_light.value(0)
            mister.value(1)
            pump.value(0)
            soil_led.value(1)
 
        else:
           
            if emergency:
                emergency = False
                mister.value(0)
                soil_led.value(0)
                for _ in range(2):
                    grow_light.value(1)
                    time.sleep_ms(300)
                    grow_light.value(0)
                    time.sleep_ms(300)
 
            
            grow_light.value(1 if is_day else 0)
 
           
            if hum < HUMIDITY_LOW:
                mister.value(1)
                mister_is_on = True
            elif hum >= HUMIDITY_HIGH:
                mister.value(0)
                mister_is_on = False
 
           
            if soil < SOIL_DRY:
                
                for _ in range(3):
                    pump.value(1)
                    time.sleep_ms(150)
                    pump.value(0)
                    time.sleep_ms(150)
                
                pump.value(1)
                soil_led.value(1)
                time.sleep_ms(800)
                pump.value(0)
                soil_led.value(0)
                soil = 80
 
            if soil >= 50:
                soil_led.value(0)                         
            elif soil >= SOIL_DRY:
                soil_led.value(1 if loop_count % 2 == 0 else 0)   
            else:
                soil_led.value(1 if loop_count % 1 == 0 else 0)   
 
    except OSError:
        # Sensor error = yellow + red alternate flash
        for _ in range(3):
            mister.value(1)
            soil_led.value(0)
            time.sleep_ms(200)
            mister.value(0)
            soil_led.value(1)
            time.sleep_ms(200)
        mister.value(0)
        soil_led.value(0)
 
    time.sleep(1)

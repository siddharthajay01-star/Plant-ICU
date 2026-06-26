import machine
import dht
import time

DHT_PIN = 15
GROW_LIGHT_PIN = 12
PUMP_PIN = 14
MISTER_PIN = 27

sensor = dht.DHT22(machine.Pin(DHT_PIN))
grow_light = machine.Pin(GROW_LIGHT_PIN, machine.Pin.OUT)
pump = machine.Pin(PUMP_PIN, machine.Pin.OUT)
mister = machine.Pin(MISTER_PIN, machine.Pin.OUT)

HUMIDITY_LOW_THRESHOLD = 65.0
HUMIDITY_HIGH_THRESHOLD = 75.0
TEMP_HOT_THRESHOLD = 32.0  

simulated_soil_moisture = 20 

print("Booting Plant ICU Sandbox...")

while True:
    try:
        sensor.measure()
        current_temp = sensor.temperature()
        current_humidity = sensor.humidity()
        
        print("Temp: {:.1f}°C | Humidity: {:.1f}%".format(current_temp, current_humidity))
        
        if current_temp > TEMP_HOT_THRESHOLD:
            print("[ALERT]: Cabinet is too hot! Shutting down Grow Light to cool down.")
            grow_light.value(0) 
        else:
            grow_light.value(1) 
        
    
        if current_humidity < HUMIDITY_LOW_THRESHOLD:
            mister.value(1)
        elif current_humidity > HUMIDITY_HIGH_THRESHOLD:
            mister.value(0)
            
        
        if simulated_soil_moisture < 30:
            print("[IRRIGATION]: Soil is DRY ({})! Turning pump ON...".format(simulated_soil_moisture))
            pump.value(1)
            time.sleep(3) 
            pump.value(0)
            print("[IRRIGATION]: Burst cycle finished. Pump OFF.")
            simulated_soil_moisture = 80 
            
    except OSError as e:
        print("Failed to read climate sensor data.")
        
   
    time.sleep(0.5)

Smart Desktop Plant ICU — Part 1: Wokwi Simulation
An automated desktop greenhouse controller simulated on ESP32 and MicroPython. Part 1 of a real hardware build  a fully sealed acrylic enclosure with live sensors, automated watering, humidity control, and time lapse photography.
https://wokwi.com/projects/467922476236614657 — Click the DHT22 sensor and drag the sliders to interact.

What This Is
This simulation is the software proof of concept for a physical Smart Desktop Plant ICU, a sealed transparent acrylic desktop greenhouse that independently keeps a plant alive with no human activity .
The real build uses an ESP32, SHT31 sensor, capacitive soil probe, 5V water pump, ultrasonic mist maker, and an ESP32-S3 camera for automated time lapse photography. This rough simulation on Wokwi shows how some of the automation will work before the physical components are assembled.

LED Blink Language
GROW LIGHT — Purple Solid ON = daytime active / OFF = night phase
PUMP — Blue 3 fast flashes then solid = watering burst firing
MISTER — Yellow Solid ON = misting / OFF = enough amount of humidity
SOIL HEALTH — Red OFF = healthy / slow blink = low / fast blink = critical / solid = emergency
Special Patterns
All 4 LEDs flash 3x on boot System started successfully
All 4 LEDs rapid flash together Heat emergency triggered (temp over 32°C)
Purple flashes 2x slowly Emergency finished, back to normal
Yellow and Red alternate flash DHT22 sensor read error

Automation
Smart Watering
Soil moisture simulated with a live decay rate 
Pump fires a 0.8 second burst when soil drops below 30%
Blocked during heat emergencies  no watering when the enclosure is overheating
Watering counter tracked across the session
Humidity Control 
Mist maker activates when humidity drops below 65%
Only shuts off once humidity recovers above 75%
Forced ON during heat emergency to cool the air
Daytime only  no misting at night prevents leaf mold
Light Cycle
Grow light runs during the day phase
Cuts automatically at night for plant respiration
Instantly cut during heat emergencies 

Hardware Map
DHT22 Sensor — GPIO 15 Temperature and humidity readings
Purple LED — GPIO 12 Grow light indicator
Blue LED — GPIO 14 Water pump indicator
Yellow LED — GPIO 27 mist maker indicator
Red LED — GPIO 2 Soil health status indicator

The Real Build (Coming in Part 2)
This simulation represents the rough firmware for a physical desktop cabinet currently under construction.
Enclosure 11x11x14 inch sealed clear acrylic cabinet, EPDM foam door seal (more things to add on)
False Bottom LECA clay pebbles → HDPE mesh → sterile baked soil
Sensors SHT31, capacitive soil probe, LDR light confirmation
Plumbing Two isolated external reservoirs tap water for watering, distilled water for misting
Power 2 breadboards one for camera and sensors, one heavy load rail for relays and pump
Failsafes Hardware float switch in LECA layer physically cuts pump power
Time Lapse ESP32-S3 camera mounted level on interior wall

Built With
MicroPython on ESP32
Wokwi online simulator
DHT22 temperature and humidity sensor



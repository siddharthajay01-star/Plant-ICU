Plant ICU Part 1 - ESP32 rough Automation Sandbox


An automated plant desktop environment monitoring and watering system built with MicroPython and simulated using an ESP32 microcontroller. This project uses sensor based loops to maintain good environmental conditions


Live Demo
Test the hardware components and interact with the DHT22 slider
https://wokwi.com/projects/467922476236614657


Features


 Heat Safety Grow Light System: Automatically runs a grow light if temperatures exceed a safe threshold of 32°C, the system instantly shuts down the grow light to protect the plant from overheating 


Humidity system: Real time atmospheric monitoring via a DHT22 sensor triggers an environmental mister (Yellow LED) when humidity drops below 65%, shutting down once it recovers to 75%.


Watering system: Simulates auto soil moisture management. Upon system boot, if soil levels are detected to be dry, the ESP32 fires a 3 second micro burst of water from the water pump (Blue LED) to safely water without waterlogging.


Hardware Simulation Layout


Microcontroller: ESP32 
Sensors: DHT22 Weather Sensor (Temperature & Humidity) -> GPIO 15
Outputs: Purple LED (Grow Light) -> GPIO 12
Blue LED (Water Pump) -> GPIO 14
Yellow LED (Mister) -> GPIO 27


Built with some code assistance from Gemini 

# Assignment-3

### IoT System for Environmental Monitoring

This repository contains the code for a cloud-based IoT system designed to collect data from virtual sensors deployed in an environmental monitoring scenario. The system utilizes the MQTT protocol for communication and is capable of displaying both real-time and historical sensor data.

#### Virtual Sensors
- The virtual sensors simulate temperature, humidity, and CO2 levels.
- Each sensor generates random values within specified ranges:
  - Temperature: -50 to 50 degrees Celsius
  - Humidity: 0 to 100%
  - CO2: 300ppm to 2000ppm
- Each virtual environmental station is assigned a unique ID to publish sensor data on an MQTT channel.

#### Repository Structure
- `virtual_sensor.py`: Python script for simulating virtual sensors.
- `main.py`: Python script for publishing sensor data to ThingSpeak using MQTT.
- feeds.csv: Feed of data published to ThingSpeak.

#### Getting Started
1. Clone the repository to your local machine.
2. Install the required libraries (`paho-mqtt`, `requests`).
3. Update the `main.py` script with your ThingSpeak channel IDs and API keys.
4. Run the `main.py` script to start publishing sensor data to ThingSpeak.

#### Authors
- [Prasad Bankar]


#### Acknowledgments
- This project was completed as an assignment for [CIS 600].

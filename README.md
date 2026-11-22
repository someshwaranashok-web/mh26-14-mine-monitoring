# MH26-14: Mine Subsidence Monitoring

This is my HackForge 2026–27 project for problem MH26-14.

The main idea is to monitor sensor readings in underground coal mines and detect unusual changes that may need attention.

## What I have made

This is a software-based demo using simulated sensor data.

- ESP32 and MPU6050 sensor simulation in Wokwi
- MQTT to send sensor readings
- Python to collect and save the data
- Pandas to handle the sensor data
- Isolation Forest to identify unusual readings
- A Python terminal program to show the final status

## How the demo works

Wokwi sends simulated sensor readings through Wi-Fi to an MQTT broker.

Python receives the readings and saves them in a CSV file. The data is then analysed using an Isolation Forest model.

The final Python program displays the total readings, normal readings, anomalous readings, and a warning or normal status in the terminal.

## Tools used

- Wokwi
- ESP32
- MPU6050
- MQTT
- Python
- Jupyter Notebook
- Pandas
- Scikit-learn

## Important note

This is a student prototype using simulated sensor data. It is not tested in an actual mine and cannot predict a real mine collapse.

The current demo uses Wi-Fi and MQTT. A physical LoRa-based sensor network and gateway can be considered for future development.

## Project files

- `MH26_MQTT_data_collection.ipynb` – data collection and analysis
- `final_status.py` – final terminal status
- `sensor_data.csv` – collected sensor readings
- `sensor_results.csv` – analysis results

This project is made for learning and hackathon demonstration.

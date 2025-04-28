# Auto Hydroponics System

An automated watering system for vegetable patches using ESP32 and MicroPython.

## Features

- Weather-based watering decisions using OpenWeatherMap API
- WiFi connectivity for remote monitoring
- Relay control for water pump/solenoid valve
- Configurable watering schedules

## Hardware Requirements

- ESP32 development board
- Relay module
- Water pump or solenoid valve
- Power supply
- (Optional) Soil moisture sensor
- (Optional) Rain sensor

## Setup Instructions

1. Flash MicroPython to your ESP32
2. Configure WiFi credentials in `config.py`
3. Set up OpenWeatherMap API key in `config.py`
4. Upload all Python files to ESP32
5. Connect hardware components:
   - Relay to GPIO pin specified in config
   - Water pump/valve to relay
   - (Optional) Connect sensors to specified GPIO pins

## Configuration

Edit `config.py` to set:
- WiFi credentials
- OpenWeatherMap API key
- GPIO pin assignments
- Watering schedule parameters

## Usage

1. Power on the ESP32
2. The system will automatically:
   - Connect to WiFi
   - Check weather conditions
   - Control watering based on weather and schedule


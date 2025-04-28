import network
import urequests
import machine
import time
import json
from config import *

# Initialize WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Initialize relay
relay = machine.Pin(RELAY_PIN, machine.Pin.OUT)
relay.value(0)  # Ensure relay is off initially

def connect_wifi():
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected:', wlan.ifconfig())

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={OWM_CITY},{OWM_COUNTRY_CODE}&appid={OWM_API_KEY}&units=metric"
        response = urequests.get(url)
        data = json.loads(response.text)
        response.close()
        
        if DEBUG:
            print("Weather data:", data)
            
        return {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'rain': 'rain' in data or 'snow' in data
        }
    except Exception as e:
        print("Error fetching weather:", e)
        return None

def should_water(weather_data):
    if not weather_data:
        return False
        
    # Don't water if it's raining
    if weather_data['rain']:
        if DEBUG:
            print("Not watering: It's raining")
        return False
        
    # Check temperature range
    if weather_data['temp'] < MIN_TEMPERATURE or weather_data['temp'] > MAX_TEMPERATURE:
        if DEBUG:
            print("Not watering: Temperature out of range")
        return False
        
    return True

def water_plants(duration):
    if DEBUG:
        print(f"Watering plants for {duration} seconds")
    relay.value(1)  # Turn on relay
    time.sleep(duration)
    relay.value(0)  # Turn off relay

def main():
    connect_wifi()
    
    while True:
        try:
            weather_data = get_weather()
            
            if should_water(weather_data):
                water_plants(WATERING_DURATION)
            
            if DEBUG:
                print(f"Sleeping for {CHECK_INTERVAL} seconds")
            time.sleep(CHECK_INTERVAL)
            
        except Exception as e:
            print("Error in main loop:", e)
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main()

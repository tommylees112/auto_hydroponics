import machine
import time

def blink_led(pin=2, times=3, duration=0.5):
    """
    Blink the onboard LED to indicate status
    """
    led = machine.Pin(pin, machine.Pin.OUT)
    for _ in range(times):
        led.value(1)
        time.sleep(duration)
        led.value(0)
        time.sleep(duration)

def read_soil_moisture(pin):
    """
    Read soil moisture sensor value
    Returns value between 0 (wet) and 4095 (dry)
    """
    adc = machine.ADC(machine.Pin(pin))
    adc.atten(machine.ADC.ATTN_11DB)  # Full range: 3.3v
    return adc.read()

def read_rain_sensor(pin):
    """
    Read rain sensor value
    Returns True if rain is detected
    """
    sensor = machine.Pin(pin, machine.Pin.IN)
    return not sensor.value()  # Active low

def deep_sleep(seconds):
    """
    Put the ESP32 into deep sleep mode
    """
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, seconds * 1000)
    machine.deepsleep() 
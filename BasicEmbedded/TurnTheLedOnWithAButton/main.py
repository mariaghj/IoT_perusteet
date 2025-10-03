from machine import Pin
import time

time.sleep(0.1)

button = Pin(13, Pin.IN, Pin.PULL_UP)
led_onboard = Pin(18, Pin.OUT)

while True:
    if button.value() == 0:
        led_onboard.value(1)
    else:
        led_onboard.value(0)
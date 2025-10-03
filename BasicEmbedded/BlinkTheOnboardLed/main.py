from machine import Pin
import time

time.sleep(0.1)

led_onboard = Pin("LED", Pin.OUT)

while True:
    led_onboard.value(1)
    time.sleep(1)
    led_onboard.value(0)
    time.sleep(1)
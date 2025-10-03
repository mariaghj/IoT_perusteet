from machine import Pin
import time

time.sleep(0.1)

led_onboard = Pin("LED", Pin.OUT)

while True:
    led_onboard.toggle()
    time.sleep(1)
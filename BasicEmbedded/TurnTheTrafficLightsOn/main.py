from machine import Pin
import time

time.sleep(0.1)

#Kun pull_down = 1 ja normaalitilassa = 0
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)
led_green = Pin(13, Pin.OUT)
led_yellow = Pin(14, Pin.OUT)
led_red = Pin(15, Pin.OUT)

leds = [led_green, led_yellow, led_red]


while True:
    if button.value() == 1:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            time.sleep(0.2)
            buzzer.value(0)
            time.sleep(0.2)
        led_red.value(0)

        
    for led in leds:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        if button.value == 1:
            break

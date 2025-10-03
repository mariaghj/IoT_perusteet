from machine import Pin
import utime

utime.sleep(0.1)

motion_sensor = Pin(19, Pin.IN)
led_red = Pin(2, Pin.OUT)
buzzer = Pin(13, Pin.OUT)


while True:
    if motion_sensor.value() == 1:
        led_red.value(1)
        buzzer.value(1)
        utime.sleep(3)
        led_red.value(0)
        buzzer.value(0)

    
    



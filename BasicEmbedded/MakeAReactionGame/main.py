from machine import Pin
import utime
import urandom

utime.sleep(0.1)

#Kun pull_down = 1 ja normaalitilassa = 0
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

#Global variables
timer_start = 0

# Inteerrupt handler
def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start) 
    #utime gives the info how many milliseconds has passed from the start of the timer.
    print("Your reaction time was "+ str(reaction_time) + "milliseconds.")

# Signal user to get ready
led.value(1)
utime.sleep(urandom.uniform(5,10))
#Turn off LED - signal to press the button
led.value(0)
timer_start = utime.ticks_ms() #Starts counting milliseconds after the led turns off

# Enable interrupt
button.irq(trigger = Pin.IRQ_RISING, handler= button_handler)
#1) button: mikä keskeyttää
#2) .irq: keskeytyskomento
#3) trigger = machine.Pin.IRQ_RISING :milloin triggeri keskeyttää
#4) , handler = button_handler :mihin mennään keskeytymisen jälkeen



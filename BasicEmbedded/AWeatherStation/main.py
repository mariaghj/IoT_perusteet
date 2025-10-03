from machine import Pin
from dht import DHT22
import utime

utime.sleep(0.1)


dht_sensor = DHT22(Pin(15, Pin.IN))


while True:
    dht_sensor.measure() #suorita mittaus
    temperature_celsius = dht_sensor.temperature()
    humidity_percent = dht_sensor.humidity()
    print("Temperature here is " + str(temperature_celsius) + "°C")
    print("Humidity here is " + str(humidity_percent) + "%")
    utime.sleep(0.3)
    break
    



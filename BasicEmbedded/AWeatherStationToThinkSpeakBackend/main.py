from machine import Pin
from dht import DHT22
import utime
import urequests
import network

utime.sleep(0.1)


dht_sensor = DHT22(Pin(15, Pin.IN))

# WiFi asetukset
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""
#ThinkSpeak asetukset
api_key = "6BFU0IOAMY2C3EPK"
base_url = "https://api.thingspeak.com/update"
# Yhdistä WiFiin
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)

print("Yhdistetään WiFiin...")
while not wifi.isconnected():
    utime.sleep(0.5)
print("Yhdistetty:", wifi.ifconfig())


while True:
    dht_sensor.measure() #suorita mittaus
    temperature_celsius = dht_sensor.temperature()
    humidity_percent = dht_sensor.humidity()
    print("Temperature here is " + str(temperature_celsius) + "°C")
    print("Humidity here is " + str(humidity_percent) + "%")

    url = "{}?api_key={}&field1={}&field2={}".format(
            base_url, api_key, temperature_celsius, humidity_percent
        )
    res = urequests.get(url)
    print("ThingSpeak vastaus:", res.text)
    res.close()

    utime.sleep(15)
    



import sys
import adafruit_dht
from board import D2 #my sensor is connected to D19 on RPi. adjust your pin accordingly
import time

# Parse command line parameters.
sensor_args = { '11': adafruit_dht.DHT11,
    '22': adafruit_dht.DHT22}
#        '2302': Adafruit_DHT.AM2302 } depreciated
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2] #ignoring this for testing purposes
else:
    sys.exit(1)

dht_device = adafruit_dht.DHT22(D2)

read_attempts = 0
while read_attempts < 15: # try for a reading 7 times since dht's are unreliable
       try:
               humidity = dht_device.humidity
               temperature = dht_device.temperature

               if humidity is not None and temperature is not None:
                   print('{0:0.1f} | {1:0.1f}'.format(temperature, humidity))
                   sys.exit(1)
       except RuntimeError as error:
               read_attempts += 1
               time.sleep(2.0)
               continue
       except Exception as error:
               read_attempts += 1
               dht_device.exit()
               raise error

       time.sleep(2.0)

print('-1 | -1')
sys.exit(1)
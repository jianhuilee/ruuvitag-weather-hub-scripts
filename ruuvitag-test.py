import time
import datetime, requests
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import json

tags = {
	'D1:1B:BC:83:E0:F1': '1: Baby',
	'F6:08:DA:81:D4:FD': '2: Outside'
}

timeout_in_sec = 5

for mac, name in tags.items():
	print("Looking for {} ({})".format(mac, name))
	datas = RuuviTagSensor.get_data_for_sensors(mac, timeout_in_sec)
	#print(datas)
	weatherdata = datas[mac]
	print(weatherdata)

print("Testing Done.")

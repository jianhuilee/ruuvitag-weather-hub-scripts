import time
import datetime, requests
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import json

import sqlite3

tags = {
        'D1:1B:BC:83:E0:F1': '1: Baby',
        'F6:08:DA:81:D4:FD': '2: Outside'
}

timeout_in_sec = 5

db_file = '/home/pi/ruuvitag/ruuvitag.db'

conn = sqlite3.connect(db_file)
# check if table exists
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sensors'")
row = cursor.fetchone()

if row is None:
        print("DB table not found. Creating 'sensors' table ...")
        conn.execute('''CREATE TABLE sensors
                (
                        id              INTEGER         PRIMARY KEY AUTOINCREMENT       NOT NULL,
                        timestamp       NUMERIC         DEFAULT CURRENT_TIMESTAMP,
                        mac             TEXT            NOT NULL,
                        name            TEXT            NULL,
                        temperature     NUMERIC         NULL,
                        humidity        NUMERIC         NULL,
                        pressure        NUMERIC         NULL
                        );''')
        print("Table created successfully\n")

for mac, name in tags.items():
        print("Looking for {} ({})".format(mac, name))
        datas = RuuviTagSensor.get_data_for_sensors(mac, timeout_in_sec)
        #print(datas)
        weatherdata = datas[mac]
        #print(weatherdata)
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        print("Saving data to database ...")
        conn.execute("INSERT INTO sensors (timestamp,mac,name,temperature,humidity,pressure) \
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".\
                format(now, mac, name, weatherdata['temperature'], weatherdata['humidity'], weatherdata['pressure']))

conn.commit()
conn.close()
print("Done.")

#!/bin/sh

db_file="/home/pi/ruuvitag/ruuvitag.db"
if [ -n $(find $db_file -type f -size +10485760c 2>/dev/null) ]; then
	prefix=$(date +%Y-%m-%d)
	mv $db_file /home/pi/ruuvitag/$prefix.db
fi

python3 /home/pi/work/RuuviTag-logger/ruuvitag-web.py &
while [ 1 ]
do
	python3 /home/pi/ruuvitag.py
	sleep 60
done

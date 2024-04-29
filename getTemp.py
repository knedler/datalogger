#!/usr/bin/python

import serial
import sqlite3
import datetime

try:
    # Connect to serial
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)

    # Write to serial
    ser.write(b'1')

    # Read response
    temp = ser.readline().decode().strip()

    # Close connection
    ser.close()

    # Connect to the database
    con = sqlite3.connect("/var/www/html/data.db")
    cur = con.cursor()

    # Make new table if needed
    cur.execute("create table if not exists temperature (DateTime text, Temp real)")

    # Get time and date
    dateTime = datetime.datetime.now().isoformat()

    # Insert into database
    cur.execute("Insert into temperature (DateTime, Temp) values (?, ?)", (dateTime, temp))
    con.commit()

except:
    quit()


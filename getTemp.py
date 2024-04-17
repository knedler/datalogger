#!/usr/bin/python

import serial
import sqlite3
import time

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
    con = sqlite3.connect("/home/blakeknedler/Documents/ECE_331/temperature-logger/data.db")
    cur = con.cursor()

    # Make new table if needed
    cur.execute("create table if not exists temperature (Date text, Time text, Temp real)")

    # Get time and date
    date = time.strftime('%F')
    time = time.strftime('%T')

    # Insert into database
    cur.execute("Insert into temperature (Date, Time, Temp) values (?, ?, ?)", (date, time, temp))
    con.commit()

except:
    quit()


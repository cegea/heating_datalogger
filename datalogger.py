#!/usr/bin/env python

import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)

gain = 10/3
volt_per_degree = 0.01

csv_file="datalogger.csv"

csv = open(csv_file,"w")

def main():
    while True:
        try:
            read_serial=ser.readline()
            e = float(read_serial)
            #print ("Voltaje: " + str(e))
            temperature = e/gain
            temperature = temperature/volt_per_degree
            temperature = float('%.3f'%(temperature))
            date = time.strftime('%X %x')
            row = date + "," + str(temperature) + "\n"
            csv.write(row)
            print (date + " Temperature: " + str(temperature))
            time.sleep(1)

        except KeyboardInterrupt:
            csv.close()

if __name__ == "__main__":
    main()

    


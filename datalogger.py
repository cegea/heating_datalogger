#!/usr/bin/env python

import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)                            # define serial port

gain = 10/3                                                         # gain of the amplifier
volt_per_degree = 0.01                                              # sensor sensibility

csv_file="datalogger.csv"                                           # local file to save data

def main():
    while True:
        try:
            read_serial=ser.readline()                              # read serial port
            e = float(read_serial)                                  # cast to float
            #print ("Voltaje: " + str(e))
            temperature = e/gain                                    # get op amp input voltage 
            temperature = temperature/volt_per_degree               # get temperature
            temperature = float('%.3f'%(temperature))               # truncate
            date = time.strftime('%X %x')                           # get time and date
            csv = open(csv_file,"a")                                # open the file to append data
            row = date + "," + str(temperature) + "\n"              # create string to add to the file
            csv.write(row)                                          # write data
            csv.close()                                             # close file
            print (date + " Temperature: " + str(temperature))      # print to terminal, debug
            time.sleep(120)                                         # non active wait of 2 minutes.

        except KeyboardInterrupt:
            csv.close()                                             # close file when ctrl+c

if __name__ == "__main__":                                          # main function
    main()

    


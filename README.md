# Heating Datalogger
Project to monitorize the heating system of my house. IoT Project.

# Motivation
Last year I got heating consumption counting installed. Since I got charged for the amount of water that flow through the counter (whether is hot or cold), I thought: "Hey, let´s stimate when the hot water inside the radiator is acctually getting the air around it warmer"

## Specifications
* Low cost
* Electronics
	* USB or 12V power input.
	* Temperature range: 0º - 90º Celsius.
	* Resolution 1º Celsius.
* Open door to fancy things.

## First prototype
The objetive of this prototype is to test and workaround some capabilities.
To keep things simple the proyect is now divided into two parts:
1. No Internet things:
	* Sensor.
	* Acconditionator.
	* Power supply.
	* ADC.
	* Serial communication.
2. Internet things:
	* Serial communication.
	* SSH, VNC, ...
	* CSV manipulation.

> Bottom - Top Architecture.

### 1. No Internet things
> Sensor + Aconditionator + Arduino
#### Sensor.
As I have laying around some LM35 from previous projects this is going to be the sensor used. From the datasheet:
* Calibrated Directly in Celsius (Centigrade).
* Linear +10mV/°C Scale Factor.
* 0.5°C Ensured Accuracy (at 25°C).
* Rated for Full −55°C to 150°C Range.
* Operates from 4 V to 30 V.
#### Acconditionator. 

* The reference voltage for the sensor will be 4.3V. The reference used is TL431, it has 445,33ppm/ºC deviation for this application.

* The LM358 Op Amp to addapt levels to the ADC. It can be single power supply powered. 
It´s  major downside is the input offset of 2mV. The error in Celsius is 2º. So for this prototype I´ll allow it. But is a big mistake!! The solution would be to use an OP07(75uV input offset) or similar with virtual ground.

#### Power supply.
The Arduino is powered from a 12V adapter. The aconditionator board could be battery powered sometime so I´ll fix it to 9V with an LM317 or LM7809.
#### ADC & Serial communication.
I´ll use the basic example sketch AnalogReadvoltage adding a delay to send data through the serial port.

### 2. Internet things
Just a Raspberry Pi (I´m usign the oldest model):
It does the following:
* Load the firmware into the Arduino.
* Read data from the serial port.
* Save data to a CSV file.
* Allow SSH or VNC to debug remotely and send the CSV file anywhere (rigth now my laptop).

# What to improve.
Just EVERYTHING.
Eventually I want the following:
* One single "brain" such as ESP8266 based board to send data over the "cloud".
* Battery operated.
* Meet specs, obviusly.

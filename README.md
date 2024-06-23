Raspberry Pi IoT Data Logger with MAX6675
This project demonstrates how to create an IoT data logger using a Raspberry Pi and a MAX6675 thermocouple temperature sensor. The system reads temperature data and logs it to a CSV file, which can be used for monitoring environments like greenhouses, server rooms, or home labs.

Hardware Requirements
  Raspberry Pi (any model)
  MAX6675 Thermocouple Temperature Sensor
  Jumper wires
  Breadboard
  SD card (with Raspbian installed)
  Power supply for Raspberry Pi
Software Requirements
   Raspbian OS (latest version)
   Python 3
   Adafruit MAX6675 library
Setup Instructions
 Hardware Setup
    Connect the VCC pin of the MAX6675 to the 3.3V pin of the Raspberry Pi.
    Connect the GND pin to a ground (GND) pin on the Raspberry Pi.
    Connect the CS pin to GPIO 5.
    Connect the SCK pin to GPIO 11 (SCLK).
    Connect the SO pin to GPIO 9 (MISO).

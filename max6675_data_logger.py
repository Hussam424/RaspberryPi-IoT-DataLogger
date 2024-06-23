import time
import csv
import board
import digitalio
import adafruit_max31855

# set up the SPI communication
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)#chip select pin
sensor = adafruit_max31855.MAX31855(spi, cs)

#set CSV file path
CSV_FILE = "/home/hrpi99/Desktop/data_log.csv"
OFFSET = 23.00

#function to log data

def log_data():
    with open(CSV_FILE,'a') as file:
	     writer = csv.writer(file)
	     while True:
	      temperature = sensor.temperature
	      if temperature is not None:
                  temperature -= OFFSET
                  print(f"Temperature: {temperature:.2f}C")
                  writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"),temperature])
                  file.flush()
                  print(f"logged: Temp={temperature:.2f}C")
	      else:
	          print("Failed o retrieve data from sensor")
	      time.sleep(30)

if __name__ == "__main__":
	print("Starting data logger")
	log_data()

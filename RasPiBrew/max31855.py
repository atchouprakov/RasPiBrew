from subprocess import Popen, PIPE, call
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

import os

class max31855:
    numSensor = 0
    def __init__(self, tempSensorId):
        self.tempSensorId = tempSensorId
        self.sensorNum = max31855.numSensor
        max31855.numSensor += 1


        # Raspberry Pi software SPI configuration.
        CLK = 25
        CS  = 24
        DO  = 18
        self.sensor = MAX31855.MAX31855(CLK, CS, DO)

        # # Raspberry Pi hardware SPI configuration.
        # SPI_PORT   = 0
        # SPI_DEVICE = self.sensorNum
        # self.sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
       
        print("Constructing 1W sensor %s"%(tempSensorId))

    def readTempC(self):

        temp_C = sensor.readTempC()
          
        return temp_C
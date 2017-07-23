from subprocess import Popen, PIPE, call
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31856.max31856 as MAX31856
import math
import os

class m31856:
    numSensor = 0
    def __init__(self, tempSensorId):
        self.tempSensorId = tempSensorId
        self.sensorNum = m31856.numSensor
        m31856.numSensor += 1


        # Raspberry Pi software SPI configuration.
        # CLK = 25
        # CS  = 24
        # DO  = 18
        # self.sensor = MAX31855.MAX31855(CLK, CS, DO)

        # Raspberry Pi hardware SPI configuration.
        SPI_PORT   = 0
        SPI_DEVICE = self.sensorNum
        self.sensor = MAX31856.MAX31856(hardware_spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
       
        print("Constructing 1W sensor %s"%(tempSensorId))

    def readTempC(self):
        temp_C = float('nan')       
        temp_C = self.sensor.read_temp_c()
        return temp_C


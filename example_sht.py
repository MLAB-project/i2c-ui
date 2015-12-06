#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
#logging.basicConfig(level=logging.DEBUG) 
import sys
from pymlab import config
import time
from src import mv

class dewpoint():
    def __init__(self, temp=None, hum=None):
        self.sens_temp = temp
        self.sens_hum = hum
        self.temp=0
        self.hum=0
        self.dewpoint=0

    def get_dp(self):
        if self.sens_temp:
            self.temp=self.sens_temp()
            self.hum=self.sens_hum()
        x = 1 - self.hum/100
        dewpoint = (14.55 + 0.114 * self.temp) * x
        dewpoint = dewpoint + ((2.5 + 0.007 * self.temp) * x) ** 3
        dewpoint = dewpoint + (15.9 + 0.117 * self.temp) * x ** 14
        self.dewpoint = self.temp - dewpoint
        return self.dewpoint

def main():

    if len(sys.argv) != 2:
        sys.stderr.write("Invalid number of arguments.\n")
        sys.stderr.write("Usage: %s Project_file (without extension)\n" % (sys.argv[0], ))
        sys.exit(1)

        filename = sys.argv[1]

        cfg = config.Config(
            i2c = {
                "port": 1,
            },
            bus = [{
                    "name": "sht25", "type": "sht25",
                },
            ],
        )

        cfg.initialize()

        sensorsSHT = cfg.get_device("sht25")
        dp = dewpoint(sensorsSHT.get_temp, sensorsSHT.get_hum)
        mVis = mv.MlabVisualiser(filename)              # initialize class with log filename

        mVis.addDataset("TempSHT", "Temperature [C]", sensorsSHT.get_temp)  # add sensors with labels, values and callbacks
        mVis.addDataset("HumiSHT", "RelativeHumidity [%]", sensorsSHT.get_hum)
        mVis.addDataset("DewpSHT", "Temperature [C]", dp.get_dp)

        mVis.run(input=["TempLTS", "TempSHT", "HumiSHT", "DewpSHT"], delay=1000, repeat=0) # infinity value reader, from sensor with labels in 1st array.
        mVis.startWeb()

    if __name__ == '__main__':
        main()

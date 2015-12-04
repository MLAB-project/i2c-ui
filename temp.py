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

    def set_dp(self, temp, hum):
        self.temp=temp
        self.hum=hum

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
        bus = [
            {
                "name": "lts01", "type": "lts01", "address": 0x48
            },{
                "name": "sht25", "type": "sht25",
            },
        ],
    )

    cfg.initialize()

    teplomer01 = cfg.get_device("lts01")
    vlhkost = cfg.get_device("sht25")
    dp = dewpoint(vlhkost.get_temp, vlhkost.get_hum)
                                                # initialize class with log filename
    mVis = mv.MlabVisualiser(filename)
                                                # add sensors with labels, values and callbacks
    mVis.addDataset("TempLTS", "Temperature [C]", teplomer01.get_temp)
    mVis.addDataset("TempSHT", "Temperature [C]", vlhkost.get_temp)
    mVis.addDataset("HumiSHT", "RelativeHumidity [%]", vlhkost.get_hum)
    mVis.addDataset("DewpSHT", "Temperature [C]", dp.get_dp)

                                                # this save values only once (optional)
    #mVis.getValue("Teplota01")
    #mVis.getValue("Teplota02")
    #mVis.getValue("vlhkost")
                                                # infinity value reader, from sensor with labels in 1st array.
    mVis.run(["TempLTS", "TempSHT", "HumiSHT", "DewpSHT"], delay=1000, repeat=0)
    print mVis.getSensors()
    mVis.startWeb()


if __name__ == '__main__':
    main()

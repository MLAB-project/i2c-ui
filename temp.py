#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
#logging.basicConfig(level=logging.DEBUG) 
import sys
from pymlab import config
import time
from src import mv


def main():

    if len(sys.argv) != 2:
        sys.stderr.write("Invalid number of arguments.\n")
        sys.stderr.write("Usage: %s Project_file (without extension)\n" % (sys.argv[0], ))
        sys.exit(1)

    filename = sys.argv[1]

    cfg = config.Config(
        i2c = {
            "port": 0,
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
    print teplomer01.get_temp()
                                                # inicialize class and add sensors with labels, values and callbacks
    mVis = mv.MlabVisualiser(filename)
    mVis.addDataset("Teplota01", "Temperature [C]", teplomer01.get_temp)
    mVis.addDataset("Teplota02", "Temperature [C]", vlhkost.get_temp)
    mVis.addDataset("vlhkost", "RelativeHumidity [%]", vlhkost.get_hum)
                                                # this save values only once
    mVis.getValue("Teplota01")
    mVis.getValue("Teplota02")
    mVis.getValue("vlhkost")
                                                # infinity value reader, from sensor with labels in 1st array.
    mVis.run(["Teplota01", "Teplota02", "vlhkost"], delay=1000, repeat=0)
    print mVis.getSensors()
    mVis.startWeb()


if __name__ == '__main__':
    main()
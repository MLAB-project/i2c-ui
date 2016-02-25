#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
#logging.basicConfig(level=logging.DEBUG) 
import sys
#from pymlab import config
import random
import time
from src import mv


def main():

    if len(sys.argv) != 2:
        sys.stderr.write("Invalid number of arguments.\n")
        sys.stderr.write("Usage: %s Project_file (without extension)\n" % (sys.argv[0], ))
        sys.exit(1)

    filename = sys.argv[1]

                                               # initialize class with log filename
    mVis = mv.MlabVisualiser(filename)
                                                # add sensors with labels, values and callbacks
    mVis.addDataset("random", "[X]", random.random)
    mVis.addDataset("random2", "[X]", random.random)

                                                # infinity value reader, from sensor with labels in 1st array.
    mVis.run(["random", "random2"], delay=1000, repeat=0)
    print mVis.getSensors()
    mVis.startWeb()


if __name__ == '__main__':
    main()

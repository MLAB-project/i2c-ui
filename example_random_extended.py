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
        sys.stderr.write("Usage: %s Project_file (without extension) it will be extended by file number and date\n" % (sys.argv[0], ))
        sys.exit(1)

    filename = sys.argv[1]
                                               # initialize class with log filename
    mVis = mv.MlabVisualiser(projectName=filename, LocalWebTime=1, filedivide=1)
                                                # add sensors with labels, values and callbacks
    mVis.addDataset("random", "[X]", random.random)

                                                # infinity value reader, from sensor with labels in 1st array.
    mVis.run(["random"], delay=10, repeat=0)
    print mVis.getSensors()
    mVis.startWeb()


if __name__ == '__main__':
    main()

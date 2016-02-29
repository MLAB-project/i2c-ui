#!/usr/bin/env python

import sys
import pymlab
import rospy
import time
from pymlab import config
import sensor_server
from std_msgs.msg import String
from sensor_server.srv import *


if __name__ == "__main__":
    i2c = '''{
            "port": 1,
        }'''
    bus = '''[
                {
                    "name":           "lts01",
                    "type":           "lts01",
                },
                {
                    "name":           "sht25",
                    "type":           "sht25",
                },
            ]'''


    rospy.init_node('pymlab_client', anonymous=True)

    pymlab = rospy.ServiceProxy('pymlab_init', PymlabInit)
    odpoved = pymlab(i2c=i2c, bus=bus)
    print odpoved

    pymlab = rospy.ServiceProxy('pymlab', GetSensVal)
    odpoved = pymlab(data = "{'sht': 'get_temp', 'rate': 10, 'start': True, 'methods': {'sht25':{'get_temp', 'get_hum'},'lts01':{'get_temp'}}}")
    print odpoved

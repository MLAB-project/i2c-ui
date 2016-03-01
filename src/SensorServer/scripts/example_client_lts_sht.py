#!/usr/bin/env python

import sys
import pymlab
import rospy
import time
from pymlab import config
import sensor_server
from std_msgs.msg import String
from sensor_server.srv import *
from sensor_server.msg import *



if __name__ == "__main__":
    i2c = '''{
            "port": 1,
        }'''
    bus = '''[
                {
                    "name":           "Teplomer01",
                    "type":           "lts01",
                },
                {
                    "name":           "Vlhkomer01",
                    "type":           "sht25",
                },
            ]'''


    msgP_pymlab_server = rospy.Publisher('pymlab_server', PymlabServerStatusM, queue_size=10)
    rospy.init_node('pymlab_client', anonymous=True)

    pymlab = rospy.ServiceProxy('pymlab_init', PymlabInit)
    print pymlab(i2c=i2c, bus=bus)
    
    msgP_pymlab_server.publish(name = "", data="{'rate': 10, 'start': True, 'AutoInputs': {'Vlhkomer01':{'get_temp', 'get_hum'},'Teplomer01':{'get_temp'}}}")


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
            ]'''
    pymlab_init = rospy.ServiceProxy('pymlab_init', PymlabInit, headers= {'i2c':i2c, 'bus':bus} )
    pymlab = rospy.ServiceProxy('pymlab', GetSensVal)
    rospy.init_node('pymlab_client', anonymous=True)

    rospy.loginfo("init")
    time.sleep(1)
    odpoved = pymlab_init(i2c=i2c, bus=bus)
    print odpoved
    odpoved = pymlab("ahoj", "maje")

    print "%s + %s = %s"%(2, 1, odpoved)
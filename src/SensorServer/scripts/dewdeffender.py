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
                    "name":         "TeplomerZarovka",
                    "type":         "lts01",
                },
                {
                    "name":         "Topeni",
                    "type":         "i2cpwm",
                },
                {
                    "name":         "Meteostanice",
                    "type":         "sht25",
                },
            ]'''


    msgP_pymlab_server = rospy.Publisher('pymlab_server', PymlabServerStatusM, queue_size=10)
    rospy.init_node('pymlab_client', anonymous=True)

    pymlab = rospy.ServiceProxy('pymlab_init', PymlabInit)
    print pymlab(i2c=i2c, bus=bus)


    msgP_pymlab_server.publish(
    name = "DewDeffender",
    data = '''{ "rate": 10,
        "start": True,
        "AutoInputs": {
                "Meteostanice":{
                                        "get_temp",
                                        "get_hum"
                },
                "TeplomerZarovka":{
                                        "get_temp"
                }
        },
        "Inputs":{
                "Meteostanice":{
                                        "get_temp",
                                        "get_hum"
                },
                "TeplomerZarovka":{
                                        "get_temp"
                }
        },
        "Outputs": {
                "Topeni":{
                                        "set_ls0",
                                        "set_ls1",
                                        "set_pwm0",
                                        "set_pwm1",
                }
        }
    }''')

    #srv_PymlabSetValue = rospy.ServiceProxy('pymlab_drive/set', PymlabSetValue)
    #srv_PymlabGetValue = rospy.ServiceProxy('pymlab_drive/get', PymlabGetValue)
    srv_PymlabValue = rospy.ServiceProxy('pymlab_drive', PymlabSetValue)
    print srv_PymlabValue(device="Topeni", method="set_ls0", parameters=str([0b11111111]))
    print srv_PymlabValue(device="Topeni", method="set_ls1", parameters=str([0b11111111]))

    while not rospy.is_shutdown():
        print "----"
        for x in xrange(1,99,2):
            print srv_PymlabValue(device="Topeni", method="set_pwm0", parameters="[100,%s]" %(str(x))), " - ",
            print srv_PymlabValue(device="Topeni", method="set_pwm1", parameters="[100,%s]" %(str(100-x)))
            time.sleep(0.1)

        time.sleep(0.5)
#!/usr/bin/env python

import rospy
import pymlab
from pymlab import config
import sys
import sensor_server
#from std_msgs.msg import String
import std_msgs
from sensor_server.srv import *

def server(req):
    print req
    print "Returning [%s + %s]"%(req.name, req.data)
    return GetSensValResponse( 10 )

class pymlab_server():
    def __init__(self):
        pass

    def init(self, cfg=None):
        print cfg
        i2c = {
                "port": 1,
            }
        bus = [
                    {
                        "name":           "lts01",
                        "type":           "lts01",
                    },
                ]
        self.pymlab_config = config.Config(i2c = eval(cfg.i2c), bus = eval(cfg.bus))
        self.pymlab_config.initialize()
        self.lts_sen = self.pymlab_config.get_device("lts01")
        print "done"
        return True

    def getvalue(self, name=None, type=None, value=None):
        print name, type, value
        val = int(float(self.lts_sen.get_temp()))
        print "value je tohle:", val
        return GetSensValResponse(val)

def add_two_ints_server():
    ps = pymlab_server()
    rospy.init_node('pymlab_node')
    s1 = rospy.Service('pymlab_init', PymlabInit, ps.init)
    s2 = rospy.Service('pymlab', GetSensVal, ps.getvalue)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
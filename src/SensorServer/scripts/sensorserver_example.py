#!/usr/bin/env python

import rospy
import pymlab
from pymlab import config
import sys
import sensor_server
from std_msgs.msg import String
from std_msgs.msg import Float32
import std_msgs
from sensor_server.srv import *
from sensor_server.msg import *

def server(req):
    print req
    print "Returning [%s + %s]"%(req.name, req.data)
    return GetSensValResponse( 10 )

class pymlab_server():
    def __init__(self):
        pass

    def init(self, cfg=None):
        self.status = False
        self.init = cfg
        self.devices = {}
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
        for x in eval(cfg.devices):
            self.devices[x] = self.pymlab_config.get_device(eval(cfg.devices)[x])
        #for x in self.devices:
        #    print self.devices[x].get_temp()

        return True

    def getvalue(self, cfg=None):
        print "getval>>"
        print cfg
        val = int(float(self.lts_sen.get_temp()))
        print "value je tohle:", val
        return GetSensValResponse(val)

    def status(self, cfg=None):
        print "status>>"
        print cfg
        self.rate = 1
        ecfg = eval(cfg.data)
        print ecfg
        if 'rate' in ecfg:
            self.rate = ecfg['rate']
            print "rate", self.rate
        if 'methods' in ecfg:
            self.methods = ecfg['methods']
            print "methods", self.methods
        if "start" in ecfg:
            self.status = True
            rate = rospy.Rate(self.rate)
            methods = self.methods
            devices = self.devices
            #sender = rospy.Publisher('pymlab_data', String)
            sender = rospy.Publisher('pymlab_data', SensorValues)
            print sender
            while not rospy.is_shutdown():
                for x in methods:
                    print x
                    data = getattr(devices[x], methods[x])()
                    sender.publish(name=str(devices[x]), value=data)
                rate.sleep()


def add_two_ints_server():
    ps = pymlab_server()
    rospy.init_node('pymlab_node')
    s1 = rospy.Service('pymlab_init', PymlabInit, ps.init)
    s2 = rospy.Service('pymlab', GetSensVal, ps.status)
    rospy.Subscriber("pymlab_status", String, ps.status)
    print "Ready to get work."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
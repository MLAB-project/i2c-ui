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
        Local_devices = {}
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
        print cfg.bus
        for _x in eval(cfg.bus):
            print _x, _x['name'], _x['type']
            self.devices[_x['name']] = self.pymlab_config.get_device(_x['name'])
            print getattr(self.devices[_x['name']], "get_temp")(), self.devices[_x['name']]
        rospy.set_param("devices", str(self.devices))
        print self.devices

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
            rospy.set_param("rate", float(self.rate))
            print "rate", self.rate
        if 'methods' in ecfg:
            self.methods = ecfg['methods']
            rospy.set_param("methods", str(self.methods))
            print "methods", self.methods
        if "start" in ecfg:
            self.status = True
            rate = rospy.Rate(self.rate)
            methods = self.methods
            devices = self.devices
            #senderTest = rospy.Publisher('pymlab', Float32)
            sender = rospy.Publisher('pymlab_data', SensorValues, queue_size=20)
            print sender
            while not rospy.is_shutdown():
                for x in methods:
                    print "---", x
                    for y in methods[x]:
                        data = getattr(self.devices[devices[x].name], y)()
                        print "dantaout>>", data
                        sender.publish(name=str(devices[x].name)+"/"+str(y), value=data)
                        #senderTest.publish(data)
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
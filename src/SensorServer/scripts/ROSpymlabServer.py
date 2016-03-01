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
        self.pymlab_read = False # slouzi k ochrane pymlabu pred pokusem o dve cteni zaroven ...

    def init(self, cfg=None):
        self.status = False
        self.init = cfg
        self.cfg_i2c = eval(cfg.i2c)
        self.cfg_bus = eval(cfg.bus)
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
        self.pymlab_config = config.Config(i2c = self.cfg_i2c, bus = self.cfg_bus)
        self.pymlab_config.initialize()
        print self.cfg_bus
        for x in self.cfg_bus:
            print "init >> ", x, x['name'], x['type']
            self.devices[x['name']] = self.pymlab_config.get_device(x['name'])
        rospy.set_param("devices", str(self.devices))
        print "self.devices>>", self.devices

        return True

    def getvalue(self, cfg=None):
        print "getval>>"
        print cfg
        val = int(float(self.lts_sen.get_temp()))
        print "value je tohle:", val
        return GetSensValResponse(val)

    def status(self, cfg=None):
        print "status>>", 
        print cfg
        self.rate = 1
        try:                            # pokud je servis s GetSensVal, tak se pouzije toto, 
            ecfg = eval(cfg.data)
        except Exception, e:            # toto je pro zpravu 'pymlab_server'
            ecfg = eval(cfg)
        print ecfg
        if 'rate' in ecfg:
            self.rate = ecfg['rate']
            print "Vlastni frekvence", self.rate
        rospy.set_param("rate", float(self.rate))
        if 'AutoInputs' in ecfg:
            self.AutoInputs = ecfg['AutoInputs']
            rospy.set_param("AutoInputs", str(self.AutoInputs))
        if "start" in ecfg:
            self.status = True
            rate = rospy.Rate(self.rate)
            AutoInputs = self.AutoInputs
            devices = self.devices
            sender = rospy.Publisher('pymlab_data', SensorValues, queue_size=20)
            values = {}
            for x in AutoInputs:
                for y in AutoInputs[x]:
                    print "AutoInputs >>", x, y, 
                    print str(x)+"/"+str(y), str(x)+"/"+str(y)
                    values[str(x)+"/"+str(y)] = str(x)+"/"+str(y)
            rospy.set_param("values", values)
            print "\n run \n\n"
            while True:
                print "\r",
                for x in AutoInputs:
                    for y in AutoInputs[x]:
                        while self.pymlab_read: pass
                        self.pymlab_read = True
                        data = getattr(self.devices[devices[x].name], y)()
                        self.pymlab_read = False
                        print x, "%.3f"%data, "||",
                        sender.publish(name=str(devices[x].name)+"/"+str(y), value=data)
                        #senderTest.publish(data)
                print "\r",
                rate.sleep()
            return True

    def drive(self, cfg):
        #print cfg
        raval = "---"
        reval = getattr(self.devices[cfg.device], cfg.method)(*eval(cfg.parameters))
        return str(reval)


def main():
    ps = pymlab_server()
    rospy.init_node('pymlab_node')

    rospy.Subscriber("pymlab_server", PymlabServerStatusM, ps.status)
    s1 = rospy.Service('pymlab_init', PymlabInit, ps.init)
    s2 = rospy.Service('pymlab_server', PymlabServerStatus, ps.status)
    s3 = rospy.Service('pymlab_drive', PymlabSetValue, ps.drive)

    print "Ready to get work."
    rospy.spin()

if __name__ == "__main__":
    main()
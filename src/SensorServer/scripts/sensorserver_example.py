#!/usr/bin/env python

import rospy
import sensor_server
from sensor_server.srv import *

def server(req):
    print req
    print "Returning [%s + %s]"%(req.name, req.data)
    return GetSensValResponse( 10 )

def add_two_ints_server():
    rospy.init_node('pymlab_node')
    s = rospy.Service('pymlab', GetSensVal, server)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
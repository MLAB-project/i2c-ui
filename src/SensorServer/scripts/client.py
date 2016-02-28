#!/usr/bin/env python

import sys
import rospy
import sensor_server
from sensor_server.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('pymlab')
    print "aaa"
    try:
        pymlab = rospy.ServiceProxy('pymlab', GetSensVal)
        odpoved = pymlab(x, y)
        return odpoved.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = str(sys.argv[1])
        y = str(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
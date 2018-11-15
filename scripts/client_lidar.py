#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan #import des donnes laser du lidar
import time
from rplidar_ros.srv import *

class Client():

    vel=None
    angle_est=None
    #Init
    def __init__(self):
        rospy.init_node('client_lidar')
  
    def listen_angle(self):
      r = rospy.Rate(10)
      while not rospy.is_shutdown():
	self.angle_est=rospy.ServiceProxy('angle',angle)
	self.angle_est()
        print(self.angle_est().angle_mes)

########################################################## Main ######################################################
if __name__ == "__main__":
    l=Client()
    l.listen_angle()
    rospy.spin()

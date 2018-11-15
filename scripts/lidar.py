#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan #import des donnes laser du lidar
import time
from rplidar_ros.srv import *



class detection():
  sub_pos=None
  temps=None
  lidar_service=None
  angle_min=None
 
  #Init
  def __init__(self):
    rospy.init_node('lidar')
    self.temps=time.time()
    self.sub_pos=rospy.Subscriber('/scan',LaserScan,self.callback)
    print("donnes recu dans le subscriber ET fin d'Init")
    
    self.lidar_service=rospy.Service('angle',angle,self.angle_pose)
    

    
  def angle_pose(self,data):
    return self.angle_min
    
            

  def callback(self, data):
    minimum=None
    index_min=None
    angle=None
    minimum=min(data.ranges)
    index_min=data.ranges.index(minimum)
    angle=data.angle_min+index_min*data.angle_increment
    
    print("   ")
    print("distance min       : ", min(data.ranges))
    #print("index val          : ",index_min)
    print("angle de detection : ",math.degrees(angle))
    self.angle_min=math.degrees(angle)
  
if __name__ == "__main__":
    d=detection()
    while not rospy.is_shutdown() and time.time()<d.temps+100:
      pass


#!/usr/bin/env python3

name = 'tz2019_loatt_tuning_directions'

import rospy
import time
import std_msgs.msg

import tz2019_controler

rospy.init_node(name)

loatt_h = tz2019_controller.loatt_v()
loatt_v = tz2019_controller.loatt_h()

loatt_h_tuning = input("Lo h-band Att tuning vol: ")  #set Lo Att tuning vol
loatt_v_tuning = input("Lo v-band Att tuning vol: ")
loatt_h.set_vol(loatt_h_tuning)
loatt_v.set_vol(loatt_v_tuning)

#!/usr/bin/env python3

name = 'tz2019_loatt_tuning_directions'

import rospy
import time
import std_msgs.msg

import tz2019_tuning_controler

rospy.init_node(name)

loatt_tuning = tz2019_tuning_controler.loatt_tuning()

loatth_tuning = input("Lo h-band Att tuning vol: ")  #set Lo Att tuning vol
loattv_tuning = input("Lo v-band Att tuning vol: ")
loatt_tuning.set_loatth_tuning(loatth_tuning)
loatt_tuning.set_loattv_tuning(loattv_tuning)

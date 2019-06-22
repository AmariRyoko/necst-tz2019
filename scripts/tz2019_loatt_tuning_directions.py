#!/usr/bin/env python3

name = 'tz2019_loatt_tuning_directions'

import rospy
import time
import std_msgs.msg

import tz2019_controler

rospy.init_node(name)

loatt_h = tz2019_controller.loatt_v()
loatt_v = tz2019_controller.loatt_h()

parser = argparse.ArgumentParser(description = 'set Lo Att level of h-band and v-band')

parser.add_argument('loatt_h_tuning', type = float, help = 'set Lo Att level of h-band')
parser.add_argument('loatt_v_tuning', type = float, help = 'set Lo Att level of v-band')

args = parser.parse_args()

loatt_h.set_vol(loatt_h_tuning)       #set Lo Att tuning vol
loatt_v.set_vol(loatt_v_tuning)

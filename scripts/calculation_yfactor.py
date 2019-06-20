#!/usr/bin/env python3

name = 'calculation_yfactor'

import rospy
import std_msgs.msg
import numpy
import sys, os, time, datetime

sys.path.append("/ogawa-ros/necst-sisrx/scripts")
import yfactor_with_set_sis_vol_direction

hot =
cold = 

#under the calculation

y_db = hot - cold
y_w = 10^((y_db)/10)
trx = (300 - 77*(y_w))/((y_w)-1)

print(trx)

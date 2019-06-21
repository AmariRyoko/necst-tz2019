#!/usr/bin/env python3

name = 'calculation_irr'

import rospy
import std_msgs.msg
import numpy as np
import sys, os, time, datetime

sys.path.append("/ogawa-ros/necst-sisrx/scripts")
import yfactor_irr_directions


#under the calculation irr

g1u = np.
g2u = np.
g1l = np.
g2l = np.
p1 = #yfactor_upperside
p2 = #yfactor_lowerside

mu = (g1u)/(g2u)
ml = (g2l)/(g1l)
mdsb = (p1)/(p2)

r1 = mu*((ml)*(mdsb)-1)/((mu)-(mdsb))
r2 = ml*((mu)-(mdsb))/((ml)*(mdsb)-1)

print('IRR R1: %f' %(r1))
print('IRR R2: %f' %(r2))

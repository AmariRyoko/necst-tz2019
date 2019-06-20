#!/usr/bin/env python3

name = 'calculation_yfactor'

import rospy
import std_msgs.msg
import numpy as np
import sys, os, time, datetime

sys.path.append("/ogawa-ros/necst-sisrx/scripts")
import yfactor_irr_directions


#under the calculation irr

g1u =
g2u =
g1l =
g2l =

mu = (g1u)/(g2u)
ml = (g2l)/(g1l)
mdsb = ((g1u)+(g1l))/((g2u)+(g2l))

r1 = mu*((ml)*(mdsb)-1)/((mu)-(mdsb))
r2 = ml*((mu)-(mdsb))/((ml)*(mdsb)-1)

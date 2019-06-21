#!/usr/bin/env python3

name = 'sis_iv_curve_plot'

import os, sys, time, datetime
import rospy
import numpy
import matplotlib.pyplot as plt
import std_msgs.msg

import sis_bias_curve_with_first_set_loatt_level_direction

#under the i-v graph plot

plt.title('SIS_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
iv = numpy.()
plt.plot(iv[:,0], iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')
plt.savefig('tz_iv_curve_.png')
plt.show()

#!/usr/bin/env python3

name = 'sis_iv_curve_plot'

import os, sys, time, datetime
import rospy
import numpy
import matplotlib.pyplot as plt
import std_msgs.msg

import sis_bias_curve_with_first_set_loatt_level_direction

#under the i-v graph plot

plt.subplot(221)
plt.title('SIS_V1_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
v1_iv = numpy.()
plt.plot(v1_iv[:,0], v1_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(222)
plt.title('SIS_H1_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
h1_iv = numpy.()
plt.plot(h1_iv[:,0], h1_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(223)
plt.title('SIS_H2_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
h2_iv = numpy.()
plt.plot(h2_iv[:,0], h2_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(224)
plt.title('SIS_V2_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
v2_iv = numpy.()
plt.plot(v2_iv[:,0], v2_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.savefig('tz_iv_curve_.png')
plt.show()

#!/usr/bin/env python3

name = 'sis_iv_curve_plot'

import os, sys
import matplotlib.pyplot as plt
import std_msgs.msg
import pandas

import necstdb

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

db = necstdb.necstdb()
db.open(file_name)

#under the i-v graph plot

plt.subplot(221)
plt.title('SIS_V1_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
plt.plot(v1_iv[:,0], v1_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(222)
plt.title('SIS_H1_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
plt.plot(h1_iv[:,0], h1_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(223)
plt.title('SIS_H2_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
plt.plot(h2_iv[:,0], h2_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.subplot(224)
plt.title('SIS_V2_IV')
plt.xlabel('V[mV]')
plt.ylabel('I[uA]')
plt.xlim(-11, 11)
plt.ylim(-200, 200)
plt.plot(v2_iv[:,0], v2_iv[:,1], lonestyle = 'solid', marker = None, coler = 'red')

plt.savefig('tz_iv_curve_.png')
plt.show()

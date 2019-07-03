#!/usr/bin/env python3

name = 'sis_iv_curve_plot'

import os, sys
import matplotlib.pyplot as plt
import std_msgs.msg
import pandas

import necstdb

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('file_name', type = str, help = 'set saving file name')

args = parser.parse_args()

db = necstdb.necstdb()
db.open(file_name)

d = db.read_as_pandas()
d['time'] = pandas.to_datetime(d['time'], unit='s')
d['data'] = [_[0][data] for _ in d['msgs']]
d2 = d.set_index(['topic', 'time']).sort_index()

dd = pandas.concat(
    [
        d2.loc['/tz2019/sis_v1/v'][['data']].rename(columns={'data': 'V1V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v1/i'][['data']].rename(columns={'data': 'V1I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h1/v'][['data']].rename(columns={'data': 'H1V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h1/i'][['data']].rename(columns={'data': 'H1I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v2/v'][['data']].rename(columns={'data': 'V2V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_v2/i'][['data']].rename(columns={'data': 'V2I'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h2/v'][['data']].rename(columns={'data': 'H2V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/tz2019/sis_h2/i'][['data']].rename(columns={'data': 'H2I'}).astype(float).resample('0.1S').mean(),
    ],
    axis = 1,
)

#under the i-v graph plot

fig = matplotlib.pyplot.figure(figsize=(7, 6))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
ax[0].plot(dd['V1V'], dd['V1I'], '.')
ax[1].plot(dd['H1V'], dd['H1I'], '.')
ax[2].plot(dd['V2V'], dd['V2I'], '.')
ax[3].plot(dd['H2V'], dd['H2I'], '.')
[_.set_xlabel('Voltage (mV)') for _ in ax]
[_.set_ylabel('Current (uA)') for _ in ax]
[_.grid(True, linestyle=':') for _ in ax]

plt.savefig('tz_iv_curve_.png')
plt.show()

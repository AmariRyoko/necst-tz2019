#!/usr/bin/env python3

def iv_plot(file_name, save_name):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas

    import necstdb

    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
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

    fig = plt.figure(figsize=(7, 6))
    ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
    ax[0].plot(dd['V1V'], dd['V1I'], '.')
    ax[1].plot(dd['H1V'], dd['H1I'], '.')
    ax[2].plot(dd['V2V'], dd['V2I'], '.')
    ax[3].plot(dd['H2V'], dd['H2I'], '.')
    ax[0].set_title('V1 I-V')
    ax[1].set_title('H1 I-V')
    ax[2].set_title('H2 I-V')
    ax[3].set_title('V2 I-V')
    [_.set_xlabel('Voltage (mV)') for _ in ax]
    [_.set_ylabel('Current (uA)') for _ in ax]
    [_.grid(True, linestyle=':') for _ in ax]

    plt.suptitle(str(save_name))
    #plt.show()
    graph_file_name = '/home/exito/data/logger/test/' + str(save_name) +'.png'
    plt.savefig(graph_file_name)

    return graph_file_name



def att_iv_plot(file_name, save_name, att_vol):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas

    import necstdb

    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
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

    fig = plt.figure(figsize=(7, 6))
    ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
    ax[0].plot(dd['V1V'], dd['V1I'], '.')
    ax[1].plot(dd['H1V'], dd['H1I'], '.')
    ax[2].plot(dd['V2V'], dd['V2I'], '.')
    ax[3].plot(dd['H2V'], dd['H2I'], '.')
    ax[0].set_title('V1 I-V')
    ax[1].set_title('H1 I-V')
    ax[2].set_title('H2 I-V')
    ax[3].set_title('V2 I-V')
    [_.set_xlabel('Voltage (mV)') for _ in ax]
    [_.set_ylabel('Current (uA)') for _ in ax]
    [_.grid(True, linestyle=':') for _ in ax]

    plt.suptitle('att_level = ' + str(att_vol))
    #plt.show()
    graph_file_name = '/home/exito/data/logger/test/' + str(save_name) + '/fig_att_level=' + str(att_vol) +'.png'
    plt.savefig(graph_file_name)

if __name__ == '__main__':
    iv_plot(file_name, save_name)

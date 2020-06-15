import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SERIES = 'outdoor'
FILEPATH = './' + SERIES + '/results/'
COOKEDPATH = './' + SERIES + '/cooked/'
COOKED_TRACE_FOLDER = './' + SERIES + '/result/test/'

csv_filepath = FILEPATH
csv_files = os.listdir(csv_filepath)

stat_name = []
stat_avg = []
stat_cov = []
for csv_file in csv_files:
    index = csv_file.find('.')
    file_name = csv_file[:index]
    file_path = csv_filepath + csv_file
    #file = csv.reader(open(file_name))
    df = ''
    #if 'result_bus 2018-06-01' not in file_name:
    #    continue;
    df = pd.read_csv(file_path, usecols=['Timestamp', 'Download'])
    #cooked_file = open(COOKEDPATH + file_name, 'wb')
    #cooked_file.write(df.to_string())
    #cooked_file.close()

    ts = pd.Series(df['Download'])
    ts /= 1000000
    avg = np.average(ts)
    cov = np.cov(ts)
    stat_name.append(file_name)
    stat_avg.append(avg)
    stat_cov.append(np.sqrt(cov))
    #ts = ts.cumsum()
    timestamps = []

    for timestamp in df['Timestamp']:
        timestamps.append(pd.Timestamp(timestamp))


    #continue
    #ts.plot(index=timestamps)
    #plt.xticks(rotation=25)
    #plt.plot(timestamps, ts)
    #plt.legend(''+ 'Avg:' + str(avg) + 'Mbps' + 'Cov:' + str(cov))
    #plt.ylabel('Bandwidth(bps)')
    #plt.xlabel('Index')
    #plt.title(SERIES + ' ' + file_name)
    #plt.show()

print('avg: ' + str(np.average(stat_avg)))
print('cov: ' + str(np.average(stat_cov)))
#plt.plot(stat_avg)
#plt.plot(stat_cov)
#plt.show()
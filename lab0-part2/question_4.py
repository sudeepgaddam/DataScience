from pylab import *

import pandas as pd

log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
log_df['DateTime'] = pd.to_datetime(log_df.apply(lambda row: row['Time'], axis=1))

histo = log_df[['ClientID', 'DateTime']].groupby(lambda row:log_df['DateTime'][row].hour,sort=True).ClientID.nunique()

print histo
pd.Series.plot(histo,kind='bar')
show()

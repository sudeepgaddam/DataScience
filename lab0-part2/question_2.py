from pylab import *
import pandas as pd
log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
log_df['DateTime'] = pd.to_datetime(log_df.apply(lambda row: row['Date'] + ' ' + row['Time'], axis=1))
beforeNoon =log_df['DateTime'].map(lambda x : (x.year == 1998) & (x.month == 05) & (x.day == 01) & (x.hour < 12))
afterNoon =log_df['DateTime'].map(lambda x : (x.year == 1998) & (x.month == 05) & (x.day == 01) & (x.hour >= 12))
print "before Noon:"
print log_df[beforeNoon]['DateTime'].count()
print "After Noon:"
print log_df[afterNoon]['DateTime'].count()

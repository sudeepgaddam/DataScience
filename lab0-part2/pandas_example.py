from pylab import *
import pandas as pd
df = pd.DataFrame( {
'a' : [1, 2, 3, 4],
'b': [ 'w', 'x', 'y', 'z'] })
print df
log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
is_may1st = log_df['Date'] == '01/May/1998'
may1_df = log_df[is_may1st]
grouped = log_df.groupby(['ResponseCode','ClientID'])
#grouped = grouped.get_group(200)
log_df['DateTime'] = pd.to_datetime(log_df.apply(lambda row: row['Date'] + ' ' + row['Time'], axis=1))
hour_grouped =log_df.groupby(lambda row: log_df['DateTime'][row].hour)
#hour_grouped = log_df.groupby(lambda row: log_df['DateTime'][row].hour)
hour_grouped
print hour_grouped


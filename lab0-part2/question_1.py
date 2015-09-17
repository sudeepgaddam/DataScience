from pylab import *
import pandas as pd
log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
is_404 = log_df['ResponseCode'] == 404
print log_df[is_404][['ClientID']].groupby(['ClientID']).size()

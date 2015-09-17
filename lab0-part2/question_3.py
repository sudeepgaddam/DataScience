from pylab import *
import pandas as pd
log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
is_200 = log_df['ResponseCode'] == 200
df_200 = log_df[is_200]
df_200_images = df_200[df_200['URL'].str.contains('gif|jpg|jpeg|GIF|JPG')]
print "Mean: " + `df_200_images[['Size']].mean()` + "Standard deviation" + `df_200_images[['Size']].std()` 

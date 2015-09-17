##
##Command to convert to csv
## sudeepgaddam@sudeepgaddam:~/data_science/lab0-part2$ cat wc_day91_1.log | sed 's/\[//g; s/ +0000\]//g; s/"//g; s/Jul/07/g; s/\([0-9]\{2\}\)\/\(.*\)\/\([0-9]\{4\}\):/\3-\2-\1 /g' | cut -d ' ' -f 1,4,5,6,7,9,10 | awk '{print $1, $2, $3, $5, $6, $7}' > csvlab2.csv
##

from pylab import *
import pandas as pd
log_df = pd.read_csv("csvlab2.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'],sep=' ')
is_200 = log_df['ResponseCode'] == 200
df_200 = log_df[is_200]
df_200 = log_df[log_df['URL'].str.contains('gif|jpg|jpeg|GIF|JPG')]
print "images size  mean: " + `df_200[['Size']].mean()` + "Standard deviation" + `df_200[['Size']].std()` 

##Output
#python question_6.py images size  mean: Size    2764.377459
#dtype: float64Standard deviationSize    5939.885117
#dtype: float64


###


from pylab import *

import pandas as pd

log_df = pd.read_csv("csvlab2.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=[' '])
log_df['DateTime'] = pd.to_datetime(log_df.apply(lambda row: row['Time'], axis=1))

histo = log_df[['ClientID', 'DateTime']].groupby(lambda row:log_df['DateTime'][row].hour,sort=True).ClientID.nunique()

print histo
pd.Series.plot(histo,kind='bar')
show()


from pylab import *
import pandas as pd
import random
import matplotlib.pyplot as plt


##put 100 unique clients into list first
log_df = pd.read_csv("wc_day6_1_sample.csv", names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'], na_values=['-'])
log_df['DateTime'] = pd.to_datetime(log_df.apply(lambda row: row['Date'] + ' ' + row['Time'], axis=1))
clients = log_df['ClientID']
uniqueClients = clients.unique()

cnt = 0
clients_sel = []
while cnt<100:
        clients_sel.append(random.choice(uniqueClients))
        cnt = cnt + 1
cl = log_df[log_df['ClientID'].isin(clients_sel)]
cl['Hour'] = cl.apply(lambda row: row['DateTime'].hour, axis=1)


cl.plot(kind='scatter', x='ClientID', y='Hour');
plt.show()

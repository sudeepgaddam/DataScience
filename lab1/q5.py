import Levenshtein as L
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt
resto = pd.read_csv('restaurants.csv')
resto['dummy'] = 0
prod = pd.merge(resto, resto, on='dummy')


clusters = pd.merge(resto, resto, on='cluster')
clusters = clusters[clusters.id_x > clusters.id_y]
clusters[:10]


# Clean up
del prod['dummy']
del resto['dummy']

prod = prod[prod.id_x > prod.id_y]
prod['ratio'] = prod.apply(lambda r: L.ratio(r['name_x'], r['name_y']), axis=1)
prod['distance'] = prod.apply(lambda r: L.distance(r['name_x'], r['name_y']), axis=1)


def accuracy_distance(max_distance):
    similar = prod[prod.distance < max_distance]
    correct = float(sum(similar.cluster_x == similar.cluster_y))
    precision = correct / len(similar)
    recall = correct / len(clusters)
    return (precision, recall)

thresholds = range(1, 11)
p_dis = []
r_dis = []

for t in thresholds:
    acc_dis = accuracy_distance(t)
    p_dis.append(acc_dis[0])
    r_dis.append(acc_dis[1])


def accuracy(max_ratio):
    similar = prod[prod.ratio > max_ratio]
    correct = float(sum(similar.cluster_x == similar.cluster_y))
    precision = correct / len(similar)
    recall = correct / len(clusters)
    return (precision, recall)

ratios = np.arange(0.01, 1.00,0.05)
p = []
r = []

for t in ratios:
    acc = accuracy(t)
    p.append(acc[0])
    r.append(acc[1])
    
    
#plt.xlabel('recall')
#plt.ylabel('precision')
#plt.plot(r, p,alpha=1)
#plt.show()

plt.plot(r,p, label='Ratio')
plt.title("Levenstein Ratio vs Distance")
plt.plot(r_dis,p_dis, label='Distance')
plt.legend(loc='upper left')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()

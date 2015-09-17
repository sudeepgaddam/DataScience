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

# Show that prod is the size of "resto" squared:
prod = prod[prod.id_x > prod.id_y]
prod['distance'] = prod.apply(lambda r: L.distance(r['name_x'], r['name_y']), axis=1)


def accuracy(max_distance):
    similar = prod[prod.distance < max_distance]
    correct = float(sum(similar.cluster_x == similar.cluster_y))
    precision = correct / len(similar)
    recall = correct / len(clusters)
    return (precision, recall)

thresholds = range(1, 11)
p = []
r = []

for t in thresholds:
    acc = accuracy(t)
    p.append(acc[0])
    r.append(acc[1])
area = [100*a*b for a,b in zip(p,r)]
plt.xlabel('recall')
plt.ylabel('precision')
plt.title("Scatter Plot for Levenstein Distance")
plt.scatter(r, p, s=area, alpha=1)
#legend(['precision', 'recall'], loc='upper left')
plt.show()

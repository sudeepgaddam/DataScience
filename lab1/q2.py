import Levenshtein as L
import pandas as pd
resto = pd.read_csv('restaurants.csv')
	#
	#
	#
	#print resto[:10]
clusters = pd.merge(resto, resto, on='cluster')
print len(clusters)
clusters = clusters[clusters.id_x < clusters.id_y]
print clusters[:10]

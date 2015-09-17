import Levenshtein as L
import pandas as pd
resto = pd.read_csv('restaurants.csv')
resto['dummy'] = 0
prod = pd.merge(resto, resto, on='dummy')

# Clean up
del prod['dummy']
del resto['dummy']

# Show that prod is the size of "resto" squared:
print len(prod), len(resto)**2, len(resto)
prod = prod[prod.id_x > prod.id_y]
print prod[:10]


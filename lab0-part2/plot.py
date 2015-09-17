from pylab import *
import pandas as pd
rand_df = pd.DataFrame({'a' : randn(100)})
rand_df.plot()
rand_df.hist()
show()

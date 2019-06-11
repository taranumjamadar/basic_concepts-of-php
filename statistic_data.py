import numpy as np
data = [1.0,4.5,2.3,-0.5,0.5,2.8]
np.mean(data)
np.median(data)
np.std(data)
np.var(data)

np.std(data,ddof=1)

md = np.arange(16)
md.shape = 4,4
md

np.mean(md)

np.std(md)

np.mean(md,axis=0)

np.mean(md,axis=1)
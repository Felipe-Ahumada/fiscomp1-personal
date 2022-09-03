import numpy as np
from integrales import midpoint_simple

f = lambda x:(x-1)*np.exp(x)

limites = np.linspace(0, 3, 1000)
integ = 0.0
for i in range(limites.size-1):
     integ = integ + midpoint_simple(f, limites[i], limites[i+1]                            
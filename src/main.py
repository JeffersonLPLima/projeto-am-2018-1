import numpy as np
import pandas as pd


base = np.genfromtxt('segmentation.data.txt',delimiter=',', dtype=np.str)


labels = base[1:,0]
data = base[1:,1:]


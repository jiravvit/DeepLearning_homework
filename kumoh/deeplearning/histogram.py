import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

my_data = pd.read_csv("data.csv")

print "-------histogram-------"
my_data.hist(bins=50, layout=(2,7), figsize=(10,3))
plt.show()


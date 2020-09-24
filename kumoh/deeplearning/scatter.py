import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from six.moves import urllib

my_data = pd.read_csv("data.csv")

print "------scatter------"
my_data.plot(kind="scatter", x='MEDV', y='ZN')
plt.show()

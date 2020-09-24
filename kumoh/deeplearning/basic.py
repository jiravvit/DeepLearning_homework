import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from six.moves import urllib

def download_data(url, dir_name, file_name):
        if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
        file_path = os.path.join(dir_name,file_name)
        urllib.request.urlretrieve(url, file_path)

dir_name = "./"
file_name = "data.csv"
download_data("https://www.openml.org/data/get_csv/52643/boston.arff", dir_name, file_name)


my_data = pd.read_csv("data.csv")

print "-------info-------"
my_data.info()

print "-------head-------"
print my_data.head()

print "-------tail-------"
print my_data.tail()

print "-------describe--------"
print my_data.describe()

print "-------histogram-------"
my_data.hist(bins=50, layout=(2,7), figsize=(10,3))
plt.show()

print "scatter"
my_data.plot(kind="scatter", x='MEDV', y='ZN')
plt.show()

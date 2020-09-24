import os
from six.moves import urllib

def download_data(url, dir_name, file_name):
	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)
	file_path = os.path.join(dir_name,file_name)
	urllib.request.urlretrieve(url, file_path)

dir_name = "./"
file_name = "data.csv"
download_data("https://www.openml.org/data/get_csv/52643/boston.arff", dir_name, file_name)

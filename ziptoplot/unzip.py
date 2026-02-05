# File : unzip.py 

def unzip(data, index):
	"""
	Opens .npz data files to desired index in the first array.  
	"""
	unzip_data = np.load(f'{data}')
	read_data = unzip_data["arr_0"]
	index_data = unzip_data[index]
	return index_data

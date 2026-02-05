# File : plot.py

def quickplot(index_data, frequency, amplitude, xlim, title, line_color):
	"""
	Plots a long, narrow graph of desired data.
	Frequency is in kilohertz, amplitude is in mV.
	X-axis is based on counts from 0-100.   
	"""
	#Plot Structure
	plt.figure()
	plt.plot(index_data, f'{linecolor}')
	plt.xlim(0, xlim)

	#Labels
	plt.title(title)
	plt.xlabel('Counts')
	plt.ylabel('Amplitude')
	#plt.show()
	return plt.show()

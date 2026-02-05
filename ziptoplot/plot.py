# File : plot.py

import numpy as np
import matplotlib.pyplot as plt

def quickplot(index_data, frequency, amplitude, xlim, title, line_color):
	"""
	Plots a long, narrow graph of desired data (index_data).
	Frequency is in kilohertz, amplitude is in ADC.
	X-axis is based on counts from 0-100.   
	"""
	#Plot Structure
	plt.figure()
	plt.plot(index_data, f'{line_color}')
	plt.xlim(0, xlim)

	#Labels
	plt.title(title)
	plt.xlabel('Counts')
	plt.ylabel('Amplitude (ADC)')
	#plt.show()
	return plt.show()

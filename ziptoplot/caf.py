# File : caf.py 

#Calculate Aliased Frequency

def calcaf(signal_frequency, sampling_rate_, nyquist_zone):
	"""
	Calculates the expected aliased frequency when given a signal frequency and the sampling rate. 

	Signal_frequency and sampling_rate must be given in Hz.
	nyquist_zone should be represented as an integer. 
	"""
	sampling_rate = 1000000 # Hz
	frequency = 600000 # Hz
	k = 1 # first nyquist zone
	f_alias =  (sampling_rate - k * frequency)
	return (f'Expected Aliased Frequency: {f_alias}')

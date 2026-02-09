import numpy as np
import matplotlib.pyplot as plt
#import ugradio
#from ugradio.SDR import sdr
from scipy.optimize import curve_fit



def read_data(file_name,array_pos): 
    file = np.load(f"{file_name}")["arr_0"][array_pos]
    return file



def freq_plots(ax, pos_x, frequency, title = "", subx=1, suby=4, figS1 = 140, figS2 = 30, pos_y = 0, varName="", background_col = "white", wave_col = "black", xlim0 = 0, xlim1 = 20, ylim0 = -100, ylim1 = 100, plineW = 20, labelFontSize = 90, titleFontSize = 105, gridW = 12, tickSize = 75, opacity = 0.3, xlabel = "", ylabel = ""):


    axs = ax[pos_x]

    #initial plot
    axs.plot(varName, color  = (wave_col), linewidth = plineW)

    #naming
    axs.set_xlabel(xlabel, fontsize = labelFontSize)
    axs.set_ylabel(ylabel, fontsize = labelFontSize)
    axs.set_title((title), fontsize = titleFontSize)
    #restrictions
    axs.set_xlim(xlim0, xlim1)
    axs.set_ylim(ylim0, ylim1)

    #aesthetic
    axs.tick_params(axis = "both", labelsize = tickSize)
    axs.grid(linewidth = gridW)
    axs.patch.set_facecolor(background_col)
    axs.patch.set_alpha(opacity)


def guass(x, mu, A, sigma, C):
    calculation = A * np.exp(-(-x-mu)**2 / (2*sigma**2)) + C




# #for installation
# [build-system]
# requires = ["setuptools >= 77.0.3"]
# build-backend = "setuptools.build_meta"

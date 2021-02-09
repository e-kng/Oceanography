# CORE GRANULOMETRY MAPPING
# DATA FROM MALVERN MASTERSIZER Hydro 2000G (from 0.06 to 900 μm)
# Fraunhofer diffraction method

######################################################################################################

path = 'C:/Users/Dwimo/Documents/05 DATA/00 GITHUB/Oceanography/Data/'
file = 'Data/core_grain_size.xlsx'

display_figure = True
save_figure = False
######################################################################################################

from matplotlib.colors import Normalize
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

raw_data = pd.read_excel(path+file, sheet_name=0, header=0, usecols='A,R:CC')

# Cleaning data
raw_data.rename({'Nom de l\'échantillon':'sample'}, axis=1, inplace=True)
raw_data.columns = raw_data.columns.str.replace(' µm', '')

# Set X, Y and Z values for colorbar
x = raw_data.columns[1:].values.astype('float')
y = raw_data['sample'].values
X, Y = np.meshgrid(x,y)

Z = raw_data.iloc[:,1:].values

# Figures
def figure_map():
    plt.figure(figsize=(3,10))
    plt.pcolormesh(X, Y, Z, cmap='jet', shading='flat')

    plt.colorbar(shrink=0.3, aspect=10)

    plt.gca().invert_yaxis()
    plt.ylabel('Depth (cm)')

    plt.xlabel('Grain size (µm) - log scale')
    plt.xscale('log', subsx=[0])
    plt.xlim(0.2)
    plt.xticks([2,10,63,250,800],labels=[2,10,63,250,800], rotation=45)

figure_map()

if save_figure:
    plt.savefig('figure_map.png',dpi=300)

if display_figure == False:
    plt.close()

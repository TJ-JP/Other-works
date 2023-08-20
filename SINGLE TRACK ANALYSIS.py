# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:24:28 2021

@author: Priya
from ggplot import *
ggplot(aes(x=x, y=y, color=z), data=dfpower400)  + geom_point()

def marker(z): 
    for i, row in dfpower400.iterrows():
        if row['Powder Feed rate (g/min)'] == 2.0:
             colour = '#8A2BE2'
        elif row['Powder Feed rate (g/min)'] == 3.0:
            colour = '#FFD39B'
        elif row['Powder Feed rate (g/min)'] == 4.0:
            colour = '#458B00'
        elif row['Powder Feed rate (g/min)'] == 5.0:
            colour = '#CD1076'
        return colour
"""

import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from openpyxl import load_workbook
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

path = 'C:\\Users\\Priya\\Downloads\\Result for analysis  For single track (Ti 64)..xlsx'
df = pd.read_excel(path)
df['Energydensity'] = df['Power (W)']/df['Scan speed (mm/min)']
df['Energydensity'] = df['Energydensity']*60
df['Energy density (J/mm)'] = df.Energydensity.round(2)

classes = ['5.0', '4.0', '3.0', '2.0', '7.5', '6', '1.5']

x = df['Energy density (J/mm)']
y = df['Width - um']
y1 = df['Height um']
y2 = df['Depth um']
y3 = df['Area - Upper - um*um']/100000
y4 = df['Area - Lower - um*um']/100000
y5 = df['Left corner upper angle']
y6 = df['Right corner upper angle']
y7 = df['left corner lower angle ']
y8 = df['right corner lower angle']
z= df['Powder Feed rate (g/min)']

plt.rcParams.update({'axes.labelsize':12})
scatter = plt.scatter(x, y2, c = z, label = z)
plt.xlabel('Energy density (J/mm)')
l =plt.legend(handles=scatter.legend_elements()[0], labels=classes, prop = {'size':10}, bbox_to_anchor= (1.21,1.0))
#, loc = 'upper left'
l.set_title('PFR (g/min)', prop = {'size':9})
plt.ylabel('Depth(μm)')
#plt.ylabel('Bead angle - Left (degree)')
plt.ylim(0,400)
plt.xlim(0,)
#plt.ylabel('Bead area * $\mathregular{10^{5}}$ ($\mathregular{μm^{2}}$)')
#$\mathregular{ms^{-2}}$
#plt.title('Power = 400 W')
plt.savefig('C:\\Users\\Priya\\Downloads\\Ed vs Depth.png', dpi = 600, bbox_inches = 'tight')

plt.show() 

"""
path = 'I:\IISc\Gowtham\gowtham_LOM\DED\ss316l\Cross_SEction\Etched\A\SS316 - CS.xlsx'
df = pd.read_excel(path)
df['Energydensity'] = df['Power (W)']/df['Scan speed (mm/min)']
df['Energy density (W*min/mm)'] = df.Energydensity.round(2)

dfpower400 = df.loc[df['Power (W)'] == 400]

dfpower500 = df.loc[df['Power (W)'] == 500]

dfpower600 = df.loc[df['Power (W)'] == 600]

dfpower800 = df.loc[df['Power (W)'] == 800]

dfpower1000 = df.loc[df['Power (W)'] == 1000]

classes = ['2.0', '3.0', '4.0', '5.0']

x = dfpower400['Scan speed (mm/min)']
y = dfpower400['Width - um']
y1 = dfpower400['Height um']
y2 = dfpower400['Depth um']
z= dfpower400['Powder Feed rate (g/min)']

plt.rcParams.update({'axes.labelsize':12})
scatter = plt.scatter(x, y2, c = z, label = z)
plt.xlabel('Scan speed (mm/min)')
l =plt.legend(handles=scatter.legend_elements()[0], labels=classes, prop = {'size':10})
l.set_title('Powder Feed rate (g/min)', prop = {'size':10})
plt.ylabel('Depth (μm)')

plt.title('Power = 400 W')
#plt.savefig('I:\IISc\Gowtham\gowtham_LOM\DED\ss316l\Cross_SEction\Etched\P400SCANVSDEPTH.tif')
plt.show() 
"""
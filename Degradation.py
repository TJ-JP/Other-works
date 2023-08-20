# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:28:33 2021

@author: Priya
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel(r'C:\Users\Priya\Downloads\Shared expenses.xlsx')
x = [6, 12, 18, 24, 36, 72]
for column in df.columns[::1]:
    y = ['meant6', 'meant12', 'meant18', 'meant24', 'meant48', 'meant72']
    for mean in y:
        mean = df[column].mean()
    yerror = ['stdt6', 'stdt12', 'stdt18', 'stdt24', 'stdt48', 'stdt72']
    for std in yerror:
        std = df[column].std()
        
plt.plot(x, y, color = 'r', linewidth = 3)
plt.title('Degradation of 15G0.1CNF gel')
plt.xlabel('time in hours')
plt.ylabel('Degradation ratio')
ax = plt.subplot()
ax.errorbar(x, y, yerr = yerror, fmt = 'o')
ax.set_ylim(bottom = 0)
ax.set_xlim(left = 0)
plt.show()


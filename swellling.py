# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:55:37 2021

@author: Priya
"""
import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Users\Priya\Downloads\Shared expenses.xlsx')
df.Swelling = (df.ww - df.dw)/df.dw *100
ax = 
idw-fdw/idw *100
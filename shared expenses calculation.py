# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:55:04 2021

@author: Priya
"""
import pandas as pd

df = pd.read_excel(r'C:\Users\Priya\Downloads\Shared expenses (2).xlsx')

t = df.Price.sum()
print(t)
Remya = 0
for i, row in df.iterrows():
   if(row.Paidby == 'R'):
       Remya = Remya + row.Price
print('Remya Share - ' + str(Remya))
print(Remya/2)
Jp = 0
for i, row in df.iterrows():
   if(row.Paidby == 'J'):
       Jp = Jp + row.Price
print('JP Share - ' + str(Jp))
print(Jp/2)
print((Remya/2) - (Jp/2))




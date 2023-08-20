# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:27:32 2021

@author: Priya
"""
import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2_contingency

df = pd.read_excel('ACS data 24 may.xlsx')

def ans(a, b, c, d):
 A = pd.DataFrame([[a, b], [c, d]], index = ['g', 'h'], columns = ['o', 'p'])
 p = chi2_contingency(A, correction = False)[1]
 print(p)
 oddsratio, pvalue = stats.fisher_exact(A)
 print(pvalue)
 
ans(0, 61, 1, 7)
"""
f = 0
for i, row in df.iterrows():
      f += 1
      a = df.ET.loc[f]
      a1 = df.ET.loc[f+1]
      b = df.TD.loc[f]
      b1 = df.TD.loc[f+1]
      c = df.SH.loc[f]
      c1 = df.SH.loc[f+1]
      d = df.OH.loc[f]
      d1 = df.OH.loc[f+1]
      A = pd.DataFrame([[a, a1], [d, d1]], index = ['g', 'h'], columns = ['o', 'p'])
      print(A)
      p = chi2_contingency(A, correction = False)[1]
      print(p)
      oddsratio, pvalue = stats.fisher_exact(A)
      print(pvalue)
      f += 3

   # ans(a, b, c, d)
   """ 
   
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2_contingency
import numpy as np

df = pd.read_excel('ACS data 24 may.xlsx')

print
def threecode(OCol, Ncol, a, b, c, v1, v2, v3, v4):
    conditions = [(df[OCol] <= v1), (df[OCol] >= v2),((df[OCol] > v3) & (df[OCol] < v4))]
    values = [a, b, c]
    df[Ncol] = np.select(conditions, values)
def twocode(OCol, Ncol, a, b, v1, v2):
    conditions = [(df[OCol] <= v1), (df[OCol] > v2)]
    values = [a, b]
    df[Ncol] = np.select(conditions, values)


#()
#Age code
threecode('Age', 'AgeC', 1, 3, 2, 40, 60, 40, 60)

#Sex code
conditions = [(df.Sex == 'M'), (df.Sex == 'F'), (df.Sex == 'm'), (df.Sex == 'f')]
values = [1, 2, 1, 2]
df['SEXC'] = np.select(conditions, values)




#Pulse rate code
threecode('PulseRate', 'PulseRateC', 1, 3, 2, 60, 101, 60, 101)

#SBP code
twocode('SBP', 'SBPC', 1, 2, 140, 140)

#DBP code
twocode('DBP', 'DBPC', 1, 2, 90, 90)
twocode('BMI', 'BMIC', 1, 2, 30, 30)
#KFT
#KFT_Urea
conditions = [(df.KFT_Urea > 40), ((df.KFT_Urea >= 15) & (df.KFT_Urea <= 40))]
values = [2, 1]
df['KFT_UreaC'] = np.select(conditions, values)



#KFT_Na
threecode('KFT_Na', 'KFT_NaC', 1, 3, 2, 135, 146, 135, 146)

#KFT_Creatinine
threecode('KFT_Creatinine', 'KFT_CreatinineC', 2, 3, 1, 0.56, 1.2, 0.56, 1.2)

#KFT_K
threecode('KFT_K', 'KFT_KC', 2, 3, 1, 3.4, 5.2, 3.4, 5.2)

#KFT_eGFR
conditions = [(df.e_GFR > 90), ((df.e_GFR >= 60) & (df.e_GFR <= 89)), ((df.e_GFR >= 30) & (df.e_GFR <= 59)), ((df.e_GFR >= 15) & (df.e_GFR <= 29)), (df.e_GFR < 15)]
values = [1, 2, 3, 4, 5]
df['e_GFRC'] = np.select(conditions, values)



#Lipid profile code
twocode('Cholesterol', 'CholesterolC', 1, 2, 200, 200)
twocode('Cholesterol_HDL', 'Cholesterol_HDLC', 2, 1, 40, 40)
twocode('Direct_LDL_Cholesterol', 'Direct_LDL_CholesterolC', 1, 2, 100, 100)
twocode('Triglycerides', 'TriglyceridesC', 1, 2, 150, 150)
twocode('CHOLHDL_RATIO', 'CHOLHDL_RATIOC', 1, 2, 4, 4)
twocode('LDLHDL_Ratio', 'LDLHDL_RatioC', 1, 2, 3.2, 3.2)
twocode('VLDLP', 'VLDLPC', 1, 2, 40, 40)


#Glucose code
twocode('Blood_Sugar_Random', 'Blood_Sugar_RandomC', 1, 2, 140, 140)

#BNP code
threecode('BNP', 'BNPC', 1, 3, 2, 99, 501, 99, 501)

#Hb profile code
threecode('Hb', 'HbC', 1, 3, 2, 11, 16, 11, 16)


#TLC/DLC profile code
conditions = [((df.TLC_DLC <= 10) & (df.TLC_DLC >= 4)), (df.TLC_DLC > 10)]
values = [1, 2]
df['TLC_DLCC'] = np.select(conditions, values)

"""
#CKMB code
twocode('CPK_MB', 'CPK_MBC', 1, 2, 3.5, 3.5)

"""
#Trop T/I profile code
twocode('Trop_TI', 'Trop_TIC', 1, 2, 15.6, 15.6)

#LVEF code
twocode('LVEF', 'LVEFC', 1, 2, 55, 55)

#Thyroid
#T3-1 code
threecode('T3___Lab_1', 'T3___Lab_1C', 1, 1, 2, 2.49, 5.81, 2.49, 5.81)

#T3-2 code
threecode('T3__Lab_2', 'T3__Lab_2C', 1, 1, 2, 1.70, 3.72, 1.70, 3.72)

df['T3___Lab_1'] = df.apply(lambda row: row['T3___Lab_1'] if row['T3___Lab_1'] !=0 else row['T3__Lab_2'], axis = 1)
#T4-1 code
threecode('T4__lab_1', 'T4__lab_1C', 1, 1, 2, 11.49, 23.01, 11.49, 23.01)

#T4-2 code
threecode('T4__lab_2', 'T4_lab_2C', 1, 1, 2, 0.69, 1.49, 0.69, 1.49)

df['T4__lab_1'] = df.apply(lambda row: row['T4__lab_1'] if row['T4__lab_1'] !=0 else row['T4__lab_2'], axis = 1)
#TSH-1 code
conditions = [((df.TSH___LAB_1 >= 0.2) & (df.TSH___LAB_1 <= 5.1)), (df.TSH___LAB_1 < 0.2), ((df.TSH___LAB_1 > 5.1) & (df.TSH___LAB_1 <= 10)), (df.TSH___LAB_1 > 10)]
values = [1, 2, 3, 4]
df['TSH___LAB_1C'] = np.select(conditions, values)

#print(df['TSH___LAB_1C'])

#TSH-2 code
conditions = [((df.TSH___LAB_2 >= 0.35) & (df.TSH___LAB_2 <= 4.9)), (df.TSH___LAB_2 < 0.35), ((df.TSH___LAB_2 > 4.9) & (df.TSH___LAB_2 <= 10)), (df.TSH___LAB_2 > 10)]
values = [1, 2, 3, 4]
df['TSH___LAB_2C'] = np.select(conditions, values)
#print(df.TSH___LAB_2C)

df['TSH___LAB_1C'] = df.apply(lambda row: row['TSH___LAB_1C'] if row['TSH___LAB_1C'] !=0 else row['TSH___LAB_2C'], axis = 1)
#pd.set_option('display.max_rows', len(df))
#print(df['TSH___LAB_1C'])

count = 0
for i, row in df.iterrows():
   if(row.AgeC == 1):
      count += 1
#print(count)

def f3(factor, acode):
 def f2(Column, code):
#Counting and basic
  def filter(Column, tcode, acode, code):
    count = 0
    for i, row in df.iterrows():
      if(((row.TSH___LAB_1C == tcode) and (row[factor] == acode) and (row[Column] == code))):
         count += 1
    print(count)

  filter(Column, 1, acode, code)
  filter(Column, 2, acode, code)
  filter(Column, 3, acode, code)
  filter(Column, 4, acode, code)
  
 f2('HEART_FAILURE _30 days', 1)
 f2('HEART_FAILURE _30 days', 0)
 f2('RECURRENT_MI_ 30 days', 1)
 f2('RECURRENT_MI_ 30 days', 0)
 f2('REHOSPITALISATION_FOR_CARDIAC_CAUSE_ 30 days', 1)
 f2('REHOSPITALISATION_FOR_CARDIAC_CAUSE_ 30 days', 0)
 f2('SIGNIFICANT_ATRIAL_AND_VENTRICULAR_ARRHYTHMIAS_ 30 days', 1)
 f2('SIGNIFICANT_ATRIAL_AND_VENTRICULAR_ARRHYTHMIAS_ 30 days', 0)
 f2('CORONARY_REVASCULARISATION_ 30 days', 1)
 f2('CORONARY_REVASCULARISATION_ 30 days', 0)
 f2('CV_DEATH_ 30 days', 1)
 f2('CV_DEATH_ 30 days', 0)
 f2('HEART_FAILURE_ 1 year', 1)
 f2('HEART_FAILURE_ 1 year', 0)
 f2('RECURRENT_MI_ 1 year', 1)
 f2('RECURRENT_MI_ 1 year', 0)
 f2('REHOSPITALISATION_FOR_CARDIAC_CAUSE_ 1 year', 1)
 f2('REHOSPITALISATION_FOR_CARDIAC_CAUSE_ 1 year', 0)
 f2('SIGNIFICANT_ATRIAL_AND_VENTRICULAR_ARRHYTHMIAS_ 1 year', 1)
 f2('SIGNIFICANT_ATRIAL_AND_VENTRICULAR_ARRHYTHMIAS_ 1 year', 0)
 f2('CORONARY_REVASCULARISATION_ 1 year', 1)
 f2('CORONARY_REVASCULARISATION_ 1 year', 0)
 f2('CV_DEATH_ 1 year', 1)
 f2('CV_DEATH_ 1 year', 0)
 
f3('AgeC', 1)




def basic(tcode, x, y):
  for i, row in df.iterrows():
      if(row.TSH___LAB_1C == tcode): 
         df[y]= df[x].where(df['TSH___LAB_1C'] == tcode)
         mean = df[y].mean()
         std = df[y].std()
         max = df[y].max()
         min = df[y].min()
         var = df[y].var(ddof = 1)
         N = (df[y].fillna(0).astype(bool).sum(axis = 0))
  print ('mean of', x, ': ', round(mean, 2))
  print ('std of', x, ': ', round(std, 2))
  print ('max of', x, ': ', max)
  print ('min of', x, ': ', min) 
  print ('var of', x, ': ', var)
  print ('N of', x, ': ', N)
def basic1(tcode, x, y):
  for i, row in df.iterrows():
      if(row.TSH___LAB_1C == tcode): 
         df[y]= df[x].where(df['TSH___LAB_1C'] != tcode)
         mean = df[y].mean()
         std = df[y].std()
         max = df[y].max()
         min = df[y].min()
         var = df[y].var(ddof = 1)
         N = (df[y].fillna(0).astype(bool).sum(axis = 0))
  print ('mean of', x, ': ', round(mean, 2))
  print ('std of', x, ': ', round(std, 2))
  print ('max of', x, ': ', max)
  print ('min of', x, ': ', min) 
  print ('var of', x, ': ', var)
  print ('N of', x, ': ', N)
#basic(1, 'T4__lab_1', 'ab')
#basic1(1, 'T4__lab_1', 'ba')
#print(df.ab)
#print(df.ba)





A = pd.DataFrame([[5,60], [0,8]], index = ['g', 'h'], columns = ['o', 'p'])
p = chi2_contingency(A)[1]
print(p)
oddsratio, pvalue = stats.fisher_exact(A)
print(pvalue)


#res = stats.ttest_ind(df.ab, df.ba, equal_var = False, nan_policy = 'omit')
#print(res)

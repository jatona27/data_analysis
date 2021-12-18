#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:44:57 2021

@author: jaimetorresnatividad
"""

import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 
from scipy.stats.stats import pearsonr

# Change working directory
os.chdir('/Users/jaimetorresnatividad/CursoFundamentosPython/clase4/tarea4')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
studentdata = pd.read_csv ('tarea4data.csv', sep=',', decimal='.')
studentdata.shape
studentdata.head()
#QC OK

#VARIABLE MATH_SCORE:
#Generamos el histograma:
x = studentdata['math_score']
x.min()
x.max()
n = x.count()
media = x.mean()
media

plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 100, step=10))
plt.title('Figure 1. Math Scores')

plt.ylabel('Frecuency')
plt.xlabel('Math Score')
props = dict(boxstyle='round',facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (8,230, textstr , bbox=props)

#Recuadro que muestre la cantidad de datos n:
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (8,230, textstr , bbox=props)

#Línea de la media representada en rojo:
plt.axvline(x=studentdata.math_score.mean(),linewidth=1, linestyle= 'dashed', color="red")
props = dict(boxstyle='round', facecolor='white', lw=0.5)

#Línea de las desviaciones estándar (cuartiles) representada en verde:
#Calculamos la desviación:
media_menosdesv = studentdata.math_score.mean()-studentdata.math_score.std()   
media_masdesv = studentdata.math_score.mean()+studentdata.math_score.std() 

plt.axvline(x=media_menosdesv,linewidth=1, linestyle= '--', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)

plt.axvline(x=media_masdesv,linewidth=1, linestyle= '--', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
#std para la desviación estándar

plt.savefig("hist_math_score_t4.svg")
plt.savefig("hist_math_score_t4.png")

#VARIABLE READING_SCORE:
#Generamos el histograma:
x = studentdata['reading_score']
x.min()
x.max()
n = x.count()
media = x.mean()

plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 100, step=10))
plt.title('Figure 2. Reading Scores')

plt.ylabel('Frecuency')
plt.xlabel('Reading Score')
props = dict(boxstyle='round',facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (8,230, textstr , bbox=props)

#Recuadro que muestre la cantidad de datos n:
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (8,230, textstr , bbox=props)

#Línea de la media representada en rojo:
plt.axvline(x=studentdata.reading_score.mean(),linewidth=1, linestyle= 'dashed', color="red")
props = dict(boxstyle='round', facecolor='white', lw=0.5)

#Línea de las desviaciones estándar (cuartiles) representada en verde:
#Calculamos la desviación:
media_menosdesv = studentdata.reading_score.mean()-studentdata.reading_score.std()   
media_masdesv = studentdata.reading_score.mean()+studentdata.reading_score.std() 

plt.axvline(x=media_menosdesv,linewidth=1, linestyle= '--', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)

plt.axvline(x=media_masdesv,linewidth=1, linestyle= '--', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
#std para la desviación estándar

plt.savefig("hist_reading_score_t4.svg")
plt.savefig("hist_reading_score_t4.png")


#Generamos un scatter plot:
med_math = studentdata['math_score'].mean()
sd_math = studentdata['math_score'].std()
   
textstr = 'Mean math = '+ str(round(med_math, 0)) +'\nS.D.= '+ str(round(sd_math,0)) +' \nn = ' + str(n)
plt.text (70,20, textstr)

med_reading = studentdata['reading_score'].mean()
sd_reading = studentdata['reading_score'].std()
textstr = 'Mean reading = '+ str(round(med_reading, 0)) +'\nS.D.= '+ str(round(sd_reading,0)) +' \nn = ' + str(n)
plt.text (7,80, textstr)

x = studentdata['math_score']
y = studentdata['reading_score']
plt.scatter(x, y, alpha= 0.5)
plt.title('Figure 3. Relación notas matemáticas y lectura')
plt.xlabel('Math Score')
plt.ylabel('Reading Score');
plt.savefig("relacion_notas4.svg")
plt.savefig("relacion_notas4.png")

#Utilizamos el coeficiente de Pearson para ver si realmente hay una relación lineal entre las dos variables:
from scipy.stats.stats import pearsonr
res = pearsonr(x, y)
print (res)   
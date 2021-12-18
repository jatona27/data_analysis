#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:58:43 2021

@author: jaimetorresnatividad
"""

import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


# Change working directory
os.chdir('/Users/jaimetorresnatividad/CursoFundamentosPython/clase3/tarea3')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
t3data = pd.read_csv ("tarea3data.csv", sep=',', decimal='.')
t3data.shape
t3data.head()

#Para la variable 1: math_score_str
res = t3data.math_score.describe()
n = res[0]
m = res[1]
sd = res[2]

print(m)
print(sd)

#Pasamos math_score a string:
t3data.loc[(t3data['math_score']<(m-sd)),"math_score_str"]= "Notas bajas"
t3data.loc[((t3data['math_score']>(m-sd))&(t3data['math_score']<(m+sd))),"math_score_str"]="Notas medias"
t3data.loc[ (t3data['math_score']>(m+sd)),"math_score_str"]="Notas altas"

#Pasamos math_score de str a ordinal:
my_categories=["Notas bajas", "Notas medias", "Notas altas"]
my_math_scores_type = CategoricalDtype(categories=my_categories, ordered=True)
t3data["math_score_cat"] = t3data.math_score_str.astype(my_math_scores_type)
t3data.info()

#Generamos el gráfico de porcentajes:
mytable = pd.crosstab(t3data.math_score_cat, columns="count", normalize='columns')*100
mytable
plt.bar(mytable.index, mytable['count'])
plt.savefig("grafico_porcent_notas.png")

#Para la variable 2: test_preparation_course --> Generamos el grafico de porcentajes:
mytable = pd.crosstab(t3data.test_preparation_course, columns="count", normalize='columns')*100
mytable
plt.bar(mytable.index, mytable['count'])
plt.savefig("grafico_porcent_test.png")

#Mezclamos las dos variables la dependiente y la independiente:
pd.crosstab(t3data.math_score_cat, t3data.test_preparation_course, normalize='columns', margins=True)*100
my_ct = pd.crosstab(t3data.math_score_cat, t3data.test_preparation_course, normalize='columns', margins=True)*100
round (my_ct,1) #Redondear función
my_ct.round(1) #Redondear, objeto
my_ct = round (my_ct,1)

#Test estadístico
ct = pd.crosstab(t3data.math_score_cat, t3data.test_preparation_course) #Tabla de contingencia
valor_chi2 = stats.chi2_contingency(ct)
valor_chi2
#Transpose and plot
my_ct2 = my_ct.transpose()

my_ct2.plot(kind='bar', edgecolor = 'black', colormap = 'Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 24,73''\n''n: 1000' '\n' 'Pval.: 4,26e-06', bbox=props)
plt.xlabel('Math Score')
plt.legend(['Notas Bajas','Notas Medias','Notas Altas'])
plt.ylim(0,100)
plt.title('Figure 3. Percentage of notas de matemáticas por nivel.' '\n')
plt.xticks(rotation='horizontal')
plt.savefig("grafico_ultimo_comparativa.png")

my_ct
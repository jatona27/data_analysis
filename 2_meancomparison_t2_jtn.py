#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:37:30 2021

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
os.chdir('/Users/jaimetorresnatividad/CursoFundamentosPython/clase3/tarea2')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
t2data = pd.read_csv ("tarea2data.csv", sep=',', decimal='.')
t2data.shape
t2data.head()
#QC OK

t2data.groupby('test_preparation_course').math_score.mean()

#filtramos los datos por si han hecho el test o no, para que nos muestre la nota de cada uno dependiendo del sexo elegido:
completed_ms = t2data.loc[t2data.test_preparation_course == 'completed', "math_score"]
none_ms = t2data.loc[t2data.test_preparation_course == 'none', "math_score"]

#Ejecutamos el t-test:
stats.ttest_ind(completed_ms, none_ms, equal_var = False)

t2data.math_score.min()
t2data.math_score.max()
t2data.math_score.mean()

#CI meanplot
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="test_preparation_course", y="math_score", data=t2data,ci=95, join=0)

plt.yticks(np.arange(t2data.math_score.min(), t2data.math_score.max(), step=5))
plt.ylim(50,80)
plt.axhline(y=t2data.math_score.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.85,73,'Mean: 66.09''\n''n:1000' '\n' 't:5.787' '\n' 'Pval.:1.043e-08', bbox=props)
plt.xlabel('Test preparation course')
plt.title('Figure 1. Average math score by preparation test done or not.''\n')

plt.savefig("grafico_medias.png")
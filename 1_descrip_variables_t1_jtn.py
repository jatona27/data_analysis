#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:44:24 2021

@author: jaimetorresnatividad
"""

import os
import pandas as pd #gestionar data frames, matrices de datos, excels, etc. no podríamos hacer análisis de datos sin pandas
import numpy as np #gestionar vectores, matrices, operaciones matemáticas
import matplotlib.pyplot as plt #librería del primer nivel para gráficos estadísticos
from sklearn import datasets, linear_model
os.chdir('/Users/jaimetorresnatividad/CursoFundamentosPython/tarea1')
os.getcwd() #saber ubicación del directorio que estamos y del proyecto

studentdata = pd.read_csv ('tarea1data.csv', sep=',', decimal='.') #leer el csv

print(studentdata.shape) #nos devuelve el número de filas y el de columnas (filas, columnas)
print(studentdata.head()) #presenta los 5 primeros
print(studentdata.tail()) #presenta los 5 últimos
#QC OK

import matplotlib.pyplot as plt #cargamos la librería de gráficos

studentdata.columns #muestra el nombre de las columnas

#Variables cuantitativas:
    # - Nota matemáticas
    # - Nota Lectura
    
#Variables nominales:
    # - Raza
    # - Nivel de educación de los padres
studentdata.columns
#Raza:
etniadata = studentdata.groupby(['race/ethnicity']).size()
etniadata.head()
n = etniadata.sum()
etniadata2 = (etniadata/n)*100
etniadata2.head()
etniadata3 = round(etniadata2,0)
print(etniadata3)
bar_list = ['Asiáticos', 'Africanos', 'Europeos', 'Americanos', 'Australianos']
plt.bar(bar_list, etniadata3, edgecolor='black') #bins para añadir columnas, ya que por defecto nos saca solo 10 barras
#plt.xticks(np.arange(0, 1000, step=1)) #definimos el eje X con xticks; definimos el eje Y con yticks
#step son los saltos
plt.title('Figure 1. Porcentaje de alumnos por etnia')
plt.ylabel('Porcentaje')
plt.savefig("barras_etnia.svg")


#Nivel de educación de los padres:
niveleddata = studentdata.groupby(['parental level of education']).size()
niveleddata.head()
n = niveleddata.sum()
niveleddata2 = (niveleddata/n)*100
niveleddata2.head()
niveleddata3 = round(niveleddata2,0)
print(niveleddata3)
bar_list = ["associate", "bachelor", "HS", "master", "college", "ot. HS"]
plt.bar(bar_list, niveleddata3, edgecolor='black') #bins para añadir columnas, ya que por defecto nos saca solo 10 barras
#plt.xticks(np.arange(0, 1000, step=1)) #definimos el eje X con xticks; definimos el eje Y con yticks
#step son los saltos
plt.title('Figure 2. % alumnos por nivel educativo padres')
plt.ylabel('Porcentaje')
plt.savefig("barras_niveleduc.svg")


#Notas reading con maths
#calculo de medias y desviación estándar:
med_math = studentdata['math score'].mean()
n = etniadata.sum()
sd_math = studentdata['math score'].std()
sd_math
textstr = 'Mean math = '+ str(round(med_math, 0)) +'\nS.D.= '+ str(round(sd_math,0)) +' \nn = ' + str(n)
plt.text (70,20, textstr)
med_read = studentdata['reading score'].mean()
med_read
sd_read = studentdata['reading score'].std()
sd_read
textstr = 'Mean reading = '+ str(round(med_read, 0)) +'\nS.D.= '+ str(round(sd_read,0)) +' \nn = ' + str(n)
plt.text (7,80, textstr)
x = studentdata['math score']
y = studentdata['reading score']
plt.scatter(x, y, alpha= 0.5)
plt.title('Figure 3. Relación notas matemáticas y reading')
plt.xlabel('Math Score')
plt.ylabel('Reading Score');
plt.savefig("relacion_notas.svg")


textstr = 'Mean math = '+ str(round(med_math, 0)) +'\nS.D.= '+ str(round(sd_math,0)) +' \nn = ' + str(n)
plt.text (70,20, textstr)
med_write = studentdata['writing score'].mean()
med_write
sd_write = studentdata['writing score'].std()
sd_write
textstr = 'Mean writing = '+ str(round(med_write, 0)) +'\nS.D.= '+ str(round(sd_write,0)) +' \nn = ' + str(n)
plt.text (7,80, textstr)
x = studentdata['math score']
y = studentdata['writing score']
plt.scatter(x, y, alpha= 0.5)
plt.title('Figure 4. Relación notas matemáticas y writing')
plt.xlabel('Math Score')
plt.ylabel('writing Score');
plt.savefig("relacion_notas2.svg")

#cálculos estadísticos
mode_math = studentdata['math score'].mode()
mode_math
quantile_math25, quantile_math50, quantile_math75 = studentdata['math score'].quantile([0.25,0.5,0.75])
quantile_math25, quantile_math50, quantile_math75

mode_read = studentdata['reading score'].mode()
mode_read
quantile_read25, quantile_read50, quantile_read75 = studentdata['reading score'].quantile([0.25,0.5,0.75])
quantile_read25, quantile_read50, quantile_read75

mode_write = studentdata['writing score'].mode()
mode_write
quantile_write25, quantile_write50, quantile_write75 = studentdata['writing score'].quantile([0.25,0.5,0.75])
quantile_write25, quantile_write50, quantile_write75
'''
mintempo = musicdata['tempo'].min()
mintempo #57,967
maxtempo = musicdata['tempo'].max()
maxtempo #220,29
'''
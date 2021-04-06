# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:17:21 2021

@author: Desktop
"""

#mediante librerias

import pandas as pd
import math
import numpy as np
from scipy import stats
from statistics import mode
datos=pd.read_csv("GlobalLandTemperaturesByState.csv")
datos1=datos['AverageTemperature']
datos2=datos['AverageTemperatureUncertainty']
datos0=datos['dt']
datos3=datos['State']
datos4=datos['Country']
datos33=pd.get_dummies(datos3,columns=['State'])
datos44=pd.get_dummies(datos3,columns=['Country'])
datos00=pd.get_dummies(datos3,columns=['dt'])
#print(datos33)
#funcion borrar vacios
def borrar(dato):
    sinvacios=[]
    for string in dato:
        if(string != 0.0):
            sinvacios.append(string)
    return sinvacios
datos11=borrar(datos1)
datos22=borrar(datos2)
#obtener la moda sin librerias
def modas(dato):
    diccionario_conteo={}
    for numero in dato:
        clave=str(numero)
        if not clave in diccionario_conteo :
        #lo agregamos
            diccionario_conteo[clave]=1
        #si existe
        else:
            diccionario_conteo[clave]+=1        
    frecuencia_mayor=0
    numero_mas_repetidos=dato[0]
    #imprimimos el diccionario solo para depurar
    #print(diccionario_conteo)

    for numero in diccionario_conteo:
        if diccionario_conteo[numero]>frecuencia_mayor:
            numero_mas_repetidos=numero
            frecuencia_mayor=diccionario_conteo[numero]
        #finalmento imprimimos el mas repetido, con su conteo
    conteo=diccionario_conteo[str(numero_mas_repetidos)]
    print(
      f"el numero o nominal que mas se repite es {numero_mas_repetidos} (encontrado {frecuencia_mayor} ocasiones)"
     )  
#obtener la media sin librerias
def media(dato):
    numero=sum(dato)/len(dato)
    return numero
#obtener la desviacion estandar sin librerias
def desviacion(dato,media):
    sigma=0.0
    for elemento in dato:
        sigma+=(elemento-media)**2
    desvi=math.sqrt(sigma/(len(dato)-1))
    return desvi
    
print("*****************A)SIN LIBRERIAS********************************")
print("FECHA: ")
modas(datos0)
print("*************************************************")
print("TEMPERATURA MEDIA")
media1=media(datos11)
print("MEDIA DE TM ",media1)
modas(datos11)
print("DESVI. EST DE TM ",desviacion(datos11, media1))
print("*************************************************")
print("INCERTIDUMBRE DE LA TEMPRATURA MEDIA")
media2=media(datos22)
print("MEDIA DE ITM ", media2)
modas(datos22)
print("DESVI. EST DE ITM ",desviacion(datos22, media2))
print("*************************************************")
print("ESTADO")
modas(datos3)
print("*************************************************")
print("PAIS")
modas(datos4)

print("*************************************************")
print("******************B)CON LIBRERIAS*******************************")
print("FECHA: ")
print("MODA: ",mode(datos0))
#print("MEDIA ", np.mean(datos00))
#print("DESV. ESTAND: ",stats.mode(datos00))
print("*************************************************")
print("TEMPERATURA MEDIA")
print("Media de la columna de Temperatura Media: ",np.mean(datos11))
print("Moda de la  columna de Temperatura Media: ",stats.mode(datos11))
print("Desviacion Estandar de la columna de Temperatura Media: ",np.std(datos11))
print("*************************************************")
print("INCERTIDUMBRE DE LA TEMPRATURA MEDIA")
print("Media de la columna de la Incertidumbre de la Temperatura Media : ",np.mean(datos22))
print("Moda de la  columna de la Incertidumbre de la Temperatura Media: ",stats.mode(datos22))
print("Desviacion Estandar de la columna de la Incertidumbre de la Temperatura Media: ",np.std(datos22))
print("*************************************************")
print("ESTADO")
print("MODA: ",mode(datos3))
#print("MEDIA ", np.mean(datos33))
#print("DESV. ESTAND: ",stats.mode(datos33))
print("*************************************************")
print("PAIS")
print("MODA: ",mode(datos4))
#print("MEDIA ", np.mean(datos44))
#print("DESV. ESTAND: ",stats.mode(datos44))
#matplotlib-C) GRAFICAR
import matplotlib.pyplot as plt
from pandas import DataFrame
#segunda columna
df=DataFrame(datos,columns=['dt','AverageTemperature'])
df.plot(x='dt',y='AverageTemperature', kind='hist')
#tercera columna
df1=DataFrame(datos,columns=['dt','AverageTemperatureUncertainty'])
df1.plot(x='dt',y='AverageTemperatureUncertainty', kind='hist')
plt.show()
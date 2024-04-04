import numpy as np
import pandas as pd

from matplotlib import pyplot as plt


def imprimir_dataframe(df):
    print(df.columns)
    print(df.head(n=40))


def imprimir_ultimas_filas(df):
    print(df.tail(n=40))


def imprimir_separacion():
    print("______________________")


def get_porcentaje_virales(df):
    cantidad_filas = df.shape[0]
    virales = (df['isViral'] == 'Yes').sum()

    return virales * 100 / cantidad_filas * 100


df = pd.read_csv('files\TwitterDatashetCleanC.csv')

imprimir_dataframe(df)

# diagrama de pastel tweets virales
labels = 'Yes', 'No'

sizes = df['isViral']

plt.figure(figsize=(10, 5))

plt.title("Tweets virales")

plt.pie(sizes.value_counts(), labels=labels, autopct='%1.1f%%')

plt.legend()

plt.show()

df_virales = df[df['isViral'] == 'Yes']

imprimir_separacion()

imprimir_dataframe(df_virales)

'''
REPRESENTACIONES GRÁFICAS
_____________________________________
'''

# diagrama de pastel de los tweets virales


labels = 'Yes', 'No'
sizes = df_virales['Weekend'].value_counts()

plt.figure(figsize=(10, 5))

plt.title("Tweets virales publicados el fin de semana")

plt.pie(df_virales['Weekend'].value_counts(), labels=labels, autopct='%1.1f%%')

plt.legend()

plt.show()

# diagrama de barras

# realizo un diagrama de barras con distintas metricas
# __________________________________________________________________-

dias_semana = df_virales['Weekday']

reach = df_virales['Reach']

retweets = df_virales['RetweetCount']

klout = df_virales['Klout']

# diagramas de barra con respecto al reach

plt.bar(dias_semana, reach)

plt.xlabel('Dias_semana')

plt.ylabel('Reach')

plt.title('Diagrama de Barras Reach - dias publicacion')

# Mostrar el gráfico
plt.show()

# diagrama de barra con respecto a los retweets

plt.bar(dias_semana, retweets)

plt.xlabel('Dias_semana')

plt.ylabel('Retweets')

plt.title('Diagrama de barras rt - dias')

plt.show()

# diagrama de barras con respecto a la puntuación klout

plt.bar(dias_semana, klout)

plt.xlabel('Dias_semana')

plt.ylabel('Klout')

plt.title('Diagrama de barras klout - dias')

plt.show()

# grafico de lineas

'''
df['Reach'].plot()

plt.show()

#diagrama de dispersion
df['Reach'].scatter()

plt.show()
'''

import numpy as np
import pandas as pd


df = pd.read_csv('files\TweetsEngagementMetrics.csv', low_memory=False)


print("COLUMNAS (con todas las variables)")

print(df.columns)

print("_____________________________")


print("COLUMNAS (tras la seleccion de variables relevantes)")
#me quedo con las variables que considero relevantes
df_cleanded = df[['Weekday', 'Hour', 'IsReshare', 'Reach', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'text']]

print(df_cleanded.columns)

print(df_cleanded.head(n=20))

#dado que a simple vista se ve que la columna de los likes tiene todos 0, realizo esta comprobacion
likes_cero = (df_cleanded['Likes'] == 0).all()

if likes_cero:
    print("Todos los valores de la columna <<Likes>> son 0")
else:
    num_valores_no_cero = (df_cleanded['Likes'] != 0).sum()
    print("Cantidad de valores en la columna <<Likes>> distinta de 0: ",num_valores_no_cero)
    

#calculo el porcentaje de valores faltantes
num_valores_totales = df_cleanded.size

# Calcular el número total de valores no nulos en el DataFrame
num_valores_no_nulos = df_cleanded.count().sum()

# Calcular el número total de valores faltantes en el DataFrame
num_valores_faltantes = num_valores_totales - num_valores_no_nulos

# Calcular el porcentaje de valores faltantes
porcentaje_valores_faltantes = (num_valores_faltantes / num_valores_totales) * 100


print("Porcentaje de valores faltantes en el DataFrame:", porcentaje_valores_faltantes * 100,"%")




df_cleanded.to_csv('files\TwitterDatashetClean.csv', index=False)




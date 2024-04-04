import numpy as np
import pandas as pd

df = pd.read_csv('files\TwitterDatashetCleanB.csv')

df_order_klout = df.sort_values(by="Klout", ascending=True)

df_order_reach = df.sort_values(by="Reach", ascending=True)

df_order_retweet = df.sort_values(by="RetweetCount", ascending=True)


def imprimir_dataframe(df):
    print(df.columns)
    print(df.head(n=20))


def get_minimo(df, nombre_columna):
    return df[nombre_columna].min()


def get_maximo(df, nombre_columna):
    return df[nombre_columna].max()


def get_promedio(df, nombre_columna):
    return df[nombre_columna].mean()


def get_mediana(df, nombre_columna):
    return df[nombre_columna].median()


def imprimir_separacion():
    print("______________________")


def viral_reach(reach, rt, klout, reshare):
    if reach >= 300 and rt >= 100 and klout >= 40 and reshare:
        return 'Yes'
    else:
        return 'No'


print(df.describe())

imprimir_separacion()

imprimir_dataframe(df)

imprimir_separacion()

# rangos reach
reach_minimo = get_minimo(df, 'Reach')

reach_maximo = get_maximo(df, 'Reach')

# tanto los retweets, como los likes y la puntuación Klout, tienen como valor minimo el 0, por lo tanto, han de sacarse los maximos
max_retweet = get_maximo(df, 'RetweetCount')

max_likes = get_maximo(df, 'Likes')

max_klout = get_maximo(df, 'Klout')

print('Reach minimo: ', reach_minimo)

print('Reach maximo: ', reach_maximo)

print('Max_retweet: ', max_retweet)

print('Likes maximo: ', max_likes)

print('Klout maximo: ', max_klout)

# a continiacion, determino el promedio y las medianas del Reach, RetweetCount y Klout
# _______________________________________________________________________________________

# Reach

promedio_reach = get_promedio(df_order_reach, 'Reach')

mediana_reach = get_mediana(df_order_reach, 'Reach')

# Retweet

promedio_retweet = get_promedio(df_order_retweet, 'RetweetCount')

mediana_retweet = get_mediana(df_order_retweet, 'RetweetCount')

# Klout

promedio_klout = get_promedio(df_order_klout, 'Klout')

mediana_klout = get_mediana(df_order_klout, 'Klout')

imprimir_separacion()

print("Reach")

imprimir_separacion()

print("Promedio:", promedio_reach)

print("Mediana:", mediana_reach)

imprimir_separacion()

print("Retweet")

print("Promedio:", promedio_retweet)

print("Mediana:", mediana_retweet)

imprimir_separacion()

print("Klout")

print("Promedio:", promedio_klout)

print("Mediana:", mediana_klout)

imprimir_separacion()

# con unas premisas que he establecido, defino si un tweet es viral o no

df['isViral'] = df.apply(lambda row: viral_reach(row['Reach'], row['RetweetCount'], row['Klout'], row['IsReshare']),
                         axis=1)

# una vez definido los umbrales, construyo la variable objetivo, que es si va a ser viral o no


imprimir_separacion()

imprimir_dataframe(df)

df.to_csv('files\TwitterDatashetCleanC.csv', index=False)

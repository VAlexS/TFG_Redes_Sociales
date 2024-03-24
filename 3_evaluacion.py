import numpy as np
import pandas as pd


df = pd.read_csv('files\TwitterDatashetCleanB.csv')

def imprimir_dataframe(df):
    print(df.columns)
    print(df.head(n=20))
    

    

def get_minimo(df, nombre_columna):
    return df[nombre_columna].min()


def get_maximo(df, nombre_columna):
    return df[nombre_columna].max()


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

#rangos reach
reach_minimo = get_minimo(df, 'Reach')

reach_maximo = get_maximo(df, 'Reach')

#tanto los retweets, como los likes y la puntuación Klout, tienen como valor minimo el 0, por lo tanto, han de sacarse los maximos
max_retweet = get_maximo(df, 'RetweetCount')

max_likes = get_maximo(df, 'Likes')

max_klout = get_maximo(df, 'Klout')

print('Reach minimo: ',reach_minimo)

print('Reach maximo: ',reach_maximo)

print('Max_retweet: ',max_retweet)

print('Likes maximo: ',max_likes)

print('Klout maximo: ',max_klout)


#con unas premisas que he establecido, defino si un tweet es viral o no

df['isViral'] = df.apply(lambda row: viral_reach(row['Reach'], row['RetweetCount'], row['Klout'], row['IsReshare']), axis=1)


# una vez definido los umbrales, construyo la variable objetivo, que es si va a ser viral o no


imprimir_separacion()

imprimir_dataframe(df)


#df.to_csv('files\TwitterDatashetCleanC.csv', index=False)
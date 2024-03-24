import numpy as np
import pandas as pd

def determinar_dia(weekday):
    if weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        return 'No'
    else:
        return 'Yes'
    
    
def imprimir_dataframe(df):
    print(df.columns)
    print(df.head(n=20))
    
def print_descripcion(df):
    print(df.describe())
    




df = pd.read_csv('files\TwitterDatashetClean.csv', low_memory=False)


#la columna weekend toma 2 valores posibles: 0 si es entre semana y 1 si es fin de semana
df['Weekend'] = df['Weekday'].apply(determinar_dia) 


print("_________________________________________________________")

#en función de las franjas horarias, defino el valor correspondiente al momento del dia

franjas_horarias = [0, 3, 7, 13, 22, 24]

momentos_dia = ['Noche', 'Madrugada', 'Mañana', 'Tarde', 'Noche']

df['FranjaHoraria'] = pd.cut(df['Hour'], bins=franjas_horarias, labels=momentos_dia, right=False, ordered=False)


imprimir_dataframe(df)




df.to_csv('files\TwitterDatashetCleanB.csv', index=False)






umbral_retweets = 100

umbral_klout = 50
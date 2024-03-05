import numpy as np
import pandas as pd

def determinar_dia(weekday):
    if weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        return 0
    else:
        return 1


df = pd.read_csv('files\TwitterDatashetClean.csv', low_memory=False)

'''
print(df.columns)

print(df.head(n=10))
'''

#la columna weekend toma 2 valores posibles: 0 si es entre semana y 1 si es fin de semana
df['Weekend'] = df['Weekday'].apply(determinar_dia) 

print(df.columns)

print(df.head(n=70))






umbral_retweets = 100

umbral_klout = 50
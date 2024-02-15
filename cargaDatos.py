import numpy as np
import pandas as pd


df = pd.read_csv('files\Twitterdatainsheets.csv', low_memory=False)


print("COLUMNAS (con todas las variables)")

print(df.columns)

print("_____________________________")

#me quedo con las variables que considero relevantes
df_cleanded = df[['Weekday', 'Hour', 'IsReshare', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'text']]

#elimino filas con valores faltantes
df_cleanded.dropna(inplace=True)

print("COLUMNAS (con las variables de interes)")
print(df_cleanded.columns)

print("_____________________")

print("PARTE DEL FICHERO")

print(df_cleanded.head(n=10))

#ya que tenemos el dataframe sin valores faltantes, hacer el EDA



import pandas as pd

df = pd.read_csv('files\TweetsEngagementMetrics.csv')

#extraccion de los datos

print("COLUMNAS (con todas las variables)")

print(df.columns)

print("_____________________________")


print("COLUMNAS (tras la seleccion de variables relevantes)")
#me quedo con las variables que considero relevantes

df_cleanded = df[['Weekday', 'Hour', 'Reach', 'RetweetCount', 'Likes', 'Klout', 'text']]

print(df_cleanded.columns)

print("Descripción")
print("_____________")
print(df_cleanded.describe())

print("info")
print("_________")
print(df_cleanded.info())



print("COLUMNAS (con las variables de interes)")
print(df_cleanded.columns)

print("_____________________")

print("PARTE DEL FICHERO")

print(df_cleanded.head(n=10))

#ya que tenemos el dataframe sin valores faltantes, genero un nuevo .csv con ese dataframe

df_cleanded.to_csv('files\TwitterDatashetClean.csv', index=False)
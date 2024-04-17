import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('files\TwitterDatashetCleanC.csv')

df.drop('isViral')

# por ahora ignoro la viralidad, ya que en verdad, depende del Reach y Klout
variables_respuesta = ['Reach', 'Klout']

X = df.drop(variables_respuesta, axis=1)  # Eliminamos las columnas de las variables de respuesta
y = df[variables_respuesta]

modelos = {}
predicciones = {}

print(X.columns)

print(X.head())


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('files\TwitterDatashetCleanB.csv')

'''
tras realizar el analisis exploratorio de datos, eliminamos columnas y nos quedamos con las variables de entrada definitivas 
y las variables de salida definitivas.

Voy a considerar como variables de entrada definitivas las siguientes columnas, ademas, al ser un nuevo dataset propio,
le agrego la columna comentarios en referencia al numero de comentarios que ha recibido el tweet, de cara al dataset de prediccion.
Una vez realizada la prediccion, en una siguiente iteraccion se tendra en cuenta la columna de comentarios:

WeekDay, Hour, IsReshare, RetweetCount, Likes, text, Weekend, FranjaHoraria.

la variable text no se considera exactamente una variable de entrada, pero puede ser util a nivel contextual

Por otro lado, las variables de salida a determinar son:
Klout y Reach.
'''

#para realizar la prediccion, los datos no numericos tengo que pasarlos a numericos, ya que los

df_train = df[['Weekday', 'Hour', 'IsReshare', 'RetweetCount', 'Likes', 'text', 'Weekend', 'FranjaHoraria', 'Klout', 'Reach']]

print(df_train.columns)

print(df_train.head())

#procedo a la prevision

X = df_train[['Weekday', 'Hour', 'IsReshare', 'RetweetCount', 'Likes', 'Weekend', 'FranjaHoraria']]

y = df_train[['Klout', 'Reach']]

# Convertir las variables categóricas en variables dummy
X_encoded = pd.get_dummies(X, columns=['Weekday', 'FranjaHoraria', 'IsReshare', 'Weekend'])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Entrenar un modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print('Error cuadrático medio:', mse)


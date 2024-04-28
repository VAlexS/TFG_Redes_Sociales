import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


df = pd.read_csv('files\TwitterDatashetCleanB.csv')

print(df)

print("____________-")



#los datos no numericos los transformo a numericos
dias_a_numeros = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

df['Weekday'] = df['Weekday'].map(dias_a_numeros)

df['IsReshare'] = df['IsReshare'].astype(int)

df['Weekend'] = df['Weekend'].map({'Yes': 1, 'No': 0})

franja_horaria_numeros = {
    'Madrugada': 1,
    'Mañana': 2,
    'Tarde': 3,
    'Noche': 4
}

df['FranjaHoraria'] = df['FranjaHoraria'].map(franja_horaria_numeros)

# por ahora ignoro la viralidad, ya que en verdad, depende del Reach y Klout
caracteristicas = ['Weekday', 'Hour', 'IsReshare', 'RetweetCount', 'Likes', 'Weekend', 'FranjaHoraria']
objetivos = ['Klout', 'Reach']

print(df)



X = df[caracteristicas]
y = df[objetivos]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Entrenar un modelo separado para Klout y Reach
modelos = {}
predicciones = {}
for objetivo in objetivos:
    # Crear y entrenar el modelo
    modelo = RandomForestRegressor()
    modelo.fit(X_train, y_train[objetivo])

    # Evaluar el modelo en el conjunto de prueba
    y_pred = modelo.predict(X_test)

    # Almacenar el modelo y las predicciones
    modelos[objetivo] = modelo
    predicciones[objetivo] = y_pred

    # Calcular el error cuadrático medio
    mse = mean_squared_error(y_test[objetivo], y_pred)
    print(f"Error cuadrático medio para {objetivo}: {mse}")


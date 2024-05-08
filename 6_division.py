import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('files\TwitterDatashetCleanB.csv')

dias_a_numeros = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

weekend_numeric = {'No': 0, 'Yes': 1}

franja_horaria_numerico = {'Madrugada': 1, 'Mañana': 2, 'Tarde': 3, 'Noche': 4}

df['Weekday'] = df['Weekday'].map(dias_a_numeros)

df['Weekend'] = df['Weekend'].map(weekend_numeric)

df['FranjaHoraria'] = df['FranjaHoraria'].map(franja_horaria_numerico)

X = df[['Weekday', 'Hour', 'RetweetCount', 'Likes', 'Weekend', 'FranjaHoraria']]

y = df[['Reach', 'Klout']]

# Divido el conjunto de datos en conjuntos de entrenamiento y prueba, 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

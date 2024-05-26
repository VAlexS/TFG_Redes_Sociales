import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('files/TwitterDatashetTransformado.csv')

X = df[['Weekday', 'Hour', 'RetweetCount', 'Likes', 'Weekend', 'FranjaHoraria']]
y = df[['Reach']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)

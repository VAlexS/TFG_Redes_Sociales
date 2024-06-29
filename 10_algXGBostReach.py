from math import sqrt

import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv('files/TwitterDatashetTransformado.csv')

X = df[['Weekday', 'Hour', 'RetweetCount', 'Weekend']]
y = df[['Reach']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = XGBRegressor()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

# Metricas

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

rmse = sqrt(mse)

mae = median_absolute_error(y_test, y_pred)

mape = mean_absolute_percentage_error(y_test, y_pred)


#Resultados

print("Mean Squared Error (MSE):", mse)

print("Coeficiente de determinacion (R2): ", r2)

print("Root Mean Squared Error (RMSE): ", rmse)

print("Median Absolute Error (MAE): ", mae)

print("Mean Absolute Percentage Error (MAPE): ", mape)



import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

df = pd.read_csv('files\TwitterDatashetTransformado.csv')


scaler = MinMaxScaler()

df['ReachNormalizado'] = scaler.fit_transform(df[['Reach']])

X = df[['Weekday', 'Hour', 'RetweetCount', 'Likes', 'Weekend', 'FranjaHoraria']]

y = df[['ReachNormalizado']]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = XGBRegressor()

#model = RandomForestRegressor(n_estimators=100, random_state=42)

#model = DecisionTreeRegressor()

#model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)


print("Mean Squared Error:", mse)
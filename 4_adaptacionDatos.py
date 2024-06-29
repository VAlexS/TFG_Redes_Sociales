import pandas as pd

df = pd.read_csv('files\TwitterDatashetCleanB.csv')

dias_a_numeros = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

weekend_numeric = {'No': 0, 'Yes': 1}

franja_horaria_numerico = {'Madrugada': 1, 'Mañana': 2, 'Tarde': 3, 'Noche': 4}

df['Weekday'] = df['Weekday'].map(dias_a_numeros)

df['Weekend'] = df['Weekend'].map(weekend_numeric)

df['FranjaHoraria'] = df['FranjaHoraria'].map(franja_horaria_numerico)


df.to_csv('files\TwitterDatashetTransformado.csv', index=False)



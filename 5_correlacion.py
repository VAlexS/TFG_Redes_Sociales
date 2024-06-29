import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('files\TwitterDatashetTransformado.csv')

'''
print(df.corr())

print("________________________________________")

'''

print("Metricas correlacion FranjaHoraria - Klout")

corr_test = pearsonr(x=df['FranjaHoraria'], y=df['Klout'])


print("P-value: ", corr_test[1])


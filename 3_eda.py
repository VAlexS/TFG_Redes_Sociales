import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('files\TwitterDatashetCleanB.csv')


# comparativa dia de la semana con Reach
dias_semana = df['Weekday']

reach = df['Reach']

plt.bar(dias_semana, reach)

plt.xlabel('Dias_semana')

plt.ylabel('Reach')

plt.title('Diagrama de Barras Reach - dias')

plt.show()

# comparativa dia de la semana con Klout
klout = df['Klout']

plt.bar(dias_semana, klout)

plt.xlabel('Dias_semana')

plt.ylabel('Nivel de influencia (klout)')

plt.title('Diagrama de Barras Klout - dias')

plt.show()
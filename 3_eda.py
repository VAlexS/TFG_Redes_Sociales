import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('files\TwitterDatashetCleanB.csv')

'''
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
'''


'''
franja_horaria = df['FranjaHoraria']

reach = df['Reach']

plt.bar(franja_horaria, reach)

plt.xlabel('Franja_Horaria')

plt.ylabel('Reach')

plt.title('Diagrama de barras Reach - Franja Horaria')

plt.show()

#___________________________

franja_horaria = df['FranjaHoraria']

klout = df['Klout']

plt.bar(franja_horaria, klout)

plt.xlabel('Franja_Horaria')

plt.ylabel('Klout')

plt.title('Diagrama de barras Klout - Franja Horaria')

plt.show()

#_____________________________________

'''

'''
horas = df['Hour']

reach = df['Reach']

plt.bar(horas, reach)

plt.xlabel('Horas')

plt.ylabel('Reach')

plt.title('Diagrama de barras Reach - Horas')

plt.show()

#___________________________

horas = df['Hour']

klout = df['Klout']

plt.bar(horas, klout)

plt.xlabel('Horas')

plt.ylabel('Klout')

plt.title('Diagrama de barras Klout - Horas')

plt.show()

'''

'''
likes = df['Likes']

reach = df['Reach']

plt.bar(likes, reach)

plt.xlabel('Likes')

plt.ylabel('Reach')

plt.title('Diagrama de barras Reach - Likes')

plt.show()

#___________________________

likes = df['Likes']

klout = df['Klout']

plt.bar(likes, klout)

plt.xlabel('Likes')

plt.ylabel('Klout')

plt.title('Diagrama de barras Klout - Likes')

plt.show()

'''

weekend = df['Weekend']

reach = df['Reach']

plt.bar(weekend, reach)

plt.xlabel('Weekend')

plt.ylabel('Reach')

plt.title('Diagrama de barras Reach - Weekend')

plt.show()

#___________________________

weekend = df['Weekend']

klout = df['Klout']

plt.bar(weekend, klout)

plt.xlabel('Weekend')

plt.ylabel('Klout')

plt.title('Diagrama de barras Klout - Weekend')

plt.show()








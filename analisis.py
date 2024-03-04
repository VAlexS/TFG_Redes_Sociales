import numpy as np
import pandas as pd


df = pd.read_csv('files\TwitterDatashetClean.csv', low_memory=False)

print(df.columns)

print(df.head(n=10))




umbral_retweets = 100

umbral_klout = 50
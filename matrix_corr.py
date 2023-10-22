import pandas as pd
import numpy as np

df = pd.read_csv('BostonHousing.csv', sep=',')
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')
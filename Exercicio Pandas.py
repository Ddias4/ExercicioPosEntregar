import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('dirtydata2.csv')


print(df)

df.dropna(inplace = True)
df.drop_duplicates(inplace = True)
df['Date'] = pd.to_datetime(df['Date'])

Duracao_media = df['Duration'].median()
Pulso_medio = df['Pulse'].median()
Pulsomax_medio = df['Maxpulse'].median()
Calorias_media = df['Calories'].median()


filter_data = df['Date'].isnull()

f1 = df['Duration'] >=2*Duracao_media
f2= df['Pulse']>= 2*Pulso_medio
f3= df['Pulse']<=Pulso_medio/2
f4 = df['Maxpulse']>= 2*Pulsomax_medio
f5 = df['Calories']>= 2*Calorias_media


df.loc[f1==True,'Duration'] = Duracao_media
df.loc[f2==True,'Pulse'] = Pulso_medio
df.loc[f3==True,'Pulse'] = Pulso_medio
df.loc[f4==True,'Maxpulse'] = Pulsomax_medio
df.loc[f5==True,'Calories'] = Calorias_media


df['Duration'].fillna(Duracao_media, inplace = True)
df['Pulse'].fillna(Pulso_medio, inplace = True)
df['Maxpulse'].fillna(Pulsomax_medio, inplace = True)
df['Calories'].fillna(Calorias_media, inplace = True)




print(df)

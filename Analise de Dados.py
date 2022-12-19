import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dados1.csv')

df['DateTime'] = df['Date'] + ' ' + df['Time']
df['DateTime'] = pd.to_datetime(df.DateTime,format='%d/%m/%Y %H:%M:%S' )

df1 = df[['DateTime','Sub_metering_1','Sub_metering_2','Sub_metering_3']]


linhas_erradas = df1[(df1['Sub_metering_1'] == '?') | (df1['Sub_metering_2'] == '?')| (df1['Sub_metering_3'] == '?')].index
df2= df1.drop(linhas_erradas)

df2[['Sub_metering_1','Sub_metering_2','Sub_metering_3']] = df2[['Sub_metering_1','Sub_metering_2','Sub_metering_3']].apply(pd.to_numeric)

clinhs = df2[df2.columns[0]].count()

sub1 = np.ndarray(shape=(24,),dtype=float)
sub2 = np.ndarray(shape=(24,),dtype=float)
sub3 = np.ndarray(shape=(24,),dtype=float)
subt = np.ndarray(shape=(24,),dtype=float)

for h in range(24):
    hora = str(h)
    df2.index = pd.to_datetime(df2['DateTime'])
    df3 = df2.between_time(hora+':00:00',hora+':59:59')
    sub1[h] = df3['Sub_metering_1'].sum()
    sub2[h] = df3['Sub_metering_2'].sum()
    sub3[h] = df3['Sub_metering_3'].sum()

    subt[h]= sub1[h]+sub2[h]+sub3[h]

mediasub1 = df2['Sub_metering_1'].mean()
print('Consumo medio sub_meterinf_1: {:.2f}'.format(mediasub1))

mediasub2 = df2['Sub_metering_2'].mean()
print('Consumo medio sub_meterinf_2: {:.2f}'.format(mediasub2))

mediasub3 = df2['Sub_metering_3'].mean()
print('Consumo medio sub_meterinf_3: {:.2f}'.format(mediasub3))

maxSub1=df2['Sub_metering_1'].max()
print('Consumo max Sub_meteting_1:',maxSub1)

maxSub2=df2['Sub_metering_2'].max()
print('Consumo max Sub_meteting_2:',maxSub2)

maxSub3=df2['Sub_metering_3'].max()
print('Consumo max Sub_meteting_3:',maxSub3)

h = np.arange(24)
plt.subplot(4,1,1)
plt.bar(h,sub1)
plt.xlabel('hora')
plt.ylabel('consumo')
plt.title('Sub-meter 1')

plt.subplot(4,1,2)
plt.bar(h,sub2)
plt.xlabel('hora')
plt.ylabel('consumo')
plt.title('Sub-meter 2')

plt.subplot(4,1,3)
plt.bar(h,sub3)
plt.xlabel('hora')
plt.ylabel('consumo')
plt.title('Sub-meter 3')

plt.subplot(4,1,4)
plt.bar(h,subt)
plt.xlabel('hora')
plt.ylabel('consumo')
plt.title('Sub-meter total')

plt.show()




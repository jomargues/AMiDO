######################################################################################################

import easygui as eg
import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as sp

######################################################################################################

def pega_arquivo():
    arquivo = eg.fileopenbox()

    return arquivo


def df(arquivo):
    df = pd.read_csv(str(arquivo), index_col=False)

    return df

######################################################################################################

arquivo1 = pega_arquivo()
arquivo2 = pega_arquivo()

df1 = df(arquivo1)
df2 = df(arquivo2)

print("-" * 120)
print('')
print('Desvios Padrão:')
print('')
print(df1[['GR', 'MR']].std())
print('')
print(df2[['GR1', 'MR1', 'GR2', 'MR2']].std())
print('')
print("-" * 120)

t1 = df1['timestamp'].values
f1 = df1['GR'].values
g1 = df1['MR'].values

t2 = df2['timestamp'].values
f2 = df2['GR1'].values
g2 = df2['MR1'].values
h2 = df2['GR2'].values
y2 = df2['MR2'].values

fig = plt.figure()

ax1 = fig.add_subplot(3, 2, 1)
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Posição Angular (rad)')
plt.plot(t1, f1)
plt.title("GR PV")

ax2 = fig.add_subplot(3, 2, 2)
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Posição Angular (rad)')
plt.plot(t1, g1)
plt.title("MR PV")

ax3 = fig.add_subplot(3, 2, 3)
ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel('Posição Angular (rad)')
plt.plot(t2, f2)
plt.title("GR1 Logging")

ax4 = fig.add_subplot(3, 2, 4)
ax4.set_xlabel('Tempo (s)')
ax4.set_ylabel('Posição Angular (rad)')
plt.plot(t2, g2)
plt.title("MR1 Logging")

ax5 = fig.add_subplot(3, 2, 5)
ax5.set_xlabel('Tempo (s)')
ax5.set_ylabel('Posição Angular (rad)')
plt.plot(t2, h2)
plt.title("GR2 Logging")

ax6 = fig.add_subplot(3, 2, 6)
ax6.set_xlabel('Tempo (s)')
ax6.set_ylabel('Posição Angular (rad)')
plt.plot(t2, y2)
plt.title("MR2 Logging")

plt.tight_layout()

plt.show()

######################################################################################################

import pandas as pd
import numpy as np

df = pd.read_csv("inf_main.csv")

df["Genero"] = df["Genero"].replace(['hombre'],0)
df["Genero"] = df["Genero"].replace(['mujer'],1)

df["Hijos del matrimonio"] = df["Hijos del matrimonio"].replace(['no'],0)
df["Hijos del matrimonio"] = df["Hijos del matrimonio"].replace(['si'],1)

print(pd.DataFrame((df["Infidelidades"]).groupby(df["Genero"]).mean()))
print(pd.DataFrame((df["Infidelidades"]).groupby(df["Genero"]).count()))

print (df)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Infidelidad vs Genero")
plt.xlabel("Genero")
plt.ylabel("Infidelidades")

plt.hist([df[df['Infidelidades']>0]['Genero'],df[df['Infidelidades']==0]['Genero']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Infiel','Fiel'])

plt.subplot(1,2,2)
plt.title("Infidelidad vs Edad")
plt.xlabel("Edad")
plt.ylabel("Infidelidades")

plt.hist([df[df['Infidelidades']>0]['Edad'],df[df['Infidelidades']==0]['Edad']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Infiel','Fiel'])
plt.show()

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Infidelidad vs Años casado")
plt.xlabel("Años casado")
plt.ylabel("Infidelidades")

plt.hist([df[df['Infidelidades']>0]['Años casado'],df[df['Infidelidades']==0]['Años casado']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Infiel','Fiel'])

plt.subplot(1,2,2)
plt.title("Infidelidad vs Hijos del matrimonio")
plt.xlabel("Hijos del matrimonio")
plt.ylabel("Infidelidades")

plt.hist([df[df['Infidelidades']>0]['Hijos del matrimonio'],df[df['Infidelidades']==0]['Hijos del matrimonio']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Infiel','Fiel'])
plt.show()
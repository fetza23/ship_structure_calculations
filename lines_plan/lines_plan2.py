import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from hidrostatik import *
print(df)
print(df.loc[12])


y = np.array([0, 0.3 * D / 6, D / 6, 2 * D / 6, 3 * D / 6, 4 * D / 6, 5 * D / 6, D])
print(y)

plt.figure(figsize=(12, 8))
#    if i<=len(df.shape)
print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",df.shape)
for i in range(len(df)):
    if i <=len(df)/2:
        x1 = df.iloc[i, df.columns.get_loc("WL0"):]
        plt.plot(-x1, y, "red")
        x0 = (0, 0)
        y0 = (min(x1), 0)
        plt.plot(y0, x0, "red")
    else:
        x1 = df.iloc[i, df.columns.get_loc("WL0"):]
        plt.plot(x1, y, "red")
        x0 = (0, 0)
        y0 = (-min(x1), 0)
        plt.plot(y0, x0, "red")


plt.axvline(x=0, color='black', linestyle='--', linewidth=1)  # 0 noktasını belirten dikey çizgi
plt.show()



#PROFİL KESİT
x1=np.linspace(0,L,100)
y1=[D]*len(x1)
plt.plot(x1,y1)
plt.show()


#AFT
aftx=[-28.748,-25,-16.8799,17.126,19.1683,19.1683,19.1683]
afty=[0, D / 6, 2 * D / 6, 3 * D / 6, 4 * D / 6, 5 * D / 6, D]
afty.reverse()
print(afty)
for i, k in zip(aftx, range(len(aftx))):
    a = i * L/2000
    aftx[k] = a
#print("aftx",aftx)
plt.figure(figsize=(15,2))
plt.plot(aftx,afty)

#FORWARD
forx=[7.250,3.2972,0,-2.4442,-4.1257,-4.1257,-4.1257]
fory=[D,5 * D / 6 , 4 * D / 6, 3 * D / 6, 2 * D / 6 ,D / 6 ,0]

for i, k in zip(forx, range(len(forx))):
    a = L+ i * L/1000
    forx[k] = a

plt.plot(forx,fory)
#BASE
xbase=np.linspace(aftx[-1],forx[-1],100)
ybase=[0]*len(xbase)
plt.plot(xbase,ybase)

#SİYER
siyerx = [0, L/6, 2*L/6, L/2, 4*L/6, 5*L/6, L]
siyery = [25, 11.1, 2.8, 0, 5.6, 22.2, 50]
for i, k in zip(siyery, range(len(siyery))):
    a = i * (L/3 + 10)/2000 +D
    siyery[k] = a



plt.plot(siyerx,siyery)
#print(siyery)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

import pandas as pd
from hidrostatik import *
L = 74
B = 10.89
T=4.737
D=7.1
CB=0.68
W=L*B*T*CB*1.025
q=W/L
print("q",q)
print("W",W)

distance=yeni_df["distance"]

# BU ORTA NARİNLİKTE BİR GEMİ İÇİN NARİN VE DOLGUN GEMİLER İÇİN KATSAYILAR DEĞİŞİYOR

# PROHASKA METHOD
a = q * 0.68
b = q * 1.185
c = q * 0.58
wtop=[]
for i in range(len(distance)+1):
    if i <= len(distance) / 3:
        q = a + i * ((b - a) / (len(distance) / 3))
        wtop.append(q)
    elif i <= 2 * len(distance) / 3:
        if i==len(distance)//2: #bunu eklemek zorunda kaldım eleman sayısı 1 fazla çıkıyordu
            pass
        else:
            q = b
            wtop.append(q)
    else:
        q = b - (i - 2 * len(distance) / 3) * ((b - c) / (len(distance) / 3))
        wtop.append(q)
q = pd.DataFrame(wtop, columns=['q'])
#SM_WL4=SM_creator(WL4A)
delta_h=abs(W-DV())/(AWP()*1.025)
print("deltah",delta_h)

print("DV",DV())

def carpim1():
    carpim1=Alan(T-delta_h)*SM_creator(Alan())
    return carpim1

def DV(s=0.5):
    DV=1/3*s*sum(carpim1())
    return DV
print("DV",DV())

newT=T-delta_h

ndelta_h=abs(W-DV())/(AWP()*1.025)
print("deltah",ndelta_h)


def carpim1():
    carpim1=Alan(newT+ndelta_h)*SM_creator(Alan())
    return carpim1

def DV(s=0.5):
    DV=1/3*s*sum(carpim1())
    return DV
print("DV",DV())
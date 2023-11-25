import pandas as pd
from hidrostatik import *

L = 74
B = 10.89
T = 4.737
D = 7.1
CB = 0.8
W = L * B * T * CB * 1.025
q = W / L
print("q", q)
print("W", W)

distance = yeni_df["distance"]

# PROHASKA METHOD # ORTA NARİNLİKTEKİ GEMİ İÇİN KATSAYILAR
a = q * 0.68
b = q * 1.185
c = q * 0.58
wtop = []
for i in range(len(distance) + 1):
    if i <= len(distance) / 3:
        q = a + i * ((b - a) / (len(distance) / 3))
        wtop.append(q)
    elif i <= 2 * len(distance) / 3:
        if i == len(distance) // 2:
            pass
        else:
            q = b
            wtop.append(q)
    else:
        q = b - (i - 2 * len(distance) / 3) * ((b - c) / (len(distance) / 3))
        wtop.append(q)
q = pd.DataFrame(wtop, columns=['q'])


delta_h = abs(W - DW(T)) / (AWP(T) )

while abs(DW(T) - W) > 0.1:
    new_T = T + delta_h if DW(T) < W else T - delta_h
    new_DW = DW(new_T)
    new_AWP = AWP(new_T)
    delta_h = abs(W - new_DW) / (new_AWP )
    print(f"New T: {new_T}, New Delta_h: {delta_h}")
    T = new_T

print(f"Final T: {T}, Final DW: {DW(T)}")



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
from hidrostatik import *
from itertools import chain
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
lenL=np.linspace(0,L,21)
Trochoidal=[1,0.966,0.871,0.795,0.578,0.422,0.28,0.16,0.072,0.018,0, 0.018,0.072,0.16,0.28,0.422,0.578,0.795,0.871,0.966,1]
stokes=[1,0.961,0.85,0.691,0.512,0.343,0.203,0.103,0.041,0.009,0,0.009,0.041,0.103,0.203,0.343,0.512,0.691,0.85,0.961,1]

print(len(Trochoidal))
print(len(stokes))
L = 70
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
def q_calculate():
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
    return q
q=q_calculate()

def delta_h():
    delta_h = abs(W - DW(T)) / (AWP(T) )
    return delta_h
delta_h=delta_h()

while abs(DW(T) - W) > 0.01:
    new_T = T + delta_h if DW(T) < W else T - delta_h
    new_DW = DW(new_T)
    new_AWP = AWP(new_T)
    delta_h = abs(W - new_DW) / (new_AWP )
    print(f"New T: {new_T}, New Delta_h: {delta_h}")
    T = new_T

print(f"Final T: {T}, Final DW: {DW(T)}")
def LCB():
    t1 = sum(Alan(T) * distance)
    t2 = sum(Alan(T))
    return t1 / t2


def LCG(q):
    return sum(q["q"] * distance) / sum(q["q"])

x_lcg = DW(T) * (LCB() - LCG(q)) / L ** 2 * 54 / 7
x_lcglist1 = np.linspace(-x_lcg, 0, len(q)//3+1)
x_lcglist2 = np.repeat([0], len(q)//3-2)
x_lcglist3 = np.linspace(0, x_lcg, len(q)//3+1)
x = np.concatenate((x_lcglist1,x_lcglist2, x_lcglist3))
x_lcglcb=pd.DataFrame(x)

if LCB()>LCG(q):
    result = q["q"].values + x_lcglcb[0].values
    new_q = pd.DataFrame(result, columns=['q'])

ax=Alan(T)*1.025

Px=new_q["q"].values - ax
################################# SPX ###################################
SPx=[0]
for i in range(len(Px)-1):
    a=(Px[i]+Px[i+1])/2+SPx[i]
    SPx.append(a)
SPx=np.array(SPx)

#if abs(SPx[-1])/max(SPx)>3/100: #%3 ü eklersin
fix=np.linspace(0,SPx[-1],len(q))
SPx_fixed = SPx- fix

############################### SSPX #################################
SSPx = [0]
for i in range(1, len(SPx_fixed)):
    a = (SPx_fixed[i-1] + SPx_fixed[i]) / 2 + SSPx[i-1]
    SSPx.append(a)

np.set_printoptions(precision=2, suppress=True)
fix=np.linspace(0,SSPx[-1],len(q))
SSPx_fixed = np.array(SSPx) - fix

print("################################ Q ########################################")

Q=SPx_fixed*0.5

print("################################ M ########################################")

M=SSPx_fixed*0.5**2
print(max(M))
print(max(Q))
#######################################################################################
distance = np.array(distance)
df_q = pd.DataFrame(Q, columns=["Q"])
df_m = pd.DataFrame(M, columns=["M"])
df_distance = pd.DataFrame(distance, columns=["distance"])
result_df_CalmWater = pd.concat([df_distance, df_q, df_m], axis=1)
result_df_CalmWater.index.name = "postalar"
print(result_df_CalmWater)


print("ffffffffffffffffffffffffffffffffffffffff  WAVE THROUGH DRAUGHTS fffffffffffffffffffffffffffffffffffffff")
np.set_printoptions(precision=5, suppress=True)
lenL=np.linspace(0,L,21)
Trochoidal_WT=np.array([1,0.966,0.871,0.795,0.578,0.422,0.28,0.16,0.072,0.018,0, 0.018,0.072,0.16,0.28,0.422,0.578,0.795,0.871,0.966,1])
stokes_WT=np.array([1,0.961,0.85,0.691,0.512,0.343,0.203,0.103,0.041,0.009,0,0.009,0.041,0.103,0.203,0.343,0.512,0.691,0.85,0.961,1])
lenL_interp=np.linspace(0,L,len(distance))

wave_trochoidal_cubicBC_WT=CubicSpline(lenL,Trochoidal_WT,bc_type="natural")
trochidal_wave_WT=wave_trochoidal_cubicBC_WT(lenL_interp)
print("trochidal",trochidal_wave_WT)
wave_stokes_cubicBC_WT=CubicSpline(lenL,stokes_WT,bc_type="natural")
stokes_wave_WT=wave_stokes_cubicBC_WT(lenL_interp)
print("stokes",stokes_wave_WT)
plt.plot(lenL_interp,stokes_wave_WT,"black")
plt.plot(lenL_interp,trochidal_wave_WT,"red")

plt.plot(lenL,Trochoidal_WT,"o")
plt.plot(lenL,stokes_WT,"o","blue")

def S_WT(T):
    S_WT=[]
    for c in stokes_wave_WT: # WAVE THROUGH
        a=(T-L/40)+L/20*c
        S_WT.append(a)
    return S_WT
S_WT=S_WT(T)
def T_WT(T):
    T_WT=[]
    for c in trochidal_wave_WT:
        a=(T-L/40)+L/20*c
        T_WT.append(a)
    return T_WT
T_WT=T_WT(T)
print(T_WT)
print(len(T_WT))
print(len(S_WT))

print("ffffffffffffffffffffffffffffffffffffffff  WAVE CREST DRAUGHTS fffffffffffffffffffffffffffffffffffffff")

Trochoidal_WC=np.array([0, 0.018,0.072,0.16,0.28,0.422,0.578,0.795,0.871,0.966,1,0.966,0.871,0.795,0.578,0.422,0.28,0.16,0.072,0.018,0])
stokes_WC=np.array([0,0.009,0.041,0.103,0.203,0.343,0.512,0.691,0.85,0.961,1,0.961,0.85,0.691,0.512,0.343,0.203,0.103,0.041,0.009,0])

wave_trochoidal_cubicBC_WC=CubicSpline(lenL,Trochoidal_WC,bc_type="natural")
trochidal_wave_WC=wave_trochoidal_cubicBC_WC(lenL_interp)
print("trochidal",trochidal_wave_WC)
wave_stokes_cubicBC_WC=CubicSpline(lenL,stokes_WC,bc_type="natural")
stokes_wave_WC=wave_stokes_cubicBC_WC(lenL_interp)
print("stokes",stokes_wave_WC)
plt.plot(lenL_interp,stokes_wave_WC,"black")
plt.plot(lenL_interp,trochidal_wave_WC,"red")

plt.plot(lenL,Trochoidal_WC,"o")
plt.plot(lenL,stokes_WC,"o","blue")
plt.show()

def S_WC1(T):
    S_WC=[]
    for c in stokes_wave_WC: # WAVE THROUGH
        a=(T-L/40)+L/20*c
        S_WC.append(a)
    return S_WC
S_WC=S_WC1(T)
def T_WC(T):
    T_WC=[]
    for c in trochidal_wave_WC:
        a=(T-L/40)+L/20*c
        T_WC.append(a)
    return T_WC
T_WC=T_WC(T)

print("######################################### AREA FUNCTİON ##############################################")

wl_wave=np.array([1,2,3,4,5,6])
def wave_area_calculate(W_type):
    area=[]
    W_type=pd.DataFrame(W_type)
    for i in range(len(alanlar)):
        wave_area=CubicSpline(wl_wave,alanlar.loc[i],bc_type="natural")
        b=wave_area(W_type.loc[i])
        B=list(b)
        area.append(B)
    return area


stokes_area_WC=wave_area_calculate(S_WC)
stokes_area_WT=wave_area_calculate(S_WT)
trochidal_area_WC=wave_area_calculate(T_WC)
trochidal_area_WT=wave_area_calculate(T_WT)

stokes_area_WC = list(chain(*stokes_area_WC))
stokes_area_WT = list(chain(*stokes_area_WT))
trochidal_area_WC = list(chain(*trochidal_area_WC))
trochidal_area_WT = list(chain(*trochidal_area_WT))

"""print(stokes_area_WC)
print(stokes_area_WT)
print(trochidal_area_WC)
print(trochidal_area_WT)
"""

print("#############################################################################################################")
def carpim_1(wave):
    carpim1=wave*SM_creator(wave)
    return carpim1
dw_swc=carpim_1(stokes_area_WC)
dw_swt=carpim_1(stokes_area_WT)
dw_twc=carpim_1(trochidal_area_WC)
dw_twt=carpim_1(trochidal_area_WT)
def DV_WAVE(X,s=0.5):
    DV=1/3*s*sum(X)
    return DV

def DW_WAVE(X):
    DW=X*1.025
    return DW
DV_SWC=DV_WAVE(dw_swc)
DV_SWT=DV_WAVE(dw_swt)
DV_TWC=DV_WAVE(dw_twc)
DV_TWT=DV_WAVE(dw_twt)
DW_SWC=DW_WAVE(DV_SWC)
DW_SWT=DW_WAVE(DV_SWT)
DW_TWC=DW_WAVE(DV_TWC)
DW_TWT=DW_WAVE(DV_TWT)

print("DWSWC",DW_SWC)
print("DWSWT",DW_SWT)
print("DWTWT",DW_TWT)
print("DWTWC",DW_TWC)
W = L * B * T * CB * 1.025
print("W",W)


"""
print("########################## stokes wave crest ##############################")
q=q_calculate()

def delta_h():
    delta_h = abs(W - DW_SWC) / (AWP(T) )
    return delta_h
delta_h=delta_h()
print("deltah swc",delta_h)
while abs(DW_SWC - W) > 0.001:
    new_T = T + delta_h if DW(T) < W else T - delta_h
    S_WC_new=S_WC1(new_T)
    stokes_area_WC_new = wave_area_calculate(S_WC_new)
    stokes_area_WC_new = list(chain(*stokes_area_WC_new))
    dw_swc_new = carpim_1(stokes_area_WC_new)
    DV_SWC_new = DV_WAVE(dw_swc_new)
    DW_SWC_new = DW_WAVE(DV_SWC_new)
    new_AWP = AWP(new_T)
    delta_h = abs(W - DW_SWC_new) / (new_AWP )
    print(f"New T: {new_T}, New Delta_h: {delta_h}, NEW DW {DW_SWC_new} , W {W}")
    T = new_T
    if abs(DW_SWC_new-W)<=1: #0.1 yapınca bir türlü bulamıyor döngü devam ediyor
        break


print(f"Final T: {T}, Final DW: {DW_SWC_new}")


def LCB():
    t1 = sum(stokes_area_WC_new * distance)
    t2 = sum(stokes_area_WC_new)
    return t1 / t2

print(LCB())
def LCG(q):
    return sum(q["q"] * distance) / sum(q["q"])

print(LCG(q))

x_lcg = DW_SWC_new * (LCB() - LCG(q)) / L ** 2 * 54 / 7
print(x_lcg)
x_lcglist1 = np.linspace(-x_lcg, 0, len(q)//3+1)
x_lcglist2 = np.repeat([0], len(q)//3-2)
x_lcglist3 = np.linspace(0, x_lcg, len(q)//3+1)
x = np.concatenate((x_lcglist1,x_lcglist2, x_lcglist3))
x_lcglcb=pd.DataFrame(x)"""

"""
if LCB()>LCG(q):
    result = q["q"].values + x_lcglcb[0].values
    new_q = pd.DataFrame(result, columns=['q'])

ax=Alan(T)*1.025

Px=new_q["q"].values - ax
################################# SPX ###################################
SPx=[0]
for i in range(len(Px)-1):
    a=(Px[i]+Px[i+1])/2+SPx[i]
    SPx.append(a)
SPx=np.array(SPx)

#if abs(SPx[-1])/max(SPx)>3/100: #%3 ü eklersin
fix=np.linspace(0,SPx[-1],len(q))
SPx_fixed = SPx- fix

############################### SSPX #################################
SSPx = [0]
for i in range(1, len(SPx_fixed)):
    a = (SPx_fixed[i-1] + SPx_fixed[i]) / 2 + SSPx[i-1]
    SSPx.append(a)

np.set_printoptions(precision=2, suppress=True)
fix=np.linspace(0,SSPx[-1],len(q))
SSPx_fixed = np.array(SSPx) - fix

print("################################ Q ########################################")

Q=SPx_fixed*0.5

print("################################ M ########################################")

M=SSPx_fixed*0.5**2
print(max(M))
print(max(Q))
#######################################################################################
distance = np.array(distance)
df_q = pd.DataFrame(Q, columns=["Q"])
df_m = pd.DataFrame(M, columns=["M"])
df_distance = pd.DataFrame(distance, columns=["distance"])
result_df = pd.concat([df_distance, df_q, df_m], axis=1)
result_df.index.name = "postalar"
print(result_df)

"""
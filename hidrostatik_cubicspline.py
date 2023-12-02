import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
import numpy as np
import pandas as pd

L = 70
B = 10.89
T = 4.737
D = 7.1
CB = 0.68

df = pd.read_excel("yny.xlsx")

print(df)
if "WL0,3" in df.columns:
    WL05 = np.array([])

    for i in range(len(df)):
        y_yi = pd.DataFrame(df.loc[i, "WL0":])
        yi_1 = y_yi.values.flatten()

        wl = np.array([0, 0.3, 1, 2, 3, 4, 5, 6])
        f = CubicSpline(wl, yi_1, bc_type="natural")

        wl = np.linspace(np.min(wl), np.max(wl), 100)
        ff = CubicSpline(wl, f(wl), bc_type="natural")

        WL_05 = ff(0.5)
        WL05 = np.append(WL05, WL_05)

    WL05 = pd.DataFrame(WL05)
    df.insert(df.columns.get_loc("WL0,3") + 1, "WL0,5", WL05)
    df = df.drop(columns=["WL0,3"])

print(df.loc[:, :"WL2"])








df.insert(1, "distance", df["postalar"] * L / 10)

yeni_df_listesi = []
for i in range(df.shape[0] - 1):
    distance_sutun = np.arange(df.loc[i, "distance"], df.loc[i + 1, "distance"], 0.5)
    yeni_df_i = pd.DataFrame({"distance": distance_sutun})

    for col in df.columns[2:]:
        oran = (df.loc[i + 1, col] - df.loc[i, col]) / (df.loc[i + 1, "distance"] - df.loc[i, "distance"])
        yeni_sutun = df.loc[i, col] + oran * (distance_sutun - df.loc[i, "distance"])
        yeni_df_i[col] = yeni_sutun

    yeni_df_listesi.append(yeni_df_i)

yeni_df_listesi.append(df.iloc[-1, :].to_frame().T)
yeni_df = pd.concat(yeni_df_listesi, ignore_index=True)

yeni_df = yeni_df.drop(columns=['postalar'])

yeni_df = yeni_df.rename_axis("postalar")

print(yeni_df.loc[:, :"WL2"])

#BU TEK SAYILI SU HATLARININ h kısmı T/4 OLMAYABİLİR ONU AYARLA

#WL1 E KADAR OLAN ALAN VE MOMENTLER

WL1Alan=[]
SM=[0.5,2,0.5]
WL1Moment=[]
M_K=[0,0.5,1]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl1 e kadar olan alan",a)
    liste=[]
    for col in yeni_df.columns[1:4]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/8*a
    Mcarpim = M_K * carpim
    c=sum(Mcarpim)
    d=2/3*(T/8)**2*c
    WL1Moment.append(d)
    WL1Alan.append(b)
WL1Moment_PDS=pd.Series(WL1Moment)
WL1Alan_PDS=pd.Series(WL1Alan)

#WL2 E KADAR OLAN ALAN VE MOMENTLER


SM=[1,4,1]
WL2Alan=[]
WL2Moment=[]
M_K=[0,1,2]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl2 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL1","WL2"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/4*a
    Mcarpim = M_K * carpim
    c = sum(Mcarpim)
    d = 2 / 3 * (T / 4) ** 2 * c
    WL2Moment.append(d)
    WL2Alan.append(b)
WL2Moment_PDS=pd.Series(WL2Moment)
WL2Alan_PDS=pd.Series(WL2Alan)

#WL3 E KADAR OLAN ALAN VE MOMENTLER

WL3Alan=[]
SM=[0.5,2,1.5,4,1]
WL3Moment=[]
M_K=[0,0.5,1,2,3]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl3 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL0,5","WL1","WL2","WL3"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/4*a
    Mcarpim = M_K * carpim
    c = sum(Mcarpim)
    d = 2 / 3 * (T / 4) ** 2 * c
    WL3Moment.append(d)
    WL3Alan.append(b)
WL3Alan_PDS=pd.Series(WL3Alan)
WL3Moment_PDS=pd.Series(WL3Moment)

#WL4 E KADAR OLAN ALAN VE MOMENTLER

WL4Alan=[]
SM=[1,4,2,4,1]
WL4Moment=[]
M_K=[0,1,2,3,4]
for i in range(len(yeni_df)):  #rint(f"{i}. postanın wl4 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL1","WL2","WL3","WL4"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/4*a
    Mcarpim = M_K * carpim
    c = sum(Mcarpim)
    d = 2 / 3 * (T / 4) ** 2 * c
    WL4Moment.append(d)
    WL4Alan.append(b)
WL4Alan_PDS=pd.Series(WL4Alan)
WL4Moment_PDS=pd.Series(WL4Moment)

#WL5 E KADAR OLAN ALAN VE MOMENTLER

WL5Alan=[]
SM=[0.5,2,1.5,4,2,4,1]
WL5Moment=[]
M_K=[0,0.5,1,2,3,4,5]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl5 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL0,5","WL1","WL2","WL3","WL4","WL5"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/4*a
    Mcarpim = M_K * carpim
    c = sum(Mcarpim)
    d = 2 / 3 * (T / 4) ** 2 * c
    WL5Moment.append(d)
    WL5Alan.append(b)
WL5Alan_PDS=pd.Series(WL5Alan)
WL5Moment_PDS=pd.Series(WL5Moment)

#WL6 E KADAR OLAN ALAN VE MOMENTLER


WL6Alan=[]
SM=[1,4,2,4,2,4,1]
WL6Moment=[]
M_K=[0,1,2,3,4,5,6]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl6 e kadar olan alan",a)
    liste = []
    for col in yeni_df[["WL0","WL1","WL2","WL3","WL4","WL5","WL6"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    b=2/3*T/4*a
    Mcarpim = M_K * carpim
    c = sum(Mcarpim)
    d = 2 / 3 * (T / 4) ** 2 * c
    WL6Moment.append(d)
    WL6Alan.append(b)
WL6Alan_PDS=pd.Series(WL6Alan)
WL6Moment_PDS=pd.Series(WL6Moment)



alanlar = pd.concat([WL1Alan_PDS, WL2Alan_PDS, WL3Alan_PDS, WL4Alan_PDS, WL5Alan_PDS, WL6Alan_PDS], axis=1)
alanlar.columns = ['WL1Alan_PDS', 'WL2Alan_PDS', 'WL3Alan_PDS', 'WL4Alan_PDS', 'WL5Alan_PDS', 'WL6Alan_PDS']
momentler=pd.concat([WL1Moment_PDS, WL2Moment_PDS, WL3Moment_PDS, WL4Moment_PDS, WL5Moment_PDS, WL6Moment_PDS], axis=1)
momentler.columns = ['WL1_Moment', 'WL2_Moment', 'WL3_Moment', 'WL4_Moment', 'WL5_Moment', 'WL6_Moment']



def moment_kolu():
    MK = list(range(-(len(yeni_df)-1)// 2, 0))  + list(range((len(yeni_df)+1)//2))
    MK=pd.Series(MK)
    return MK



def YG(T=2 * D / 3):
    yari_genislik = []
    for i in range(len(yeni_df)):
        y_yi = pd.DataFrame(yeni_df.loc[i, "WL0":])
        yi = y_yi.values.flatten()
        wl = np.array([0, 0.5, 1, 2, 3, 4, 5, 6])
        f=CubicSpline(wl,yi,bc_type="natural")
        wl = np.linspace(np.min(wl), np.max(wl), 100)
        ff=CubicSpline(wl, f(wl), bc_type="natural")
        yarigenislik =ff(T)

        yari_genislik.append(yarigenislik)
    yari_genislik = pd.Series(yari_genislik)
    return yari_genislik

def Alan(T):
    T_A_list = []
    for i in range(len(alanlar)):
        ypd = pd.DataFrame(alanlar.loc[i])
        y = ypd.values.flatten()
        x = np.array([1, 2, 3, 4, 5, 6])
        f = CubicSpline(x, y, bc_type="natural")
        x = np.linspace(np.min(x), np.max(x), 100)
        ff=CubicSpline(x, f(x), bc_type="natural")
        coef = ff(T)

        T_A_list.append(coef)
    T_A_list = pd.Series(T_A_list)
    return T_A_list

def moment(T):
    T_M_list = []
    for i in range(len(momentler)):
        ypd = pd.DataFrame(momentler.loc[i])
        y = ypd.values.flatten()
        x = np.array([1, 2, 3, 4, 5, 6])
        f = CubicSpline(x, y, bc_type="natural")
        x = np.linspace(np.min(x), np.max(x), 100)
        ff = CubicSpline(x, f(x), bc_type="natural")
        coef = ff(T)

        T_M_list.append(coef)
    T_M_list = pd.Series(T_M_list)
    return T_M_list


def SM_creator(nmr):
    SM = [1]
    for i in range(1, len(nmr)-1):
        if i % 2 == 1:
            SM.append(4)
        else:
            SM.append(2)
    SM.append(1)
    SM=pd.Series(SM)
    return SM


def Bwl(T):
    Bwl=max(YG(T)*2)
    return Bwl

def carpim1(T):
    carpim1=Alan(T)*SM_creator(Alan(T))
    return carpim1
def carpim2(T):
    carpim2=moment_kolu()*carpim1(T)
    return carpim2
def carpim3(T):
    carpim3=moment(T)*SM_creator(moment(T))
    return carpim3
def carpim4(T):
    carpim4=SM_creator(yeni_df)*YG(T)
    carpim4=pd.Series(carpim4)
    return carpim4
def carpim5(T):
    carpim5=moment_kolu()*carpim4(T)
    carpim5=pd.Series(carpim5)
    return carpim5
def carpim6(T):
    carpim6=moment_kolu()*carpim5(T)
    return carpim6
def carpim7(T):
    carpim7=YG(T)**3*SM_creator(yeni_df)
    return carpim7



def DV(T,s=0.5):
    DV=1/3*s*sum(carpim1(T))
    return DV

def DW(T):
    DW=DV(T)*1.025
    return DW
def LCB(T,s=0.5):
    LCB=s*sum(carpim2(T))/sum(carpim1(T))
    return LCB
def KB(T):
    KB=sum(carpim3(T))/sum(carpim1(T))
    return KB
def CB(T=2*D/3):
    CB=DV(T)/(L*Bwl(T)*T)
    return CB
def CM(T=2*D/3):
    CM=Alan(T).max()/(Bwl(T)*T)
    return CM
def CP(T):
    CP=CB(T)/CM(T)
    return CP

def LCF(T,s=0.5):
    LCF=s*sum(carpim5(T))/sum(carpim4(T))
    return LCF

def CWP(T):
    CWP=AWP(T)/(Bwl(T)*L)
    return CWP
def AWP(T,s=0.5):
    AWP=2/3*s*sum(carpim4(T))
    return AWP
def TPC(T):
    TPC=AWP(T)/100*1.025
    return TPC
def ix(T,s=0.5):
    ix=2/9*s*sum(carpim7(T))
    return ix

def BM(T):
    BM=ix(T)/DV(T)
    return BM

def i0(T,s=0.5):
    i0=2/3*s**3*sum(carpim6(T))
    return i0

def i_f(T):
    i_f=i0(T)-AWP(T)*LCF(T)**2
    return i_f

def BML(T):
    BML=i_f(T)/DV(T)
    return BML

def MT1(T):
    MT1=DW(T)*BML(T)/L
    return MT1
T=4.73

print(YG(5).loc[70])
print(YG(T).loc[70])
print(YG(D).loc[70])
print("dv",DV(T))
print("dw",DW(T))
print("lcb",LCB(T))
print("kb",KB(T))
print("cb",CB(T))
print("CM",CM(T))
print("CP",CP(T))
print("AWP",AWP(T))
print("LCF",LCF(T))
print("TPC",TPC(T))
print("CWP",CWP(T))
print("ix",ix(T))
print("BM",BM(T))
print("i0",i0(T))
print("i_f",i_f(T))
print("BML",BML(T))
print("MT1",MT1(T))


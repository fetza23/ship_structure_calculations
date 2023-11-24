import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

L = 120
T = 5.820
D=8.73

df = pd.read_excel("mrt.xlsx")
WL05 = np.array([])
if "WL0,3" in df.columns:
    for i in df.index:
        if not pd.isna(df.loc[i, "WL0,3"]) and not pd.isna(df.loc[i, "WL1"]):
            x = (df.loc[i, "WL0,3"] * 5 + 2 * df.loc[i, "WL1"]) / 7
            WL05 = np.append(WL05, x)

    WL05 = pd.DataFrame(WL05)
    df["WL0,3"] = WL05
    df = df.rename(columns={"WL0,3": "WL0,5"})
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





WL1Alan=[]
SM=[0.5,2,0.5]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl1 e kadar olan alan",a)
    liste=[]
    for col in yeni_df.columns[1:4]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T=5.820
    b=2/3*T/4*a
    WL1Alan.append(b)
WL1Alan_PDS=pd.Series(WL1Alan)

WL2Alan=[]
SM=[0.5,2,0.5]

for i in range(len(yeni_df)):  # print(f"{i}. postanın wl2 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL1","WL2"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T=5.820
    b=2/3*T/4*a
    WL2Alan.append(b)
WL2Alan_PDS=pd.Series(WL2Alan)

WL3Alan=[]
SM=[0.5,2,1.5,4,1]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl3 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL0,5","WL1","WL2","WL3"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T = 5.820
    b=2/3*T/4*a
    WL3Alan.append(b)
WL3Alan_PDS=pd.Series(WL3Alan)


WL4Alan=[]
SM=[1,4,2,4,1]
for i in range(len(yeni_df)):  #rint(f"{i}. postanın wl4 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL1","WL2","WL3","WL4"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T = 5.820
    b=2/3*T/4*a
    WL4Alan.append(b)
WL4Alan_PDS=pd.Series(WL4Alan)

WL5Alan=[]
SM=[0.5,2,1.5,4,2,4,1]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl5 e kadar olan alan",a)
    liste=[]
    for col in yeni_df[["WL0","WL0,5","WL1","WL2","WL3","WL4","WL5"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T = 5.820
    b=2/3*T/4*a
    WL5Alan.append(b)
WL5Alan_PDS=pd.Series(WL5Alan)

WL6Alan=[]
SM=[1,4,2,4,2,4,1]
for i in range(len(yeni_df)):  # print(f"{i}. postanın wl6 e kadar olan alan",a)
    liste = []
    for col in yeni_df[["WL0","WL1","WL2","WL3","WL4","WL5","WL6"]]:
        liste.append(yeni_df.loc[i, col])
    liste_ps=pd.Series(liste)
    carpim=SM*liste_ps
    a=sum(carpim)
    T = 5.820
    b=2/3*T/4*a

    WL6Alan.append(b)
WL6Alan_PDS=pd.Series(WL6Alan)





alanlar = pd.concat([WL1Alan_PDS, WL2Alan_PDS, WL3Alan_PDS, WL4Alan_PDS, WL5Alan_PDS, WL6Alan_PDS], axis=1)
alanlar.columns = ['WL1Alan_PDS', 'WL2Alan_PDS', 'WL3Alan_PDS', 'WL4Alan_PDS', 'WL5Alan_PDS', 'WL6Alan_PDS']

def moment_kolu():
    MK = list(range(-(len(yeni_df)-1)// 2, 0))  + list(range((len(yeni_df)+1)//2))
    MK=pd.Series(MK)
    return MK

WL6_Moment=WL6Alan_PDS*moment_kolu()
WL5_Moment=WL5Alan_PDS*moment_kolu()
WL4_Moment=WL4Alan_PDS*moment_kolu()
WL3_Moment=WL3Alan_PDS*moment_kolu()
WL2_Moment=WL2Alan_PDS*moment_kolu()
WL1_Moment=WL1Alan_PDS*moment_kolu()
momentler = pd.concat([WL1_Moment, WL2_Moment, WL3_Moment, WL4_Moment, WL5_Moment, WL6_Moment], axis=1)
momentler.columns = ['WL1_Moment', 'WL2_Moment', 'WL3_Moment', 'WL4_Moment', 'WL5_Moment', 'WL6_Moment']



def YG(T=2*D/3):
    yari_genislik=[]
    for i in range(len(yeni_df)):
        y_yi = pd.DataFrame(yeni_df.loc[i,"WL0":])
        yi=y_yi.values.flatten()
        wl = np.array([0,0.5,1,2,3,4,5,6])
        curve = np.polyfit(wl,yi, 2)
        yarigenislik = np.poly1d(curve)
        yari_genislik.append(yarigenislik(T))
    yari_genislik=pd.Series(yari_genislik)
    return yari_genislik



def Alan(T=2*D/3):
    T_A_list = []
    for i in range(len(alanlar)):
        ypd = pd.DataFrame(alanlar.loc[i])
        y=ypd.values.flatten()
        x = np.array([1,2,3,4,5,6])
        curve = np.polyfit(x, y, 2)
        coef = np.poly1d(curve)
        T_A_list.append(coef(T))
    T_A_list=pd.Series(T_A_list)
    return T_A_list

def moment(T=2*D/6):
    T_M_list = []
    for i in range(len(momentler)):
        ypd = pd.DataFrame(momentler.loc[i])
        y=ypd.values.flatten()
        x = np.array([1,2,3,4,5,6])
        curve = np.polyfit(x, y, 2)
        coef = np.poly1d(curve)
        T_M_list.append(coef(T))
    T_M_list=pd.Series(T_M_list)
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


def Bwl():
    Bwl=max(YG()*2)
    return Bwl

def carpim1():
    carpim1=Alan()*SM_creator(Alan())
    return carpim1
def carpim2():
    carpim2=moment_kolu()*carpim1()
    return carpim2
def carpim3():
    carpim3=moment()*SM_creator(moment())
    return carpim3
def carpim4():
    carpim4=SM_creator(yeni_df)*YG(T)
    carpim4=pd.Series(carpim4)
    return carpim4
def carpim5():
    carpim5=moment_kolu()*carpim4()
    carpim5=pd.Series(carpim5)
    return carpim5
def carpim6():
    carpim6=moment_kolu()*carpim5()
    return carpim6
def carpim7():
    carpim7=YG()**3*SM_creator(yeni_df)
    return carpim7




def DV(s=0.5):
    DV=1/3*s*sum(carpim1())
    return DV

def DW(s=0.5):
    DW=DV()*1.025
    return DW
def LCB(s=0.5):
    LCB=s*sum(carpim2())/sum(carpim1())
    return LCB
def KB():
    KB=sum(carpim3())/sum(carpim1())
    return KB
def CB(T=2*D/3):
    CB=DV()/(L*Bwl()*T)
    return CB
def CM(T=2*D/3):
    CM=Alan().max()/(Bwl()*T)
    return CM
def CP():
    CP=CB()/CM()
    return CP







def LCF(s=0.5):
    LCF=s*sum(carpim5())/sum(carpim4())
    return LCF

def CWP():
    CWP=AWP()/(Bwl()*L)
    return CWP
def AWP(s=0.5):
    AWP=2/3*s*sum(carpim4())
    return AWP
def TPC(ro=1.025):
    TPC=AWP()/100*ro
    return TPC
def ix(s=0.5):
    ix=2/9*s*sum(carpim7())
    return ix

def BM():
    BM=ix()/DV()
    return BM

def i0(s=0.5):
    i0=2/3*s**3*sum(carpim6())
    return i0

def i_f(s=0.5):
    i_f=i0()-AWP()*LCF()**2
    return i_f

def BML(s=0.5):
    BML=i_f()/DV()
    return BML

def MT1():
    MT1=DW()*BML()/L
    return MT1


print("dv",DV())
print("dw",DW())
print("lcb",LCB())
print("kb",KB())
print("cb",CB())
print("CM",CM())
print("CP",CP())
print("i_f",i_f())
print("i0",i0())
print("ix",ix())
print("BM",BM())
print("LCF",LCF())
print("BML",BML())
print("MT1",MT1())
print("TPC",TPC())
print("AWP",AWP())
print("CWP",CWP())





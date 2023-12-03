
import main_particulars
from main_particulars import *
import math
fs = int(input("Please select one of the numbers 1 or 2 to choose framing system (1 = transverse framing, 2 = longitudinal framing): "))
RSA=int(input("Estimated restricted service area? (answers must be one of (200,50,20,2,1) or 1)unlimited service area,2)sheltered water service "))
ReH=int(input(" What is the yield strength of your material (N/mm^2) \
                (Note: please write 235 if your material is normal strength hull structural steel ): "))
part=input("which part of ship length you are checking over? \
[1, shell plating, weather deck] [2, frames, deck beam] [3, web frame, stringer] ")
x=int(input(" which part of the ship do you want to process? \
(enter a value in meters, from the stern to the bow) ")) # m

wave_type=int(input(" please tab 1,2 or 3 for the wave type  \
( 1 = heading waves , 2 = side waves 3= doesnt matter ): "))
G = int(input("mass of cargo in the hold [t] ? NOTE:if you dont know please press 0"))
V = int(input("volume of the hold [m³] (hatchways excluded)? NOTE:if you dont know please press 0 "))
vessel_type=int(input("what type vessel ? (select 1 or 2)  1-dry cargo 2-tanker "))
PCq = int(input("What is the static cargo load? (if you dont know it exactly, please press 0): "))


################## bu kısım centre girderdan alındı ################ sonradan çekecek şekilde ayarlayıp sil
lcg=B
hcg=350 + 45*lcg   #mm
if hcg<600:
    hcg=600
ha=(hcg+99)//100*100
hdb=(ha / 1000)
#######################################################################################
hc=D - hdb # inner bottomdan alındı ####################################################

loc=x/L

def round_t(a):
    decimal = a - int(a)
    if decimal < 0.5:
        if decimal!=0:
            return int(a) + 0.5
    else:
        return int(a) + 1
class coefficients():
    def calculate_CRW(self,RSA):
        if RSA == 200:
            CRW = 0.9
        elif RSA == 50:
            CRW = 0.75
        elif RSA == 20:
            CRW = 0.66
        else:
            CRW = 1
        return CRW

    def calculate_CL(self,L):
        if L < 90:
            CL = math.sqrt(L / 90)
        else:
            CL = 1
        return CL

    def calculate_C0(self, L):
        CRW=coefficients().calculate_CRW(RSA)
        if 90 < L <= 300:
            C0 = (10.75 -((300 - L) / 100) ** 1.5) * CRW
        elif L < 90:
            C0 = ((L / 25) + 4.1) * CRW
        else:
            C0 = 10.75 * CRW
        return C0

    def calculate_CF(self,loc,CB):
        if loc < 0.2:
            CF = 1 + 5 / CB * (0.2 - loc)
        elif 0.2 <= loc <= 0.7:
            CF = 1
        elif loc < 0.7:
            CF = 1 + 20 / CB * (loc - 0.7) ** 2
        else:
            CF = 1
        return CF

    def calculate_CD(self,loc):
        if loc < 0.2:
            CD = 1.2 - loc
        elif 0.2 <= loc <= 0.7:
            CD = 1
        elif loc < 0.7:
            c = 0.15 * L - 10
            CD = 1 + c / 3 * (loc - 0.7)
        else:
            CD = 1
        return CD
    def calculate_CRS(self,RSA):
        if RSA == 200:
            CRS = 0.95
        elif RSA == 50:
            CRS = 0.85
        elif RSA == 20:
            CRS = 0.80
        elif RSA==2:
            CRS=0.75
        else:
            CRS = 1
        return CRS



class stress_calculations():
    XL = 0
    def calculate_ZLB(self,L):  # bottom plating
        k=other_coefficients().calculate_k(ReH)
        if L < 90:
            ZLB = 12.6 * math.sqrt(L) / k
        else:
            ZLB = 120 / k
        return ZLB

    def calculate_Zperm(self):
        if L < 90:
            Zperm = (0.8 + L / 450) * 230 / k
        else:
            Zperm = 230 / k
        return Zperm

    def calculate_ZPL(self):  # bottom plating
        XL = 0
        Zperm=stress_calculations().calculate_Zperm()
        ZPL = math.sqrt(Zperm ** 2 - 3 * XL ** 2) - 0.89 * ZLB
        return ZPL

    def calculate_ZLS(self,ZLB):
        ZLS = 0.76 * ZLB  # N/mm^2
        return ZLS

    def calculate_ZPL_SP(self,ZLS): # SHELL PLATİNG İÇİN ZPL
        XL =55 / k
        ZPL_SP = math.sqrt(Zperm**2 - 3 * XL ** 2) - 0.89 * ZLS
        return ZPL_SP

    def calculate_ZPLmax(self):   # SHELL PLATİNG
        XL =55 / k
        ZPLmax = math.sqrt((230 / k) ** 2 - 3 * XL ** 2) - 0.89 * ZLS
        return ZPLmax


class other_coefficients():
    def calculate_f(self,part): # hangi part olduğunu düzenleyeceksin side girder vs ekleyeceksin
        ftypouter = ["1", "shell plating", "weather deck"]
        ftypssm = ["2", "frame", "deck beam"]
        ftypgirder = ["3", "web frame", "stringer"]

        if part in ftypgirder:
            f = 0.6
        elif part in ftypouter:
            f = 1
        elif part in ftypssm:
            f = 0.75
        else:
            f = 1
        return f
    def calculate_k(self,ReH):
        k=1
        if ReH < 235:
            k = 235 / ReH
        elif ReH >= 235:
            k = 295 / (ReH + 60)
        return k

    def calculate_nf(self, fs):  # Note the 'self' parameter here
        if fs == 1:
            nf = 1
        elif fs == 2:
            nf = 0.83
        else:
            nf = 1
        return nf

    def calculate_GV(self,G, V):
        if G == 0 or V == 0:
            x = 0.7
        else:
            x = G / V
        return x

    def calculate_F(self):
        F = 0.11 * V0 / math.sqrt(L)
        return F

    def calculate_m(self):
        F = other_coefficients().calculate_F()
        m0 = 1.5 + F
        if loc < 0.2:
            m = m0 - 5 * (m0 - 1) * loc
        elif 0.2 <= loc <= 0.7:
            m = 1
        elif loc < 0.7:
            m = 1 + (m0 + 1) / 0.3 * (loc / 0.7)
        else:
            m = 1
        return m

    def calculate_av(self):
        F=other_coefficients().calculate_F()
        m = other_coefficients().calculate_m()
        return F * m


    def calculate_ma(self,l): #3.A.4 #MAİN FRAME HESABINDA 9.A.2.1
        l=3 # bunu kesin öğren
        ma=00.204*a/l*(4-(a/l)**2)
        return ma

    def calculate_c(self): #MAİN FRAME HESABINDA 9.A.2.1
        lKu,lKo=0,0   # if no brackets used c = 1
        l=1            # bu l v lKlara bak
        c=1-(lKu/l+0.4*lKo/l)
        if c<0.6:
            c=0.6
        return c

    def calculate_cr(self): #MAİN FRAME HESABINDA 9.A.2.1
        s,l=0,3           # buna da bi bak , for wall sided ships , there is no curvature s/l=0
        cr=1-2*s/l
        if cr<0.75:
            cr=0.75
        return cr
    def calculate_n(self):   #MAİN FRAME HESABINDA 9.A.2.1
        if L<100:
            n=0.9-0.0035*L
        else:
            n=0.55
        return n






class pressure():

    CB = main_particulars.CB
    T = main_particulars.T
    CL = coefficients().calculate_CL(L)
    f=other_coefficients().calculate_f(ReH)
    CO=coefficients().calculate_C0(L)
    CF = coefficients().calculate_CF(loc, CB)

    def calculate_P0(self):
        P0 = 2.1 * (CB + 0.7) * C0 * CL * f
        return P0

    def calculate_P01(self):
        P01 = 2.6 * (CB + 0.7) * CL * C0
        return P01
    def calculate_PS(self,z):
        x = (10 * (T - z) + P0 * CF * (1 + z / T))  # kN/m^2
        return x

    def calculate_PS1(self,z,y):
        x = (10 * (T - z) + P01*(1 + z / T * (2 - z / T)) * 2 * abs(y) / B)
        return x

    def calculate_PB(self):
        x= (10 * T + P0 * CF)
        return x

    def calculate_Pi(self):
        GV=other_coefficients().calculate_GV(G,V)
        return 9.81 * GV * hc * (1 + av)

    def calculate_P_inner(self):
        if vessel_type == 1:
            Pi=pressure().calculate_Pi()
            Pd = 10 * (T - hdb)  # p damaged
            if Pi >= Pd:
                Pinner = Pi  # P cargo
            else:
                Pinner = Pd
        elif vessel_type == 2:
            Pd = 10 * (T - hdb)
            h2 = hc +1 # bu +1 firar borusu yüzünden konuldu
            P2 = 9.81 * h2
            # P1=1   # bunun hesabı haddinden fazla karışık
            if P2 >= Pd:
                Pinner = P2
            else:
                Pinner = Pd
        return Pinner

    def calculate_PD(self,z,H):  #SHEER STRAKE HESABINDA
        PD1 = P0 * (20 * T) / ((10 + z - T) * H) * CD  # kN/m^2
        PDmin1 = 16 * f
        PDmin2 = 0.7 * P0
        PDlist = [PD1, PDmin1, PDmin2]
        PD = max(PDlist)
        return PD

    # PC static cargo load [kN/m2]  MİN 15  OLACAK
    def calculate_PC(self,PC):
        PC = int(input("What is the static cargo load? (if you dont know it exactly, please press 0): "))
        if PC == 0:
            h = int(input("What is the height of the tween decks? (if you dont know it exactly, please press 0):"))
            PC = 7 * h
            if h == 0:
                PC = 15
        if PC < 15:
            PC = 15
        return PC

    def calculate_PL(self):
        PL = PC * (1 + av)  # PL Load on cargo decks [kN/m2]
        return PL

    def calculate_Pe(self): # main frames hesabında
        pass                 # aşırı karmaşık eklersin p ya ps ya da pe ye eşit olacak sen ps ye eşitledin şimdilik


nf = other_coefficients().calculate_nf(fs)  # Pass 'fs' when calling the method
print("nf",nf)
CRW=coefficients().calculate_CRW(RSA)
print("CRW",CRW)
k=other_coefficients().calculate_k(ReH)
print("k",k)
C0=coefficients().calculate_C0(L)
print("C0",C0)
f=other_coefficients().calculate_f(part)
print("f",f)
CL=coefficients().calculate_CL(L)
print("CL",CL)
CF=coefficients().calculate_CF(loc,CB)
print("CF",CF)
CD=coefficients().calculate_CD(loc)
print("CD",CD)
CRS=coefficients().calculate_CRS(RSA)
print(CRS)
ZLB=stress_calculations().calculate_ZLB(L)
print("ZLB",ZLB)
P0=pressure().calculate_P0()
print("P0",P0)
P01=pressure().calculate_P01()
print("P01",P01)

"""PS1=pressure().calculate_PS1()
print("PS1",PS1)
PS=pressure().calculate_PS()
print("PS",PS)"""
PB=pressure().calculate_PB()
print("PB",PB)
ZPL=stress_calculations().calculate_ZPL()
print("ZPL",ZPL)
Zperm=stress_calculations().calculate_Zperm()
print("Zperm",Zperm)
ZLS = stress_calculations().calculate_ZLS(ZLB)
print("ZLS",ZLS)
ZPL_SP=stress_calculations().calculate_ZPL_SP(ZLS)
print("ZPL_SP",ZPL_SP)
ZPLmax=stress_calculations().calculate_ZPLmax()
print("ZPLmax",ZPLmax)
GV = other_coefficients().calculate_GV(G, V)
print("GV",GV)
av=other_coefficients().calculate_av()
print("av",av)
m=other_coefficients().calculate_m()
print("m",m)
F=other_coefficients().calculate_F()
print("F",F)
Pi=pressure().calculate_Pi()
print("Pi",Pi)
Pinner=pressure().calculate_P_inner()
print("P_inner", Pinner)
"""PD=pressure().calculate_PD()
print("PD",PD)"""
PC=pressure().calculate_PC(PCq)
print("PC",PC)
PL=pressure().calculate_PL()
print("PL",PL)
ma=other_coefficients().calculate_ma(l=3)
print("ma",ma)
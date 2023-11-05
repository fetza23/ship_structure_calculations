import math
from main_particulars import *
ReH=int(input(" What is the yield strength of your material (N/mm^2) \
                (Note: please write 235 if your material is normal strength hull structural steel ): "))
fs = int(input(" please select one of the numbers 1 or 2 to choose framing system \
             ( 1 = transverse framing , 2 = longitudinal framing): "))
RSA=int(input("Estimated restricted service area? (answers must be one of (200,50,20) "))

part=input("which part of ship length you are checking over?  ")

wave_type=int(input(" please tab 1,2 or 3 for the wave type  \
( 1 = heading waves , 2 = side waves 3= doesnt matter ): "))

x=int(input(" which part of the ship do you want to process? \
(enter a value in meters, from the stern to the bow) ")) # m
loc=x/L





class calculation_of_nf():
    def __init__(self, fs):
        self.fs = fs
        self.nfvalue = self.calculate_nf()

    def calculate_nf(self):
        if self.fs == 1:
            nf = 1
        elif self.fs == 2:
            nf = 0.83
        else:
            nf = None  # Handle other values of fs as needed
        return nf

nf=calculation_of_nf(fs).nfvalue


class calculation_of_CRW():
    def __init__(self, RSA):
        self.RSA = RSA
        self.CRWvalue = self.calculate_CRW()

    def calculate_CRW(self):
        if self.RSA == 200:
            CRW = 0.9
        elif self.RSA == 50:
            CRW = 0.75
        elif self.RSA == 20:
            CRW = 0.66
        else:
            CRW = 1
        return CRW

CRW=calculation_of_CRW(RSA).CRWvalue

class calculation_of_k():
    def __init__(self,ReH):
        self.ReH=ReH
        self.kValue=self.calculate_k()
    def calculate_k(self):
        if self.ReH<235:
            k=235/self.ReH
        elif self.ReH>=235:
            k=295/(self.ReH+60)
        return k
k=calculation_of_k(ReH).kValue




class calculation_of_C0():
    def __init__(self, CRW):
        self.CRW = CRW

    def C0(self, L):
        if 90 < L <= 300:
            C0 = (10.75 -((300 - L) / 100) ** 1.5) * self.CRW
        elif L < 90:
            C0 = ((L / 25) + 4.1) * self.CRW
        else:
            C0 = 10.75 * self.CRW
        return C0
C0=calculation_of_C0(CRW).C0(L)


def f_calculator():
    ftypouter=["1","shell plating","weather deck"]
    ftypssm=["2","frame","deck beam"]
    ftypgirder=["3","web frame","stringer"]

    if part in ftypgirder:
        f=0.6
    elif part in ftypouter:
        f=1
    elif part in ftypssm:
        f=0.75
    else:
        f=1
    return f
f=f_calculator()


def CL_calculator():
    if L<90:
        CL=math.sqrt(L/90)
    else:
        CL=1
    return CL
CL=CL_calculator()


def CF_calculator():
    if loc<0.2:
        CF=1+5/CB*(0.2-loc)
    elif 0.2 <=loc <=0.7:
        CF=1
    elif loc<0.7:
        CF=1+20/CB*(loc-0.7)**2
    else:
        CF=1
    return CF
CF=CF_calculator()

def CD_calculator():
    if loc<0.2:
        CD=1.2-loc
    elif 0.2 <=loc <=0.7:
        CD=1
    elif loc<0.7:
        c=0.15*L-10
        CD=1+c/3*(loc-0.7)
    else:
        CD=1
    return CD
CD=CD_calculator()
def Zperm_calculator():
    if L<90:
        Zperm=(0.8+L/450)*230/k
    else:
        Zperm=230/k
    return Zperm
Zperm=Zperm_calculator()

def ZLB_calculator():
    if L<90:
        ZLB=12.6*math.sqrt(L)/k
    else:
        ZLB=120/k
    return ZLB
ZLB=ZLB_calculator()

XL=0

def ZPL_calculator():
    ZPL=math.sqrt(Zperm**2-3*XL**2)-0.89*ZLB
    return ZPL
ZPL=ZPL_calculator()
print(ZPL)





def P0_calculator():
    if wave_type == 1:
        P0 = 2.1 * (CB + 0.7) * C0 * CL * f
    elif wave_type == 2:
        P0 = 2.6 * (CB + 0.7) * CL * C0
    else:
        P0 = 2.1 * (CB + 0.7) * C0 * CL * f
    return P0
P0=P0_calculator()
print("P0",P0)

PB=10*T+P0*CF


print("ZLB",ZLB)
print("ZPL",ZPL)
print("Zperm",Zperm)
print("CD",CD)
print("CF",CF)

print("C0",C0)
print("crw",CRW)
print("k",k)
print("nf",nf)
print("f", f)

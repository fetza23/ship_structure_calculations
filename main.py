import main_particulars
from main_particulars import *
import math
fs = int(input("Please select one of the numbers 1 or 2 to choose framing system (1 = transverse framing, 2 = longitudinal framing): "))
RSA=int(input("Estimated restricted service area? (answers must be one of (200,50,20) "))
ReH=int(input(" What is the yield strength of your material (N/mm^2) \
                (Note: please write 235 if your material is normal strength hull structural steel ): "))
part=input("which part of ship length you are checking over?  ")
x=int(input(" which part of the ship do you want to process? \
(enter a value in meters, from the stern to the bow) ")) # m

wave_type=int(input(" please tab 1,2 or 3 for the wave type  \
( 1 = heading waves , 2 = side waves 3= doesnt matter ): "))




loc=x/L
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


class stress_calculations():
    def calculate_ZLB(self,L):
        k=other_coefficients().calculate_k(ReH)
        if L < 90:
            ZLB = 12.6 * math.sqrt(L) / k
        else:
            ZLB = 120 / k
        return ZLB

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
            nf = None  # Handle other values of fs as needed
        return nf





class pressure():

    CB = main_particulars.CB
    T = main_particulars.T
    CL = coefficients().calculate_CL(L)
    f=other_coefficients().calculate_f(ReH)
    CO=coefficients().calculate_C0(L)
    CF = coefficients().calculate_CF(loc, CB)

    def calculate_P0(self):
        if wave_type == 1:
            P0 = 2.1 * (CB + 0.7) * C0 * CL * f
        elif wave_type == 2:
            P0 = 2.6 * (CB + 0.7) * CL * C0
        else:
            P0 = 2.1 * (CB + 0.7) * C0 * CL * f
        return P0

    def calculate_P01(self):
        if fs == 1:
            P01 = 2.1 * (CB + 0.7) * C0 * CL * f
        else:
            P01 = 1  # sallama
        return P01

    def calculate_PS(self):
        z = main_particulars.B / 2 + main_particulars.a / 2   # side shell plating için olan z
        x = (10 * (T - z) + P0 * CF * (1 + z / T))  # kN/m^2
        return x

    def calculate_PS1(self):
        y=main_particulars.B/2
        z = main_particulars.B / 2 + main_particulars.a / 2   # side shell plating için olan z
        x = (10 * (T - z) + P01*(1 + z / T * (2 - z / T)) * 2 * abs(y) / B)
        return x

    def calculate_PB(self):
        x= (10 * T + P0 * CF)
        return x

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
ZLB=stress_calculations().calculate_ZLB(L)
print("ZLB",ZLB)
P0=pressure().calculate_P0()
print("P0",P0)
P01=pressure().calculate_P01()
print("P01",P01)
PS1=pressure().calculate_PS1()
print("PS1",PS1)
PS=pressure().calculate_PS()
print("PS",PS)
PB=pressure().calculate_PB()
print("PB",PB)

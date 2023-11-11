from coefficient_calculations import *
from main_particulars import *

def bB_calculator():
    bB=800+5*L
    return bB
bB=bB_calculator()
print(f"bottom plating breadth bB: {bB} ")

def tB_calculator():
    if L >= 90:
        ttB1 = 18.3 * nf * a * math.sqrt(PB / ZPL)
        if ttB1 <= 10:
            tK1 = 1.5
        else:
            tK1 = 0.1 * ttB1 / math.sqrt(k)
            if tK1 > 3:
                tK1 = 3
        tB1 = 18.3 * nf * a * math.sqrt(PB / ZPL) + tK1  # mm
        ttB2 = 1.21 * a * math.sqrt(PB * k)
        if ttB2 <= 10:
            tK2 = 1.5
        else:
            tK2 = 0.1 * ttB1 / math.sqrt(k)
            if tK2 > 3:
                tK2 = 3
        tB2 = 1.21 * a * math.sqrt(PB * k) + tK2
        if tB1 <= tB2:
            tB = tB2
        else:
            tB = tB1
    if L < 90:
        ttB1 = 1.9 * nf * a * math.sqrt(PB * k)
        if ttB1 <= 10:
            tk = 1.5
        else:
            tk = 0.1 * ttB1 / math.sqrt(k)
            if tk > 3:
                tk = 3
        tB = 1.9 * nf * a * math.sqrt(PB * k) + tk
    return tB
tB1=tB_calculator()
tB=round_t(tB1)
print(f"bottom plating thickness tB: {tB} ")

def calculate_tFPK():
    tFPK = tB + 2  # mm
    tFKGL = math.sqrt(L * k)
    if L >= 50:
        if tFPK <=tFKGL:
            tFPK=tFKGL
    return tFPK

tFPK1=calculate_tFPK()
tFPK=round_t(tFPK1)
print(f"flat plate keel thickness tFK {tFPK}")



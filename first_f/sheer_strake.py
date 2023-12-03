from shell_plating import *
from coefficient_calculations import *
from main_particulars import *
# The width of the sheerstrake is not to be lessthan:
b = 800 + 5 * L  # mm


# The thickness of strength deck plating tE
def calculate_tD():
    tFKGL = math.sqrt(L * k)  # bu normalde el kodunda var  sonradan anla diye burada
    ttE1 = 1.21 * a * math.sqrt(PD * k)
    if ttE1 <= 10:
        tKss = 1.5
    else:
        tKss = 0.1 * ttE1 / math.sqrt(k)
        if tKss > 3:
            tKss = 3
    tE1 = 1.21 * a * math.sqrt(PD * k) + tKss

    ttE2 = 1.1 * a * math.sqrt(PL * k)
    if ttE2 <= 10:
        tKss = 1.5
    else:
        tKss = 0.1 * ttE2 / math.sqrt(k)
        if tKss > 3:
            tKss = 3

    tE2 = 1.1 * a * math.sqrt(PL * k) + tKss

    tEmin = (5.5 + 0.02 * L) * math.sqrt(k)
    tmin = (4.5 * 0.05 * L) * math.sqrt(k)
    tlist = [tE1, tE2, tEmin, tmin]
    tD = max(tlist)
    if tD < tFKGL:
        tD = tFKGL
    return tD

tD=calculate_tD()
# The thickness of the sheerstrake shall,
t = 0.5 * (tD + ts)  # ts= side shell    # tD=required thickness of strength deck
if t < ts:
    t = ts
print("sheer strake ts",t)





"""
# SHEER STRAKE
# The width of the sheerstrake is not to be lessthan:
b=800+5*L  #mm
# The thickness of the sheerstrake shall,
t=0.5*(tD+ts)      # ts= side shell    # tD=required thickness of strength deck
if t<ts:
    t=ts
YUKARIDA DA YAZDIN BU KISMI SONNRA DÜZENLERSİN"""
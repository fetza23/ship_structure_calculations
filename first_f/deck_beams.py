
from coefficient_calculations import *

# TRANSVERSE FRAMİNG SYSTEM


def calculate_Wd():
    l=B/4 # 3 tane girder olsun dedik , sayı neye göre bi bak
    P=max(PL,PD)
    mk=1 # with no brackets assuption as a first approximation , hesabı baya zorlu
    m=mk**2-ma**2
    c=0.75  # for beams,girders and transverses simply supported on one or both ends , bi tane değeri de c=0.55 ama nedeni yok
    Wd=m*c*a*P*l**2*k
    return Wd
Wd=calculate_Wd()
print("Wd",Wd)
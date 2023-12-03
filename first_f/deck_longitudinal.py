from coefficient_calculations import *

############# FOR longitudinal framing system ###############

ZLB=120 # as a firs approximation
ZLD=ZLB*((D-0.4*D)/(0.4*D))
ZL=ZLD
Zpr=Zperm-abs(ZL)
mk=1 # with no brackets assuption as a first approximation , hesabı baya zorlu
m=mk**2-ma**2
l=e
P=PD
def calculate_Wl_dl():
    Wl_dl=(83/Zpr)*m*a*l**2*P
    return Wl_dl
Wl_dl=calculate_Wl_dl()
print(Wl_dl)



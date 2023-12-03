from coefficient_calculations import *
P=Pinner
ZL=ZLB*((0.4*D-hdb)/(0.4*D))
Zpr=Zperm-abs(ZL)
l=e
def calculate_Wl_ibl():
    Wl=83/Zpr*m*a*l**2*e*P
    return Wl
Wl_ibl=calculate_Wl_ibl()

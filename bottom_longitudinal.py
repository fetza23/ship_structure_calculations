from coefficient_calculations import *
P=PB
ZL=ZLB*((0.4*D-hdb)/(0.4*D))
Zpr=Zperm-abs(ZL)
l=e
mk=1 # we assumed that there are no brackets
m=mk**2-ma**2
def calculate_Wl_bl():
    Wl_bl=83/Zpr*m*a*l**2*P
    return Wl_bl
Wl_bl=calculate_Wl_bl()
print("Wl_bl",Wl_bl)
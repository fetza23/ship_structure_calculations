from coefficient_calculations import *
l=D-hdb
nc=0.3  # cross tie sayısına bağlı olarak değişiyor


def calculate_PS_wf():
    z = hdb + l / 2
    x = (10 * (T - z) + P0 * CF * (1 + z / T))  # kN/m^2
    return x
PS_wf=calculate_PS_wf()
P=PS_wf
def calculate_Wr_wf():
    Wr_wf=0.55*e*l**2*P*nc*k
    return Wr_wf
Wr_wf=calculate_Wr_wf()
print("Wr_wf",Wr_wf)

# TRİAL ERROR METHOD
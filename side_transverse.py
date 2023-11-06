from coefficient_calculations import *
l=D-hdb
nc=0.3  # cross tie sayısına bağlı olarak değişiyor


def calculate_PS_st(): #BURADAKİ İLE WEB FRAMEDEKİ PS_WF AYNI BUNLARI BİREŞTİRİRSİN
    z = hdb + l / 2
    x = (10 * (T - z) + P0 * CF * (1 + z / T))  # kN/m^2
    return x
PS_st=calculate_PS_st()
P=PS_st
def calculate_Wr_st():
    Wr_st=0.55*e*l**2*P*nc*k
    return Wr_st
Wr_st=calculate_Wr_st()
print("Wr_st",Wr_st)
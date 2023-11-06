from coefficient_calculations import *
l=14.4  #we assumed it 14.4 = the distance between transverse bulkheads
nc=0.2  # cross tie sayısına bağlı olarak değişiyor


def calculate_PS_ss():
    z = hdb + 3  # ilk side girder ın dibden yüksekliği
    x = (10 * (T - z) + P0 * CF * (1 + z / T))  # kN/m^2
    return x
PS_wf=calculate_PS_ss()
P=PS_wf
def calculate_Wr_ss():
    e=3/2+2.5/2  # buna bi bak anlaşılmadı
    Wr_ss=0.55*e*l**2*P*nc*k
    return Wr_ss
Wr_ss=calculate_Wr_ss()
print("Wr_ss",Wr_ss)
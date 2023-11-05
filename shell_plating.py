from coefficient_calculations import *
from main_particulars import *
# BURDAKİ P LERİN KULLANIMINA BAK ÖDEVDEKİ GİBİ YAPTIN AMA DEĞİŞTİR
def ts_calculator():
    if L < 90:
        ts = 1.9 * nf * a * math.sqrt(PS * k) + k
        if L < 50:  # last check for min
            ts1 = (1.5 - 0.01 * L) * math.sqrt(L * k)
            if ts <= ts1:
                ts = ts1
        else:
            ts1 = math.sqrt(L * k)
            if ts <= ts1:
                ts = ts1

    elif L >= 90:
        ttS1 = 18.3 * nf * a * math.sqrt(PS / ZPL_SP)
        if ttS1 <= 10:
            tKs1 = 1.5
        else:
            tKs1 = 0.1 * ttS1 / math.sqrt(k)
            if tKs1 > 3:
                tKs1 = 3
        ts1 = 18.3 * nf * a * math.sqrt(PS / ZPL_SP) + tKs1
        P=PS # 4.B.2 DEN P YA PS YE YA DA PE YE EŞİT OLACAK FALAN DİYOR ONU AYARLA
        ttS2 = 1.21 * a * math.sqrt(P * k)
        if ttS2 <= 10:
            tKs2 = 1.5
        else:
            tKs2 = 0.1 * ttS2 / math.sqrt(k)
            if tKs2 > 3:
                tKs2 = 3
        ts2 = 1.21 * a * math.sqrt(P * k) + tKs2

        ttS3 = 18.3 * nf * a * math.sqrt(PS1 / (ZPLmax))
        if ttS3 <= 10:
            tKs3 = 1.5
        else:
            tKs3 = 0.1 * ttS3 / math.sqrt(k)
            if tKs3 > 3:
                tKs3 = 3
        ts3 = 18.3 * nf * a * math.sqrt(PS1 / (ZPLmax)) + tKs3
        tslist = [ts1, ts2, ts3]
        ts = max(tslist)
        ts11 = math.sqrt(L * k)  # last check for min
        if ts11 > ts:
            ts = ts11
    return ts
ts=ts_calculator()
print("SHELL PLATİNG ts",ts)




"""
 ZPL = math.sqrt(Zperm - 3 * XL ** 2) - 0.89 * ZLS
    ZPLmax = math.sqrt((230 / k) ** 2 - 3 * XL ** 2) - 0.89 * ZLS


XL = 55 / k  # N/mm^2
PS = 10 * (T - z) - P0 * CF * (1 + z / T)  # kN/m^2
PS1 = 10 * (T - z) - P01(1 + z / T * (2 - z / T)) * 2 * abs(y) / B  # P0 ve p01 var zaten
"""
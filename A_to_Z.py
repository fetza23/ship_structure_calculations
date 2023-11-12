from coefficient_calculations import *
from main_particulars import *

def bB_calculator():
    bB=800+5*L
    return bB
bB=bB_calculator()
print(f" breadth of flat plate keel bB: {bB} ")
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

tFPK=calculate_tFPK()

print(f"flat plate keel thickness tFK {tFPK}")

#################################### CENTRE GİRDER ####################################

lcg=B
def hcg_calculator():
    hcg=350 + 45*lcg
    if hcg<600:
        hcg=600
    return hcg
hcg=hcg_calculator()
print(f"height of centre girder hcg : {hcg}")
ha=(hcg+99)//100*100
print(f"actual height of centre girder ha : {ha}")


def tmcg_calculator():
    if ha <=1200:
        tmcg=hcg/ha*((hcg/100)+1)*math.sqrt(k)
    else:
        tmcg=hcg/ha*((hcg/120)+3)*math.sqrt(k)
    tmincg=(5+0.03*L)*math.sqrt(k)
    if tmcg <= tmincg:
        tmcg=tmincg
    return tmcg
tmcg1=tmcg_calculator()
tmcg=round_t(tmcg1)
print("thickness of centre girder tmcg",tmcg)

#################################### SIDE GİRDER ###################################
# Arrangement of side girders #
def number_of_SG():
    if 0< B/2 <4.5:
        print("no need for side girders")
        locx1 = []
    elif 4.5 <= B/2 < 8:
        locx1 = [-B / 4, B / 4]
        print(" one side girder at each side")
    elif 8<= B/2 <= 10:
        locx1 = [-B / 3, -B / 6, B / 6, B / 3]
        print(f"two side girders at each side")

    elif B/2>10:
        print("three side girders at each side")
        locx1=[-3*B/8,-B/4,-B/8,B/8,B/4,3*B/8]
    locx = [round(num, 2) for num in locx1]
    return locx


loc_SG=number_of_SG()
print(f"the distance of side girders from centerline {loc_SG}")

def tsg_calculator():
    tsg=hcg**2/(120*ha)*math.sqrt(k)
    return tsg
tsg1=tsg_calculator()
tsg=round_t(tsg1)
print("the thickness of side girder tsg",tsg)


####################################  PLATE FLOORS  ###################################


def tpf_calculator(): # dolu döşek
    tpf = tmcg - 2 * math.sqrt(k)
    if tpf > 16:
        tpf = 16
    return tpf
tpf=tpf_calculator()
print(f"the thickness of plate floor tpf",tpf)


def manhole_calculator():
    LLq = input("is there any bulkhead in your ship? press 1 or 2     1) yes    2) no )")
    if LLq == "1":
        LL = int(input("what is the span between longitudinal bulkheads in meters?"))
    else:
        LL = B
    ymax = 0.4 * LL
    y_manhole = int(input(f"what is the distance between supporting point of the plate floor (ship's side, longitudinal bulkhead) in meters?\
note that The distance y is not to be taken greater than {ymax} : "))
    Ɛ = int(input("what kind of space you are checking for manhole? ( press 1 or 2 )\
1) for spaces which may be empty at full draught, e.g. machinery spaces, storerooms, etc.\
2) elsewhere "))
    if Ɛ == 1:
        Ɛ = 0.5
    else:
        Ɛ = 0.3
    Aw = Ɛ * T * LL * e * (1 - 2 * y_manhole / LL) * k

    rwsa = ha * tpf / 100
    Amh = rwsa - 40 * tpf / 10
    if Amh >= Aw:
        print("a man hole may be opened")
        mh=1
    else:
        print("you shouldnt open a man hole")
        mh=2
    return mh

        

manhole = input("Do you want to check if you want to open manholes? Press 1 or 2    1)yes   2)no) ")
if manhole == "1":
    man_hole=manhole_calculator()

####################################  BRACKETS  ###################################

def tBr_calculator():
    tBr=tpf
    return tBr
tBr=tBr_calculator()
print("The thickness of brackets tBr",tBr)
def bBr_calculator():
    bBr=0.75*hcg
    return bBr
bBr=bBr_calculator()
print("the breadth of brackets bBr",bBr)

####################################  INNER BOTTOM  ###################################

def tinner_calculator():
    P=Pinner
    ttinner = 1.1 * a * math.sqrt(P * k)
    if ttinner <= 10:
        tKinner = 1.5
    else:
        tKinner = 0.1 * ttinner / math.sqrt(k)
        if tKinner > 3:
            tKinner = 3

    return 1.1 * a * math.sqrt(P * k) + tKinner +2  # hoca ahşap kaplama yoksa +2 gibi bir şey dedi ona bi bakarsın sonra
tinner = round_t(tinner_calculator())
print("the thickenss of inner bottom tinner: ", tinner)
print("pinner",Pinner)

"""
##################### BRACKET FLOORS ##############################
if fs==1:
    pass

############################# BOTTOM LONG. ######################
if fs==2:
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
    
######################## İNNER BOTTOM LONG . #######################
if fs == 2:
    P = Pinner
    ZL = ZLB * ((0.4 * D - hdb) / (0.4 * D))
    Zpr = Zperm - abs(ZL)
    l = e
    def calculate_Wl_ibl():
        Wl = 83 / Zpr * m * a * l ** 2 * e * P
        return Wl
    Wl_ibl = calculate_Wl_ibl()

"""
########################### SHELL PLATİNG #########################

z=hdb+a/2
PS=pressure().calculate_PS(z)
PS1=pressure().calculate_PS1(z,B/2)
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
        ts1 = ttS1 + tKs1
        P=PS # 4.B.2 DEN P YA PS YE YA DA PE YE EŞİT OLACAK FALAN DİYOR ONU AYARLA
        ttS2 = 1.21 * a * math.sqrt(P * k)
        if ttS2 <= 10:
            tKs2 = 1.5
        else:
            tKs2 = 0.1 * ttS2 / math.sqrt(k)
            if tKs2 > 3:
                tKs2 = 3
        ts2 =ttS2+ tKs2

        ttS3 = 18.3 * nf * a * math.sqrt(PS1 / (ZPLmax))
        if ttS3 <= 10:
            tKs3 = 1.5
        else:
            tKs3 = 0.1 * ttS3 / math.sqrt(k)
            if tKs3 > 3:
                tKs3 = 3
        ts3 =ttS3 + tKs3
        tslist = [ts1, ts2, ts3]
        ts = max(tslist)
        ts11 = math.sqrt(L * k)
        if ts11 > ts:
            ts = ts11
        print(tslist)
    return ts
ts=ts_calculator()
print("the thickness of shell plate ts",ts)

##################### DECK PLATİNG  #####################

z = H = D
PD=pressure().calculate_PD(z,H)
def calculate_tD():
    tFKGL = math.sqrt(L * k)
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
    tmin = (4.5 + 0.05 * L) * math.sqrt(k)
    tcheck=math.sqrt(L*k)
    tlist = [tE1, tE2, tEmin, tmin,tcheck]
    tD = max(tlist)
    if tD < tFKGL:
        tD = tFKGL
    return tD

tD=calculate_tD()
print("thickness of deck plating tD: ",tD)

##################### SHEER STRAKE ######################
def calculate_bss():
    bss = 800 + 5 * L  # mm
    return bss
bss=calculate_bss()
print("breadth of sheer strake bss:", bss)
def calculate_tss():
    tss = 0.5 * (tD + ts)
    if tss < ts:
        tss = ts
    return tss
tss=calculate_tss()
print("thickness of sheer strake tss: ", tss)

##################### SIDE FRAMES ( HOLD FRAMES ) #####################
if fs==1:
    l = (D / 3)
    round_t(l)
    print("l",l)
    f=other_coefficients().calculate_f(2)
    n=other_coefficients().calculate_n()
    c=other_coefficients().calculate_c()
    cr=other_coefficients().calculate_cr()
    z=l/2
    PS = pressure().calculate_PS(z)

    def calculate_WRmf():
        WR=(1-ma**2)*n*c*a*l**2*PS*cr*k
        return WR
    WR=calculate_WRmf()
    print("side frame's WR",WR)

##################### SIDE LONGİTUDİNALS #####################
if fs==2:
    def calculate_ZL():
        ZL = ZLB * ((0.4 * D - hdb) / (0.4 * D))
        return ZL

    ZL = calculate_ZL()
    def calculate_Zpr():
        Zpr = Zperm - abs(ZL)
        return Zpr
    Zpr = calculate_Zpr()
    z = hdb + a
    PS = pressure().calculate_PS(z)
    def calculate_Wl_sl():
        l = e
        Wl_sl = 83 / Zpr * m * a * l ** 2 * PS
        return Wl_sl

    Wl_sl = calculate_Wl_sl()
    print(Wl_sl)
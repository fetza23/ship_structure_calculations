from coefficient_calculations import *
from main_particulars import *

def bB_calculator():
    bB=800+5*L
    return bB
bB=bB_calculator()
print(f"bottom plating breadth bB: {bB} ")
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

tFPK1=calculate_tFPK()
tFPK=round_t(tFPK1)
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
    print("Aw",Aw)

    rwsa = ha * tpf / 100
    print("RWSA",rwsa)
    Amh = rwsa - 40 * tpf / 10
    print("AMH",Amh)
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

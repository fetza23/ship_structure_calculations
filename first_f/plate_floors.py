from centre_girder import *
from coefficient_calculations import *
import math

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
    else:
        print("you shouldnt open a man hole")
    
        

manhole = input("Do you want to check if you want to open manholes? Press 1 or 2    1)yes   2)no) ")
if manhole == "1":
    man_hole=manhole_calculator()

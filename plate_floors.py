from centre_girder import *
from coefficient_calculations import *
import math

def tpf_calculator():
    tpf = tmcg - 2 * math.sqrt(k)
    if tpf > 16:
        tpf = 16
    return tpf
tpf=tpf_calculator()
print(tpf)


"""manhole = input("Do you want to open manholes? (yes or no) ")
if manhole in answerofdetail:
    LL = input("is there any bulkhead in your ship? (yes or no )")
    if LL in answerofdetail:
        LL = int(input("what is the span between longitudinal bulkheads in meters?"))
    else:
        LL = B
    ymax = 0.4 * LL
    y = int(input(f"what is the distance between supporting point of the plate floor (ship's side, longitudinal bulkhead) in meters?\
note that The distance y is not to be taken greater than {ymax} : "))
    Ɛ = int(input("what kind of space you are checking? ( press 1 or 2 )\
1) for spaces which may be empty at full draught, e.g. machinery spaces, storerooms, etc.\
2) elsewhere "))
    if Ɛ == 1:
        Ɛ = 0.5
    else:
        Ɛ = 0.3
    Aw = Ɛ * T * LL * e * (1 - 2 * y / LL) * k
    print(Aw)

    rwsa = ha * tpf / 100
    Amh = rwsa - 40 * tpf / 10
    if Amh >= Aw:
        print("a man hole may be opened")
    else:
        print("you shouldnt open a man hole")"""


from centre_girder import *
from plate_floors import *
def tB_calculator():
    tB=tpf
    return tB# The brackets are, in general, to be of same thickness as the plate floors.
tB=tB_calculator()
print(tB)
def bB_calculator():
    bB=0.75*hcg # the breadth is to be 0,75 of the depth of the centre girder
    return bB
bB=bB_calculator()
print(bB)
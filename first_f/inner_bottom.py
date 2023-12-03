from coefficient_calculations import *
import math
"""
G = int(input("mass of cargo in the hold [t] ? NOTE:if you dont know please press 0"))
V = int(input("volume of the hold [m³] (hatchways excluded)? NOTE:if you dont know please press 0 "))
vessel_type = int(input("what type vessel ? (select 1 or 2)  1-dry cargo 2-tanker "))"""
"""G=int(input("mass of cargo in the hold [t] ? NOTE:if you dont know please press 0"))
V=int(input("volume of the hold [m³] (hatchways excluded)? NOTE:if you dont know please press 0 "))
if G ==0:
    G=7
if V==0:             # G/V = 0.7 is min value
    V=10   


"""


def tKinner_calculator():
    P=Pinner
    ttinner = 1.1 * a * math.sqrt(P * k)
    print(ttinner)
    if ttinner <= 10:
        tKinner = 1.5
    else:
        tKinner = 0.1 * ttinner / math.sqrt(k)
        if tKinner > 3:
            tKinner = 3
    return tKinner


tKinner = tKinner_calculator()
print("TKİNNER", tKinner)


def tinner_calculator():
    P=Pinner
    return 1.1 * a * math.sqrt(P * k) + tKinner  # yuvarla standart thickness için


tinner = tinner_calculator()
print("TİNNER", tinner)


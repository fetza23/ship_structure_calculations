L = 100
LWL = 100
LBP = 98
B = 16
T = 6.5
D = H = 9
CB = 0.6
V0 = 16
a = 0.6
e = 2.4
"""V0=float(input("Maximum service speed [kn], which the ship is designed to maintain at the summer load line draught and\
at the propeller RPM corresponding to MCR (maximum continuous rating).   \
(press 5 if you do not know the speed in knots)"))     #ship's speed (kn)
if V0==0:
    V0=float(input("Maximum service speed [m/s]? "))
    ms_to_knot = 1.94384
    V0kn=V0*ms_to_knot
    V0=V0kn
if V0<math.sqrt(L):
    V0=math.sqrt(L)
    print("max service speed can not be taken less than √L ")



G=int(input("mass of cargo in the hold [t] ? NOTE:if you dont know please press 0"))
V=int(input("volume of the hold [m³] (hatchways excluded)? NOTE:if you dont know please press 0 "))
if G ==0:
    G=7
if V==0:             # G/V = 0.7 is min value
    V=10    

vessel_type=int(input("what type vessel ? (select 1 or 2)  1-dry cargo 2-tanker "))
"""
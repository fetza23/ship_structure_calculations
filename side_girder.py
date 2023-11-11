from centre_girder import *

# Arrangement of side girders #
def number_of_SG():
    if 0< B/2 <4.5:
        print("no need for side girders")
    elif 4.5 <= B/2 < 8:
        locx1 = [-B / 4, B / 4]
        print(" one side girder at each side")
        locx1=[-B/4,B/4]
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

from coefficient_calculations import *
lcg=B
hcg=350 + 45*lcg   #mm

if hcg<600:
    hcg=600
ha=(hcg+99)//100*100


def tmcg_calculator():
    if ha <=1200:
        tmcg=hcg/ha*((hcg/100)+1)*math.sqrt(k)
    else:
        tmcg=hcg/ha*((hcg/120)+3)*math.sqrt(k)
    tmincg=(5+0.03*L)*math.sqrt(k)
    if tmcg <= tmincg:
        tmcg=tmincg
    return tmcg
tmcg=tmcg_calculator()
print("thickness of centre girder tmcg",tmcg)
print("height of centre girder hcg",hcg)
print("actual height of centre girder ha",ha)

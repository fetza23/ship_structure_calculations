
from coefficient_calculations import *
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


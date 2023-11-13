from main_particulars import *
import matplotlib.pyplot as plt
import numpy as np
from A_to_Z import *
############### kabuk #####################
x = np.linspace(-B/2, B/2,1000)
y = [1]*(len(x))
y[0],y[-1]=9,9

plt.plot(x, y, color='green', linewidth=tFPK/5 , label="flat plate ") # /10 grafikte gözüksün diye
###########inner bottom ##################
y=[ha/1000 +1]*len(x)
plt.plot(x,y ,color="b", label="inner bottom")

############### centre girder ###################

y=np.linspace(1,ha/1000+1,1000)
x=[0]*len(y)
plt.plot(x,y,color="r",label="center girder",linewidth=tmcg/5)
plt.legend()
################ SIDE GIRDER ###################
if 4.5<=B/2:
    legend_added = False
    for i in loc_SG:
        y = np.linspace(1, ha / 1000 + 1, 1000)
        x = [i] * len(y)
        if not legend_added:
            plt.plot(x, y, color="k", label="side girder", linewidth=tsg / 5)
            legend_added = True
        else:
            plt.plot(x, y, color="k", linewidth=tsg / 5)

############### bracket floor ################
x = [0,bBr/1000 , bBr/1000, 0]
x1 =[0,-bBr/1000 , -bBr/1000, 0]
y = [ 1,1, ha/1000+1, ha/1000+1]
plt.plot(x1, y, label='bracket', color='y')
plt.plot(x, y, color='y')

x2=[B/2-bBr/1000 , B/2-bBr/1000, B/2]
x3=[-B/2+bBr/1000 , -B/2+bBr/1000, -B/2]
y = [1, ha/1000+1, ha/1000+1]
plt.plot(x2, y, color='y')
plt.plot(x3, y, color='y')

bracket_hole1 = plt.Circle((bBr/2000,ha/2000+1), 0.15,fill=False, color='y')
bracket_hole2 = plt.Circle((-bBr/2000,ha/2000+1), 0.15,fill=False, color='y')
bracket_hole3 = plt.Circle((B/2-bBr/1750,ha/2000+1), 0.15,fill=False, color='y')
bracket_hole4 = plt.Circle((-B/2+bBr/1750,ha/2000+1), 0.15,fill=False, color='y')
bracket_hole=[bracket_hole3,bracket_hole2,bracket_hole4,bracket_hole1]
for i in bracket_hole:
    plt.gca().add_patch(i)

############ man hole #################
if man_hole ==1:
    if 0 < B / 2 < 4.5:
        cx=[-B/4,B/4]
    elif 4.5 <= B / 2 < 8:
        cx=[-B/8,B/8]
    elif 8 <= B / 2 <= 10:
        cx = [-B / 4, B / 4]
    elif B / 2 > 10:
        cx=[-B/5,B/5]
    man_holes = []
    legend_added = False
    for i in cx:
        if not legend_added:
            man_hole = plt.Circle((i, 1 + ha / 2000), 0.4,label="manhole", fill=False)
            man_holes.append(man_hole)
            legend_added = True
        else:
            man_hole = plt.Circle((i, 1 + ha / 2000), 0.4, fill=False)
            man_holes.append(man_hole)
for i in man_holes:
    plt.gca().add_patch(i)

plt.legend()
plt.title("midsection")
plt.show()


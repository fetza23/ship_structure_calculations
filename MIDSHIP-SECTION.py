from main_particulars import *
import matplotlib.pyplot as plt
import numpy as np
from Bottom_plating import *
from Centre_Girder import *

############### kabuk #####################
x = np.linspace(-B/2, B/2,1000)
y = [1]*(len(x))
y[0],y[-1]=9,9

plt.plot(x, y, color='green', linewidth=tFK/5 , label="flat plate ") # /10 grafikte gözüksün diye
###########inner bottom ##################
y=[ha/1000 +1]*len(x)
plt.plot(x,y ,color="b", label="inner bottom")

############### centre girder ###################
"""x = [0, 1]  # İki noktanın x koordinatları
y = [0, ha/1000+1]  # İki noktanın y koordinatları
b=plt.plot(x,y, linewidth=tmcg/5)"""
y=np.linspace(1,ha/1000+1,1000)
x=[0]*len(y)
plt.plot(x,y,color="r",label="center girder")
plt.legend()

############ man hole #################
man_hole=plt.Circle((B/4,1+ha/2000),(ha/1000-0.2)/2,label="man hole",fill=False)
man_hole2=plt.Circle((-B/4,1+ha/2000),(ha/1000-0.2)/2,fill=False)
man_holes=[man_hole2,man_hole]
for i in man_holes:
    plt.gca().add_patch(i)

plt.legend()
plt.title("midsection")
plt.show()

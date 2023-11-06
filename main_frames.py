# f=0.75 for frames
from coefficient_calculations import *
from main_particulars import *
n=other_coefficients().calculate_n()
print("n",n)
c=other_coefficients().calculate_c()
print("c",c)
cr=other_coefficients().calculate_cr()
print("cr",cr)

def calculate_WRmf():
    l=3 # c ve ma hespalarında da 3 almıştık
    WR=(1-ma**2)*n*c*l**2*PS*cr*k
    return WR
WR=calculate_WRmf()
print("WR",WR)

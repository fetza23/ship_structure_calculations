from coefficient_calculations import *
l=14.4
P=PD

def calculate_W_dg():
    e=B/4  # The width of the area carried by deck girder
    W_dg=0.55*e*l**2*P*k
    return W_dg
W_dg=calculate_W_dg()
print("W_dg",W_dg)

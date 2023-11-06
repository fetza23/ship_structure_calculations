from coefficient_calculations import *
P=PD
l=B # if there is no longitudinal bulkhead
def calculate_W_dt():
    W_dt=0.55*e*l**2*P*k
    return W_dt
W_dt=calculate_W_dt()
print("W_dt",W_dt)
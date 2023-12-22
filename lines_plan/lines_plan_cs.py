import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d, CubicSpline
from hydrostatic_calculations import *


y = np.array([0, 0.3 * D / 6, D / 6, 2 * D / 6, 3 * D / 6, 4 * D / 6, 5 * D / 6, D])
y_extended=np.linspace(np.min(y),np.max(y),100)
plt.figure(figsize=(12, 8))

for i in range(len(df)):
    if i <= len(df)/2:
        x = df.iloc[i, df.columns.get_loc("WL0"):]
        x=np.array(x)
        x_bc=CubicSpline(y,-x,bc_type="natural")
        plt.plot(x_bc(y_extended), y_extended,"red")
        plt.plot(-x, y, "o")
        x0=(0,0)
        y0=(min(x),0)
        plt.plot(y0,x0,"red")
    else:
        x = df.iloc[i, df.columns.get_loc("WL0"):]
        x=np.array(x)
        x_bc=CubicSpline(y,x,bc_type="natural")
        plt.plot(x_bc(y_extended), y_extended,"red")
        x0=(0,0)
        y0=(-min(x),0)
        plt.plot(x, y, "o")
        plt.plot(y0,x0,"red")

plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


x_wl=np.linspace(0,L,len(df))
x_wl_extended=np.linspace(np.min(x_wl),np.max(x_wl),100)
for column_name in df.columns:
    if column_name.startswith("W"):
        y_wl = df[column_name].values
        y_wl_bc = CubicSpline(x_wl, y_wl, bc_type="natural")
        plt.plot(x_wl_extended, y_wl_bc(x_wl_extended), label=column_name)

plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=len(df.columns))

plt.show()
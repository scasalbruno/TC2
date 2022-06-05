import math
import numpy as np
import splane as sp
alpha_min = 48
alpha_max = 0.4
fo=3200
fs=9600
fn=1
ws=fs/fo
print ("Relacion normalizada de fs/fo= ", ws)

ep = np.sqrt(10**(alpha_max / 10)-1)
print("Valor de epsilon: ",  round(ep,5))

n = np.arccosh(np.sqrt((10**(alpha_min/10)-1)/ep**2))/np.arccosh(ws)
if n != math.trunc(n):
    n = math.trunc(n) + 1
print("Valor minimo de n = ", n)


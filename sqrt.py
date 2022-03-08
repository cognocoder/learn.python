
from math import *

data = []

while True:
    userdata = input(" · √")
    dec = float(userdata)
    
    if dec < 0:
        break

    res = sqrt(dec)
    data.append(res)
    
    print("   √" + str(dec) + " = " + str(res))


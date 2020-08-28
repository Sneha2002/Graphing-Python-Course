import matplotlib.pyplot as plt
import numpy as np
import math

R=6400000
l=np.arange(0,90,1)
t=24*60*60
g=9.8

omega=(2*math.pi)/t
W=[]
radian=[]
for i in l:
    ans=math.radians(i)
    radian.append(ans)


for j in radian:
    g_l=g-R*(omega**2)*(math.pow(math.cos(j),2))
    
    W.append(g_l)

plt.plot(l,W)
plt.show()
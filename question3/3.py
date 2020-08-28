import matplotlib.pyplot as plt
import numpy as np
import math

lg=1
ga=9.8
T=(2*math.pi)*(math.sqrt(lg/ga))
t=[]
arr=np.arange(0,90,1)

for i in arr:
    t.append(T)

plt.plot(arr,t)
plt.show()

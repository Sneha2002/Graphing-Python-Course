import numpy as np
import matplotlib.pylab as plot
import math as m
#initialize variables
#velocity, gravity
v = 30
g = 9.8
#increment theta 25 to 60 then find  t, x, y
#define x and y as arrays

theta = np.arange(m.pi/6, m.pi/3, m.pi/36)

t = np.linspace(0, 5, num=100) # Set time as 'continous' parameter.

for i in theta: # Calculate trajectory for every angle
    a1 = []
    b1 = []
    for k in t:
        a = ((v*k)*np.cos(i)) # get positions at every point in time
        b = ((v*k)*np.sin(i))-((0.5*g)*(k**2))
        a1.append(a)
        b1.append(b)
    p = [i for i, j in enumerate(b1) if j < 0] # Don't fall through the floor                          
    for i in sorted(p, reverse = True):
        del a1[i]
        del b1[i]

    plot.plot(a1, b1) # Plot for every angle

plot.show()
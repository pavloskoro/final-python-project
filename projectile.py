import math
import matplotlib.pyplot as plt
import numpy as np

N = 10
a = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
b = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

h = float(input('Enter height(m): '))
v = float(input('Enter horizontal speed(m/v): '))
g = float(input('Enter acceleration of gravity(m/s^2): '))
x = 0
y = h

t = 0
tf = math.sqrt(2*h/g)
dt = tf/N
math.sqrt(2*h/g)
for i in range(0,N + 1):
	x = t*v
	x_formatted = "{:.2f}".format(x)
	a[i] = x_formatted
	
	y = h - 0.5*g*t*t
	y_formatted = "{:.2f}".format(y)
	b[i] = y_formatted
	
	t = t + dt			
print("\nthe projectile will land %s meters away" %x_formatted)

t_formatted = "{:.2f}".format(t - dt) 
print("the projectile will hit the ground after %s seconds" %t_formatted)

plt.plot(a,b)
plt.show()


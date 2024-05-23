import matplotlib.pyplot as plt
import numpy as np
g = 9.80665
x = 2
y = 3

a_rad = np.arctan((y+(1/2*g))/x)
a_grad = np.rad2deg(a_rad)
V0 = x/np.cos(a_rad)

t = np.linspace(0, 1, 100)
x = V0*np.cos(a_rad)*t
y = V0*np.sin(a_rad)*t-((1/2)*g*t**2)

plt.figure(figsize=(9,7))
print(x, y)
plt.plot(x, y)

plt.show()

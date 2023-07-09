import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin

x = np.linspace(-5,5,500)
y = np.linspace(-5,5,500)
X,Y = np.meshgrid(x,y)

U = 1
R = 2
rho = 1.2

r = np.sqrt(X**2+Y**2)
theta = np.arctan(Y/X)

P = (0.5*rho*U**2)*((2*(R/r)**2*(cos(theta)**2-sin(theta)**2) - (R/r)**6))
P[r<R] = np.nan 

plt.figure(figsize=(7,7),dpi=200)
circle1 = plt.Circle((0,0),R,color='white')
plt.gca().add_patch(circle1)

plt.contourf(X,Y,P,200,cmap='jet')
plt.colorbar()
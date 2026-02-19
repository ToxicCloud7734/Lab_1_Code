import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D 


x = np.linspace(0, 2 * np.pi, 1000)

y = np.sin(x)

plt.plot(x, y, label='sin(x)', color='blue')

plt.xlabel('X value (radians)')
plt.ylabel('Amplitude')
plt.title('Sine Function Plot')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(y=0, color='k')

plt.legend()
plt.show()

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(figsize=(10, 8)) # Create a new figure

ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Plot of z = sin(sqrt(x^2 + y^2))')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
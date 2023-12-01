import numpy as np
import matplotlib.pyplot as plt

# Criar uma grade de valores x e y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

x, y = np.meshgrid(x, y)

# Criar uma onda senoidal rotacionada
theta = np.pi / 4
x_rot = x * np.cos(theta) - y * np.sin(theta)
y_rot = x * np.sin(theta) + y * np.cos(theta)
sin_rotated = np.sin(np.sqrt(x_rot**2 + y_rot**2))

# Exibir a imagem
plt.imshow(sin_rotated, cmap='viridis', origin='lower', extent=[-5, 5, -5, 5])
plt.title('Seno Rotacionado')
plt.colorbar()
plt.show()

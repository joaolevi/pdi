import numpy as np
import matplotlib.pyplot as plt

# Criar uma grade de valores x e y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

x, y = np.meshgrid(x, y)

# Criar uma função de distribuição normal (gaussiana)
gaussian = np.exp(-(x**2 + y**2) / 2)

# Exibir a imagem
plt.imshow(gaussian, cmap='viridis', origin='lower', extent=[-5, 5, -5, 5])
plt.title('Gaussiana')
plt.colorbar()
plt.show()

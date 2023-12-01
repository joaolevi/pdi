import numpy as np
import matplotlib.pyplot as plt

# Criar uma grade de valores x e y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

x, y = np.meshgrid(x, y)

# Paraboloid com um eixo escalado
z = x**2 + 2*y**2

# Exibir a imagem
plt.imshow(z, cmap='viridis', origin='lower', extent=[-5, 5, -5, 5])
plt.title('Paraboloid com um eixo escalado')
plt.colorbar()
plt.show()

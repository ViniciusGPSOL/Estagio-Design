import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4'])
ypoints = np.array([120, 60, 80, 240])


plt.bar(xpoints, ypoints, width = 0.8)
plt.legend(title = "Legenda")
plt.show()

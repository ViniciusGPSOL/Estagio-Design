import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Pizza1", "Pizza2", "Pizza3", "Pizza4"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Pizzas")
plt.show() 

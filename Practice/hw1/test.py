import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure(num = "123",figsize=(10,20))
plt.plot(x, y1)
plt.show()

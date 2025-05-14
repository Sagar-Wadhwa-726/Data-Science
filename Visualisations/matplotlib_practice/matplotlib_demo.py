import matplotlib.pyplot as plt
import numpy as np

for i in range(100):
    plt.plot(np.random.rand(5),linewidth=1)

plt.title("Too much data can be confusing !")
plt.grid(True)
plt.tight_layout()
plt.show()
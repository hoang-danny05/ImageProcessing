
import matplotlib
# matplotlib.use('Agg')
# sudo apt-get install python3.11-tk #DEPENDS ON PYTHON VERSION

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)
plt.title("oh god")

print("apttempting to show:")
plt.show()
# print("done, saving")
# plt.savefig("output.png")

from matplotlib import pyplot as plt
import numpy as num



x = num.arange(0.0, 5.0, 0.1)
y = num.cos(2*num.pi*x)

plt.plot(x,y)
plt.xlabel('arange(0.0, 5.0, 0.1)')
plt.ylabel('2πΧ')
plt.title('Y=cos(2πX)')
plt.show()
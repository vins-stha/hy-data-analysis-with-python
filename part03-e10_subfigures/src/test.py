import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0,2.0)

y1 = np.cos(x1)*np.exp(-x1)
print(x2)
y2 = np.sin(x1)*np.exp(-x2)
y3 = np.cos(x1)*np.exp(-x2)
y4 = np.tan(x1)*np.exp(-x1)


fig, ax = plt.subplots(2,2)
ax[0,0].plot(x1,y1,'*')
plt.title("PLOT-(1,1)")

#ax[0,1].subplot(1,2,2)

plt.title("PLOT-(1,2))")
ax[0,1].plot(x2,y2,"-o")

#plt.subplot(2,1,1)

plt.title("PLOT-(1,2))")
ax[1,0].plot(x1,y3,"-o")
#plt.subplot(2,1,2)

plt.title("PLOT-(1,2))")
ax[1,1].plot(x2,y4,"-^")
#plt.show()


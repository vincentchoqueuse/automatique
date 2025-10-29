import numpy as np 
import matplotlib.pyplot as plt


m = 0.2
w0 = 10

a = np.polymul([1/(w0**2), 2*m/w0, 1], [1/20, 1], )
a = np.polymul(a, [1/12, 1])

b = [1, -2, 3, 1]

zeros = np.sort(np.roots(b))
poles = np.sort(np.roots(a))
plt.plot(np.real(poles),np.imag(poles),'x',label="poles")
plt.plot(np.real(zeros),np.imag(zeros),'o',label="zeros")

plt.xlabel("$\Re e(.)$")
plt.ylabel("$\Im m(.)$")
plt.legend()
plt.grid()
plt.xlim([-4,2])
plt.axis("equal")

# save the figure
#plt.show()
plt.savefig('../img/fig1.png')
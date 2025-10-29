import numpy as np 
import matplotlib.pyplot as plt



m_vect = [0.5,1,1.25]
w0 = 1

fig = plt.figure(figsize=[7,4.8])

for m in m_vect:
    poles = np.sort(np.roots([1/(w0**2),2*m/w0,1]))
    plt.plot(np.real(poles),np.imag(poles),'x',label="$\\xi={}$".format(m), lw=2)

plt.xlabel("$\Re e(.)$")
plt.ylabel("$\Im m(.)$")
plt.legend()
plt.grid()
plt.xlim([-4,2])
plt.axis("equal")

# save the figure
plt.savefig('../img/fig1.png', dpi=300)

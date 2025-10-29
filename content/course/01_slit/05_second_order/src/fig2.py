from scipy.signal import lti
import matplotlib.pyplot as plt
import numpy as np


K1, m1, wn1 = 10,2,100
H1 = lti([K1],[1/(wn1**2),2*m1/wn1,1])
E = 1
t,s = H1.step(T=np.arange(0,0.25,0.001))  #E=1
print(H1.poles)
tr = 3/(-H1.poles[1])

tau = -1/H1.poles
print(tau)
print(3*tau)

plt.plot(t,s)
plt.plot([0,tr,tr],[0.95*K1*E,0.95*K1*E,0],'r--')
plt.grid()
plt.xlim([0,0.25])
plt.ylim([0,11])
plt.xlabel("temps [s]")

# save the figure
plt.savefig('../img/fig2.png', dpi=300)
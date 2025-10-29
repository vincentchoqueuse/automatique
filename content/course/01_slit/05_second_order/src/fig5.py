from scipy.signal import lti
import matplotlib.pyplot as plt
import numpy as np    

K3, m3, wn3 = 10,0.05,100

m_vect = [0.2, 0.707, 1, 1.5]

for m in m_vect:

    H3 = lti([K3],[1/(wn3**2),2*m/wn3,1])
    w,H3jw = H3.freqresp(w=np.logspace(0,4,200))
    ax = plt.semilogx(w,180*np.angle(H3jw)/np.pi, label=f"m={m}", lw=2)


plt.grid()
plt.legend()
plt.ylim([-180,0])
plt.xlim([1,10000])
plt.xlabel("$w$ [rad/s]")
plt.ylabel("$\\arg[H(j\omega)]$ (deg)")


# save the figure
plt.savefig('../img/fig5.png', dpi=300)
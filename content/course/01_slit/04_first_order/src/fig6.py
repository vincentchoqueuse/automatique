from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

K, tau = 2,3
sys = lti([K],[tau,1])
w,Hjw = sys.freqresp(w=np.logspace(-2,1,100))
wc = 1/tau
Hjwc = K/np.sqrt(2)

plt.semilogx(w,180*np.angle(Hjw)/np.pi)
plt.plot([0,wc,wc],[-45,-45,-90],'r--')
plt.ylim([-90,0])
plt.xlim([0.01,10])
plt.xticks([wc], ["$\omega_c = 1/\\tau$"])
plt.yticks([-45], ["$-45^o$"])
plt.grid()
plt.xlabel("$w$ [rad/s]")
plt.ylabel("$\\arg[H(j\omega)]$")

# save the figure
plt.savefig('../img/fig6.png')
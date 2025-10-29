from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

K, tau = 2,3
sys = lti([K],[tau,1])
w,Hjw = sys.freqresp(w=np.logspace(-2,1,100))
wc = 1/tau
Hjwc = K/np.sqrt(2)

plt.loglog(w,np.abs(Hjw))
plt.plot([0,wc,wc],[Hjwc,Hjwc,0],'r--')
plt.plot([0,10],[K,K],'r--')
plt.plot([0.01,10],[K*(wc/0.01),K*wc/10],'r--')
plt.ylim([0.1,3])
plt.xlim([0.01,10])
plt.yticks([K,K/np.sqrt(2)], ["$G_0(dB)$","$G_0(dB)-3$"])
plt.xticks([wc], ["$\omega_c = 1/\\tau$"])
plt.grid()
plt.xlabel("$w$ [rad/s]")
plt.ylabel("$|H(j\omega)|_{dB}$");

# save the figure
plt.savefig('../img/fig5.png')
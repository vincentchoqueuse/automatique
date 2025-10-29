import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti

w0 = 1
m = 0.2
t = np.arange(0,30,0.1)
H = lti([0.8],[1/(w0**2),2*m/w0,1])
t,s = H.step(T=t)
t2 = np.insert(t,0,[-1,0])
s2 = np.insert(s,0,[0,0])
smax = max(s)
tr = t[np.where((s>1.05*0.8) | (s<0.95*0.8))[-1]]

plt.plot(t2,s2,label="y(t)")
plt.plot([0,0,0,30],[0,0,1,1],color = 'r', label="x(t)=Eu(t)")
plt.xlabel("$t$ [rad/s]")
plt.ylabel("$y(t)$")
plt.xlim([-1,30])
plt.ylim([0,1.25])
plt.xticks([0,tr[-1]],["0","$t_r$"])
plt.yticks([0,0.95*0.8,0.8,1.05*0.8,1,smax],["0","$0.95y(\infty)$","$y(\infty)$","$1.05y(\infty)$","$x(\infty)=E$","$\max(y(t))$"])
plt.grid()
plt.legend()
plt.tight_layout()

plt.savefig('../img/fig2.png')
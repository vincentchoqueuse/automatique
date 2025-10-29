from scipy.signal import lti
import matplotlib.pyplot as plt
import numpy as np

K3, m3, wn3 = 10,0.1,100
H3 = lti([K3],[1/(wn3**2),2*m3/wn3,1])
E = 1
t,s = H3.step(T=np.arange(0,0.7,0.001))  #E=1
Dr = np.exp(-np.pi*m3/np.sqrt(1-m3**2))

wp = wn3*np.sqrt(1-m3**2)
Tp = 2*np.pi/wp
t_r = 30/wn3
print(H3.poles)
print(f"wp={wp}, Tp={Tp}, tr={t_r}")


plt.plot(t,s)
plt.plot(t,K3*E*(1+(1/np.sqrt(1-m3**2))*np.exp(-m3*wn3*t)),'r--')
plt.plot(t,K3*E*(1-(1/np.sqrt(1-m3**2))*np.exp(-m3*wn3*t)),'r--')
plt.plot(t,0.95*K3*E*(t>=0),'r--')
plt.plot(t,1.05*K3*E*(t>=0),'r--')
plt.plot([0,t_r, t_r],[1.05*K3*E,1.05*K3*E, 0],'r--')
plt.plot([0,0.7],[K3*E,K3*E],'r--')
plt.plot([0,0.7],[K3*E*(1+Dr),K3*E*(1+Dr)],'r--')
plt.grid()
plt.xlim([0,0.7])
plt.ylim([0,20])
plt.xlabel("temps [s]")

# save the figure
plt.savefig('../img/fig3.png', dpi=300)

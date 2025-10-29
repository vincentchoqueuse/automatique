from scipy.signal import lti
import matplotlib.pyplot as plt

K, tau = 2,3
sys = lti(K, [tau, 1])
t,s = sys.impulse()

# plot figure
plt.plot(t,s)
plt.xlim([0,20])
plt.ylim([0,1])
plt.grid()

# add annotation
plt.axhline(y = K/tau, color ='r', linestyle = '--')
plt.axhline(y = 0.05*K/tau, color = 'r', linestyle = '--')
plt.axvline(x = 9, color = 'r', linestyle ='--')
plt.xlabel("time [s]")
plt.yticks([0.05*K/tau, K/tau],["$0.05KE/ \\tau$","$KE/ \\tau$"])
plt.xticks([9], ["$3\\tau$"])
plt.ylabel("y(t)")
plt.tight_layout()

# save the figure
plt.savefig('../img/fig2.png')
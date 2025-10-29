from scipy.signal import lti
import matplotlib.pyplot as plt

K, tau = 2,3
sys = lti(K, [tau, 1])
t,s = sys.step()

# plot figure
plt.plot(t,s)
plt.xlim([0,20])
plt.ylim([0,2.2])
plt.grid()

# add annotation
plt.axhline(y = 2, color ='r', linestyle = '--')
plt.axhline(y = 1.9, color = 'r', linestyle = '--')
plt.axvline(x = 9, color = 'r', linestyle ='--')
plt.xlabel("time [s]")
plt.yticks([1.9,2],["$0.95KE$","$KE$"])
plt.xticks([9], ["$3\\tau$"])
plt.ylabel("y(t)")
plt.tight_layout()

# save the figure
plt.savefig('../img/fig3.png')
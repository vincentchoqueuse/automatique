from scipy.signal import lti
import matplotlib.pyplot as plt

K, tau = 2,3
sys = lti(K, [tau, 1])
poles = sys.poles

# plot figure
plt.plot(poles.real,poles.imag,'x',label="poles")

plt.xlabel("$\Re e(.)$")
plt.ylabel("$\Im m(.)$")
plt.legend()
plt.grid()
plt.ylim([-2,2])
plt.xlim([-3,1])
plt.xticks([-1/tau, 0], ["$-1/\\tau$", "0"])
#plt.axis("equal")

# add annotation
plt.tight_layout()

# save the figure
plt.savefig('../img/fig1.png')
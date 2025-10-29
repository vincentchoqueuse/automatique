import numpy as np
import matplotlib.pyplot as plt


# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# plot figure
t = np.array([-0.5, 1])
u = (t==0)

axs[0, 0].plot(t,u)
axs[0, 0].set_ylim([-0.5, 1.5])
axs[0, 0].set_xlim([-0.5, 1])
axs[0, 0].set_xlabel("$t$")
axs[0, 0].set_ylabel("$\delta(t)$")
axs[0, 0].annotate("", xy=(0, 1), xytext=(0, 0), arrowprops=dict(arrowstyle="->",linewidth=2,color="C0"))
axs[0, 0].set_title("Impulsion de Dirac")
axs[0, 0].grid()



# plot figure
t = np.array([-0.5, -0.0001, 0, 1])
u = (t>=0)

axs[0, 1].plot(t,u)
axs[0, 1].set_ylim([-0.5, 1.5])
axs[0, 1].set_xlim([-0.5, 1])
axs[0, 1].set_xlabel("$t$")
axs[0, 1].set_ylabel("$u(t)$")
axs[0, 1].set_title("Signal échelon")
axs[0, 1].grid()


# plot figure
t = np.array([-0.5, -0.0001, 0, 1])
u = (t>=0)*t

axs[1, 0].plot(t,u)
axs[1, 0].set_ylim([-0.5, 1.5])
axs[1, 0].set_xlim([-0.5, 1])
axs[1, 0].set_xlabel("$t$")
axs[1, 0].set_ylabel("$r(t)$")
axs[1, 0].set_title("Rampe")
axs[1, 0].grid()


# plot figure
E = 1.2
phi = 0.1
f = 2
T = 1/f
t = np.arange(-1, 1, 0.01)
e = E*np.cos(2*np.pi*f*t+phi)
t0 = -phi/(2*np.pi*f)

axs[1, 1].plot(t,e)
axs[1, 1].plot([-0.5, 1],[E, E],"r--", linewidth=1)
axs[1, 1].plot([t0, t0],[-1.5, 1.5],"r--", linewidth=1)
axs[1, 1].plot([t0+T, t0+T],[-1.5, 1.5],"r--", linewidth=1)
axs[1, 1].annotate("", xy=(t0+T, 0.1), xytext=(t0, 0.1), arrowprops=dict(arrowstyle="<->",linewidth=1,color="r"))
axs[1, 1].annotate("", xy=(-0.2, E), xytext=(-0.2, 0), arrowprops=dict(arrowstyle="<->",linewidth=1,color="r"))
axs[1, 1].text(-0.3, E/2, "$A$", fontsize=12,color="r")
axs[1, 1].text(t0+T/2-0.1, 0.2, "$T_0=1/f_0$", fontsize=12,color="r")
axs[1, 1].set_ylim([-1.5, 1.5])
axs[1, 1].set_xlim([-0.5, 1])
axs[1, 1].set_xlabel("$t$")
axs[1, 1].set_ylabel("$x(t)$")
axs[1, 1].set_title("Signal sinusoïdal")
axs[1, 1].grid()

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('../img/fig1.png')

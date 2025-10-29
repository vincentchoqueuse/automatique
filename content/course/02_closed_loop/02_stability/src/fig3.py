
import numpy as np
import matplotlib.pyplot as plt
from control import tf,  bode, feedback, margin


H = tf([2], [1, 3, 3, 1]) 
Gm, Pm, Wcg, Wcp = margin(H)



# Compute bode response
mag, phase, omega = bode(H, dB=True, Hz=False, deg=True, plot=False)

# step response of the closed loop
H_cl = feedback(H, 1)

print(f"Gm={20*np.log10(Gm)}")
print(f"Pm={Pm}")


# Nichols
plt.plot(180*phase/np.pi, 20*np.log10(mag), lw=2)
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.plot([-180], [0], 'ro', markersize=5)
plt.grid(True)

plt.plot([-180 + Pm, -180], [0, 0], 'r--', markersize=8)

# Gain margin (M_G)
plt.plot([-180, -180], [-20 * np.log10(Gm), 0], 'r--', markersize=8)

plt.annotate(
    f"$M_\\varphi$",
    xy=(-180 + Pm / 2, 0),
    xytext=(-180 + Pm / 2, 5),
    ha='center',
    color='red',
    fontsize=10,
)

# Gain margin (M_G) with arrow
plt.annotate(
    f"$M_G$",
    xy=(-180, -10 * np.log10(Gm)),
    xytext=(-190, -10 * np.log10(Gm)),
    ha='center',
    color='red',
    fontsize=10,
)

plt.xlim([-250, -20])
plt.ylim([-60, 10])

plt.savefig(f'../img/fig3.png', dpi=300)

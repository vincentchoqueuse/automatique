import numpy as np
import matplotlib.pyplot as plt
from control import tf

# Parameters
K = 2
a = 0.05
T = 10

w_m = 1/(T*np.sqrt(a))


# Transfer function of PI: Kp * (1 + wi/s)
C_s = K * tf([T, 1], [a*T, 1])

# Compute bode response
omega = np.logspace(-2, 2, 400)
mag, phase, omega = C_s.frequency_response(omega=omega)


# Plot magnitude
plt.figure(figsize=(8, 4))
plt.semilogx(omega, 20 * np.log10(abs(mag)), label="$|C(j\omega)|$ (dB)")
plt.axhline(20*np.log10(K), c="r", linestyle="--", label="$20.log10(K)$")
plt.axhline(20*np.log10(K/a), c="r", linestyle=":", label="$20.log10(K/a)$")
plt.axhline(20*np.log10(K/np.sqrt(a)), c="r", linestyle="-", label="$20.log10(K/\sqrt{a})$")
plt.axvline(w_m, c="r", linestyle=":")


xticks = [w_m]
labels = [r"$\omega_m=1/(T \sqrt{a})$"]
plt.xticks(xticks, labels)

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel("$|C_{av}(j\omega)|_{dB}$")
plt.legend()
plt.xlim([0.01, 10])
plt.grid(True, which="both", linestyle="--")
plt.savefig('../img/fig1_1.png', dpi=300)


# Plot phase
plt.figure(figsize=(8, 4))
plt.semilogx(omega, 180*np.unwrap(phase)/np.pi, label="$\\arg[C(j\omega)]$")
plt.scatter([w_m], [-45], c='r', s=50)
plt.axvline(w_m, c="r", linestyle=":")
plt.axhline(-45, c="r", linestyle=":")

xticks = [w_m]
labels = [r"$\omega_m=1/(T \sqrt{a})$"]
plt.xticks(xticks, labels)


Phi_M = 180*np.arcsin((1-a)/(1+a))/(np.pi)

yticks = [0, Phi_M, 90]
labels = ["$0$", "$ \Phi_m$", "$90$"]
plt.yticks(yticks, labels)

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel("$\\arg[C_{ap}(j\omega)]$")
plt.xlim([0.01, 10])
plt.ylim([0., 90])
plt.grid(True, which="both", linestyle="--")
plt.savefig('../img/fig1_2.png', dpi=300)


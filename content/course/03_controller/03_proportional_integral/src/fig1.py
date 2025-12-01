import numpy as np
import matplotlib.pyplot as plt
from control import tf

# Parameters
K_p = 2
w_i = 1

# Transfer function of PI: Kp * (1 + wi/s)
C_s = K_p * tf([1, w_i], [1, 0])

# Compute bode response
omega = np.logspace(-1, 3, 400)
mag, phase, omega = C_s.frequency_response(omega=omega)

# Compute point at w = wi
mag_wi = 20 * np.log10(abs(C_s(1j * w_i)))
mag_Kp = 20 * np.log10(K_p)
mag_Kp_plus3 = mag_Kp + 3

# Plot magnitude
plt.figure(figsize=(8, 4))
plt.semilogx(omega, 20 * np.log10(abs(mag)), label="$|C(j\omega)|$ (dB)")
plt.axhline(mag_Kp, c="r", linestyle="--", label="$20.log10(K_p)$")
plt.axhline(mag_Kp_plus3, c="r", linestyle=":", label="$20log10(K_p)$ + 3 dB")
plt.scatter([w_i], [mag_wi], c='r', s=50)
plt.axvline(w_i, c="r", linestyle=":")

xticks = [w_i]
labels = [r"$\omega_i=1/T_i$"]
plt.xticks(xticks, labels)

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel("$|C(j\omega)|_{dB}$")
plt.legend()
plt.xlim([0.1, 100])
plt.grid(True, which="both", linestyle="--")
plt.savefig('../img/fig1_1.png', dpi=300)


# Plot phase
plt.figure(figsize=(8, 4))
plt.semilogx(omega, 180*np.unwrap(phase)/np.pi, label="$\\arg[C(j\omega)]$")
plt.scatter([w_i], [-45], c='r', s=50)
plt.axvline(w_i, c="r", linestyle=":")
plt.axhline(-45, c="r", linestyle=":")

xticks = [w_i]
labels = [r"$\omega_i=1/T_i$"]
plt.xticks(xticks, labels)

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel("$\\arg[C(j\omega)]$")
plt.legend()
plt.xlim([0.1, 100])
plt.grid(True, which="both", linestyle="--")
plt.savefig('../img/fig1_2.png', dpi=300)



import numpy as np
from control import tf, freqresp
import matplotlib.pyplot as plt

# Paramètres du système de premier ordre
H = tf([1], [1, 1])

mag, phase, omega = freqresp(H, omega=np.logspace(-1, 1, 100))

# Création de la figure en 2x2
fig, axs = plt.subplots(1, 2, figsize=(12, 5))


# Subplot 1: Impulsion simple
axs[0].loglog(omega, mag)
axs[0].set_xlabel("$\omega$ [rad/s]")
axs[0].set_ylabel("$|H(j\omega)|$")
axs[0].set_xlim([0.1, 10])
axs[0].grid()
axs[0].set_title('Module')

# Subplot 2: Réponse impulsionnelle à une impulsion simple
axs[1].semilogx(omega, phase)
axs[1].set_xlabel("$\omega$ [rad/s]")
axs[1].set_ylabel("$\\arg[H(j\omega)]$ [rad]")
axs[1].set_xlim([0.1, 10])
axs[1].grid()
axs[1].set_title('Argument')

plt.tight_layout()


# Save the figure
plt.savefig('../img/fig3.png')
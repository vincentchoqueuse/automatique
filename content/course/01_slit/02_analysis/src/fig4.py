import numpy as np
from control import tf, forced_response
import matplotlib.pyplot as plt

# Paramètres du système de premier ordre
H = tf([1], [1, 1])

t = np.arange(0, 100, 0.01)
x = np.sin(1*t)

t2, y2 = forced_response(H,t,x)

# Création de la figure en 2x2
fig, axs = plt.subplots(1, 2, figsize=(12, 5))


# Subplot 1: Impulsion simple
axs[0].plot(t-20*np.pi, x)
axs[0].set_xlabel("$t$ [s]")
axs[0].set_ylabel("$x(t)$")
axs[0].set_xlim([0, 10])
axs[0].set_ylim([-1.5, 1.5])
axs[0].grid()
axs[0].set_title('entrée: $e(t)=\sin(t)$')

# Subplot 2: Réponse impulsionnelle à une impulsion simple
axs[1].plot(t2-20*np.pi, y2)
axs[1].set_xlabel("$t$ [s]")
axs[1].set_ylabel("$y(t)$")
axs[1].set_xlim([0, 10])
axs[1].set_ylim([-1.5, 1.5])
axs[1].grid()
axs[1].set_title('sortie: $y(t)$')

plt.tight_layout()


# Save the figure
plt.savefig('../img/fig4.png')
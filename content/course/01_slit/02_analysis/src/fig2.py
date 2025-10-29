import numpy as np
from control import tf, step_response
import matplotlib.pyplot as plt

# Paramètres du système de premier ordre
H = tf([1], [1, 1])

t = np.arange(-0.2, 5, 0.01)
T, y = step_response(H)
T = np.insert(T, 0, -0.2)
y = np.insert(y, 0, 0)

# Création de la figure en 2x2
fig, axs = plt.subplots(1, 2, figsize=(12, 5))


# Subplot 1: Impulsion simple
axs[0].plot(t, (t>=0))
axs[0].set_ylim([-0.25, 1.25])
axs[0].set_xlim([-0.2, 5])
axs[0].set_xlabel("$t$")
axs[0].set_ylabel("$u(t)$")
axs[0].grid()
axs[0].set_title('entrée: $u(t)$')

# Subplot 2: Réponse impulsionnelle à une impulsion simple
axs[1].plot(T, y)
axs[1].set_xlim([-0.2, 5])
axs[1].set_ylim([-0.25, 1.25])
axs[1].set_xlabel("$t$")
axs[1].set_ylabel("$y(t)$")
axs[1].grid()
axs[1].set_title('sortie: $y(t)$')

plt.tight_layout()


# Save the figure
plt.savefig('../img/fig2.png')

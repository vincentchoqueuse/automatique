import numpy as np
import matplotlib.pyplot as plt

# Paramètres du système de premier ordre
tau = 1.0
t = np.linspace(-0.2, 10, 400)

# Réponse impulsionnelle d'un système de premier ordre
h = (1 / tau) * np.exp(-t / tau)

# Impulsion simple
impulse = np.zeros_like(t)
impulse[0] = 1.0
response = np.convolve(impulse, h)[:len(t)] * (t[1] - t[0])*(t>=0)

# Impulsion décalée et pondérée
t0 = 1.0
a = 1.5
impulse_shifted = np.zeros_like(t)
shift_index = np.where(t >= t0)[0][0]
impulse_shifted[shift_index] = a
response_shifted = np.convolve(impulse_shifted, h)[:len(t)] * (t[1] - t[0])*(t-t0>=0)

# Création de la figure en 2x2
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Impulsion simple
axs[0, 0].plot(t, 0*t)
axs[0, 0].set_ylim([-0.5, 2])
axs[0, 0].set_xlim([-0.2, 2])
axs[0, 0].set_xlabel("$t$")
axs[0, 0].set_ylabel("$\delta(t)$")
axs[0, 0].annotate("", xy=(0, 1), xytext=(0, 0), arrowprops=dict(arrowstyle="->", linewidth=2, color="C0"))
axs[0, 0].grid()
axs[0, 0].set_title('entrée: $\delta(t)$')

# Subplot 2: Réponse impulsionnelle à une impulsion simple
axs[0, 1].plot(t, response)
axs[0, 1].set_xlim([-0.2, 6])
axs[0, 1].set_ylim([-0.01, 0.05])
axs[0, 1].set_xlabel("$t$")
axs[0, 1].set_ylabel("$h(t)$")
axs[0, 1].grid()
axs[0, 1].set_title('sortie: $h(t)$')

# Subplot 3: Impulsion décalée et pondérée
axs[1, 0].plot(t, 0*t)
axs[1, 0].set_ylim([-0.5, 2])
axs[1, 0].set_xlim([-0.2, 2])
axs[1, 0].set_xlabel("$t$")
axs[1, 0].set_ylabel("$a \delta(t - t_0)$")
axs[1, 0].annotate("", xy=(t0, a), xytext=(t0, 0), arrowprops=dict(arrowstyle="->", linewidth=2, color="C0"))
axs[1, 0].grid()
axs[1, 0].set_title('entrée: $1.5\delta(t-1)$')

# Subplot 4: Réponse impulsionnelle associée
axs[1, 1].plot(t, response_shifted)
axs[1, 1].set_xlim([-0.2, 6])
axs[1, 1].set_ylim([-0.01, 0.05])
axs[1, 1].set_xlabel("$t$")
axs[1, 1].set_ylabel("$h(t - t_0)$")
axs[1, 1].grid()
axs[1, 1].set_title('sortie: $1.5h(t-1)$')

plt.tight_layout()


# Save the figure
plt.savefig('../img/fig1.png')

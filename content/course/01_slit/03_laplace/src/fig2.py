import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode, lti

# Paramètres du système de premier ordre
K = 2  # Gain
tau = 10  # Constante de temps

# Fonction de transfert H(s) = K / (tau*s + 1)
numerator = [K]
denominator = [tau, 1]
system = TransferFunction(numerator, denominator)

# Fréquence angulaire (logarithmique)
omega = np.logspace(-2, 1, 500)  # De 0.01 rad/s à 10 rad/s

# Calcul de la réponse fréquentielle
w, mag, phase = bode(system, omega)

# Diagramme de Bode avec un subplot pour le module et l'argument
plt.figure(figsize=(10, 8))

# Subplot pour le module (Amplitude)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Amplitude en dB
plt.ylabel('Amplitude (dB)')
plt.grid(which="both", linestyle="--", linewidth=0.5)

# Subplot pour l'argument (Phase)
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Phase en degrés
plt.ylabel('Phase (°)')
plt.xlabel('Fréquence angulaire (rad/s)')
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig('../img/fig2_1.png')



# Diagramme de Black (Plan complexe)
_, H = lti(numerator, denominator).freqresp(omega)

plt.figure(figsize=(8, 6))
plt.plot(H.real, H.imag, label="Réponse fréquentielle")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.xlabel('Partie réelle')
plt.ylabel('Partie imaginaire')
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.savefig('../img/fig2_2.png')



# Diagramme de Nichols (Gain en dB vs Phase)
plt.figure(figsize=(8, 6))

# Gain (Magnitude en dB) et Phase
plt.plot(phase, mag, label="Réponse fréquentielle")
plt.xlabel('Phase (°)')
plt.ylabel('Gain (dB)')
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.axhline(0, color="black", linewidth=0.5, linestyle="--", label="Gain nul")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--", label="Phase nulle")
plt.legend()
plt.tight_layout()
plt.savefig('../img/fig2_3.png')

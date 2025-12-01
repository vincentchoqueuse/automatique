import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode, nichols_grid

# -----------------------------
# Paramètres
# -----------------------------
Kp = 6/4
omega = np.logspace(-2, 3, 2000)  # plus dense pour bien trouver ωc

G = tf([1.5], [1, 1, 1])

# -----------------------------
# Étape 1 : boucle ouverte proportionnelle Kp G(s)
# -----------------------------
L_p = Kp * G
mag_p, phase_p, omega_p = L_p.frequency_response(omega = omega)
mag_p_db = 20 * np.log10(np.abs(mag_p))
idx_wc = np.argmin(np.abs(mag_p_db) + 10*(omega_p< 0.47))  # point le plus proche de 0 dB
omega_c = omega_p[idx_wc]

print("omega_c ≈", omega_c)

# -----------------------------
# Étape 2 : choix de ωi = ωc / 10
# -----------------------------
wi = omega_c / 10
print("omega_i = omega_c / 10 ≈", wi)
C_pi = Kp * tf([1, wi], [1, 0])

# -----------------------------
# Réponses fréquentielles pour le Nichols
# -----------------------------
# G(s)
mag_G, phase_G, omega_G = G.frequency_response(omega=omega)
mag_G_db = 20 * np.log10(np.abs(mag_G))
phase_G_deg = 180 * np.unwrap(phase_G) / np.pi

# Kp G(s)
mag_Gp, phase_Gp, omega_Gp = L_p.frequency_response(omega=omega)
mag_Gp_db = 20 * np.log10(np.abs(mag_Gp))
phase_Gp_deg = 180 * np.unwrap(phase_Gp) / np.pi

# C_pi(s) G(s)
L_pi = C_pi * G
mag_Gpi, phase_Gpi, omega_Gpi = L_pi.frequency_response(omega=omega)
mag_Gpi_db = 20 * np.log10(np.abs(mag_Gpi))
phase_Gpi_deg = 180 * np.unwrap(phase_Gpi) / np.pi

# -----------------------------
# Point correspondant à ω = ωi sur C_pi G
# -----------------------------
idx_wi = np.argmin(np.abs(omega - wi))
phi_wi = phase_Gpi_deg[idx_wi]
mag_wi = mag_Gpi_db[idx_wi]

# -----------------------------
# Tracé Nichols
# -----------------------------
plt.figure(figsize=(10, 6))

plt.plot(phase_G_deg,   mag_G_db,   label="$G(s)$")
plt.plot(phase_Gp_deg,  mag_Gp_db,  "r-", label="$K_p G(s)$")

plt.scatter(phase_Gp_deg[idx_wc], mag_Gp_db[idx_wc], s=60, color="r")
plt.text(phase_Gp_deg[idx_wc], mag_Gp_db[idx_wc], r"  $\omega_c$", color="r")
cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])
nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

plt.plot([-360, 0], [0, 0], 'k--')          # 0 dB
plt.plot([-135, -135], [-40, 20], 'k--')    # repère -135°
plt.scatter(-180, 0, color="r", s=50)       # point critique -180°, 0 dB

# Mise en forme
plt.xlabel("Phase (deg)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])
plt.ylim([-40, 20])
plt.grid(True)
plt.legend()

plt.savefig('../img/fig2_1.png', dpi=300)


plt.plot(phase_Gpi_deg, mag_Gpi_db, "g-", label="$C_{PI}(s)G(s)$")
plt.grid(True)
plt.legend()
plt.savefig('../img/fig2_2.png', dpi=300)

plt.show()


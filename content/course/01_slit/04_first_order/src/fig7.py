from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

# System parameters
K, tau = 2, 3
sys = lti([K], [tau, 1])

# Frequency range
w = np.logspace(-2, 2, 1000)  # Frequency range from very low to high values
w, Hjw = sys.freqresp(w=w)    # Frequency response H(jw)

# Magnitude in dB and phase in degrees
magnitude_dB = 20 * np.log10(np.abs(Hjw))
phase_deg = np.angle(Hjw, deg=True)

# Plot Nichols Diagram
plt.figure(figsize=(8, 6))
plt.plot(phase_deg, magnitude_dB, label="1st Order LP System", lw=2)
plt.scatter(-45, 20*np.log10(K/np.sqrt(2)), color='red', zorder=5, label="Cut-off point")
plt.axhline(20 * np.log10(K), color='r', linestyle='--', label="DC gain (Magnitude)")
plt.axvline(-90, color='g', linestyle='--', label="Phase at Cut-off Frequency")

plt.yticks([20*np.log10(K),20*np.log10(K/np.sqrt(2))], ["$G_0 (dB)$","$G_0(dB)-3$"])
plt.xticks([-90, -45, 0], ["-90", "-45", "0" ])

# Axis limits and labels
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig('../img/fig7.png')

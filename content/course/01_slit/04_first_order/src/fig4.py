from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

# System parameters
K, tau = 2, 3
sys = lti([K], [tau, 1])

# Frequency range
w = np.logspace(-5, 2, 100)  # Frequency range from very low to high values
_, Hjw = sys.freqresp(w=w)    # Frequency response H(jw)

# Extract real and imaginary parts
real_part = Hjw.real
imag_part = Hjw.imag

# Nyquist plot
plt.figure(figsize=(8, 6))
plt.plot(real_part, imag_part, label="1st Order LP System", lw=2)
plt.plot(real_part, -imag_part, '--', label="Mirror Image (Negative Frequencies)", lw=1)

# Highlight DC gain (w = 0) and high-frequency point (w -> ∞)
plt.scatter(real_part[0], imag_part[0], color='red', zorder=5, label="DC Gain (w=0)")
plt.scatter(real_part[-1], imag_part[-1], color='orange', zorder=5, label="w → ∞")

# Add axis lines
plt.axhline(0, color='gray', linestyle='--', lw=1)
plt.axvline(0, color='gray', linestyle='--', lw=1)

# Labels and grid
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid(True, which="both", linestyle="--")
plt.xticks([0, K/2, K], ["0", "K/2", "K" ])
plt.yticks([-K, -K/2, 0, K/2, K], ["-K", "-K/2", "0", "K/2", "K" ])


plt.legend()
plt.axis('equal')  # Ensure equal scaling of axes
plt.tight_layout()

# Save the figure
plt.savefig('../img/fig4.png')

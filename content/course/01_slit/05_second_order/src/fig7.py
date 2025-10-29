from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

# System parameters
# System parameters
K, m, wn = 10,0.1,100

m_vect = [0.2, 0.707, 1, 1.5]
w = np.logspace(-1, 4, 1000)  # Frequency range from very low to high values

plt.figure(figsize=(8, 6))
for m in m_vect:

    # Frequency range
    H = lti([K],[1/(wn**2),2*m/wn,1])
    w, Hjw = H.freqresp(w=w)    # Frequency response H(jw)

    # Magnitude in dB and phase in degrees
    magnitude_dB = 20 * np.log10(np.abs(Hjw))
    phase_deg = np.angle(Hjw, deg=True)

    # Plot Nichols Diagram
    
    plt.plot(phase_deg, magnitude_dB, label=f"m={m}", lw=2)


# Axis limits and labels
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()
plt.ylim([-60, 30])

# Save the figure
plt.savefig('../img/fig7.png', dpi=300)

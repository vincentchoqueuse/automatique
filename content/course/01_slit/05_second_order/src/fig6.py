from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt

# System parameters
K, m, wn = 10,0.1,100

m_vect = [0.2, 0.707, 1, 1.5]

plt.figure(figsize=(8, 6))

for m in m_vect:
    H = lti([K],[1/(wn**2),2*m/wn,1])

    # Frequency range
    w = np.logspace(-4, 3, 500)  # Frequency range from very low to high values
    _, Hjw = H.freqresp(w=w)    # Frequency response H(jw)

    # Extract real and imaginary parts
    real_part = Hjw.real
    imag_part = Hjw.imag

    # Nyquist plot
    
    plt.plot(real_part, imag_part, label=f"m={m}", lw=2)

    # Add axis lines
    plt.axhline(0, color='gray', linestyle='--', lw=1)
    plt.axvline(0, color='gray', linestyle='--', lw=1)

# Labels and grid
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid(True, which="both", linestyle="--")



plt.legend()
plt.axis('equal')  # Ensure equal scaling of axes
plt.tight_layout()

# Save the figure
plt.savefig('../img/fig6.png', dpi=300)

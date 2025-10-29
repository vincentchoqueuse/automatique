import numpy as np
from control import tf, feedback, forced_response
import matplotlib.pyplot as plt

# System definitions
K = 2
G_list = [
    tf([0.5 * K], [1, 10, 1]),           # Classe L=0 (no pure integrator)
    tf([0.5 * K], [1, 2, 1, 0])         # Classe L=1 (one integrator)
]

# Time vector and input signals
t = np.arange(0, 200, 0.1)
E = 1  # Amplitude of the input and perturbation
D = 0.25
# Define step input with delay
u = E * (t >= 0)  # Input step delayed by 10 seconds
d = D * (t >= 100)  # Perturbation step delayed by 30 seconds

# Create figure for the responses

# Simulate and plot responses for each system
for L, G in enumerate(G_list):
    plt.figure()
    plt.plot(t, u, label="Entrée $e(t)$")
    plt.plot(t, d, label="Perturbation $d(t)$")

    H = feedback(G, 1)      # Closed-loop system transfer function
    N = 1 / (1 + G)         # Disturbance rejection transfer function
    
    # Compute system responses
    _, y_u = forced_response(H, T=t, U=u)  # Response to the input
    _, y_d = forced_response(N, T=t, U=d)  # Response to the disturbance

    # Total response
    y_total = y_u + y_d

    # Plot the total response
    plt.plot(t, y_total, label=f"$y(t)$: Classe L={L}")
    plt.xlim([0, 200])

    #plt.ylim([0, 1.5 * E])
    plt.xlabel("Temps [s]")
    plt.ylabel("$y(t)$")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'../img/fig3_{L+1}.png', dpi=300)


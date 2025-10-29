
import numpy as np
import matplotlib.pyplot as plt
from control import tf,  bode, step_response, feedback

# Define the transfer function directly


K_vect = [2, 10]

xlim_vect = [14, 80]
for index, K in enumerate(K_vect):

    H = tf([K], [1, 3, 3, 1]) 

    # Compute bode response
    mag, phase, omega = bode(H, dB=True, Hz=False, deg=True, plot=False)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # step response of the closed loop
    H_cl = feedback(H, 1)
    t, y = step_response(H_cl)

    # Nichols
    axes[0].plot(180*phase/np.pi, 20*np.log10(mag), lw=2)
    axes[0].set_title("Black Diagram (Open Loop)")
    axes[0].set_xlabel("Arg (degree)")
    axes[0].set_ylabel("Modulus (dB)")
    axes[0].plot([-180], [0], 'ro', markersize=5)
    axes[0].grid(True)

    axes[0].set_ylim([-100, 20])
    axes[0].set_xlim([-270, 0])

    axes[1].plot(t, y, label="Step Response ", lw=2)
    axes[1].set_title("Step Response (Closed Loop)")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)
    axes[1].set_xlim([0, xlim_vect[index]])

    plt.savefig(f'../img/fig2_{index+1}.png', dpi=300)

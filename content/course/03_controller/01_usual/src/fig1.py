import matplotlib.pyplot as plt
import numpy as np
from control import tf, bode

# Define transfer functions for P, PI, and PID controllers
Kp = 2  # Gain for the proportional controller
Ki = 1  # Integral gain
Kd = 0.5  # Derivative gain

# Parameters for the phase-lead controller
alpha = 10  # Ratio (alpha < 1 for phase-lead)
omega_lead = 3  # Frequency for the zero/pole pair


# P controller: H_P(s) = Kp
H_P = tf([Kp], [1])

# PI controller: H_PI(s) = Kp + Ki/s
H_PI = tf([Kp, Ki], [1, 0])

# PID controller: H_PID(s) = Kp + Ki/s + Kd*s
H_PID = tf([Kd, Kp, Ki], [1, 0])

# Phase-lead controller: H_Lead(s) = (1 + alpha*T*s) / (1 + T*s)
T =1/(omega_lead)
H_Lead = tf([alpha * T, 1], [T, 1])

# Compute bode responses
systems = {"P": H_P, "PI": H_PI, "PID": H_PID, "AP": H_Lead}
bode_data = {}

w = np.logspace(-2, 2, 500)


for label, system in systems.items():
    fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    mag, phase, omega = bode(system, omega=w, plot=False)

    if label == "AP":
        phase += 2*np.pi

    ax_mag.semilogx(omega, 20 * np.log10(mag), label=label)
    ax_phase.semilogx(omega, np.degrees(phase), label=label)

    # Magnitude plot
    ax_mag.set_ylabel('Magnitude [dB]')
    ax_mag.grid()
    ax_mag.legend()
    ax_mag.set_xlim([0.01, 100])

    # Phase plot
    ax_phase.set_xlabel('Frequency [rad/s]')
    ax_phase.set_ylabel('Phase [deg]')
    ax_phase.grid()
    ax_phase.set_xlim([0.01, 100])
    ax_phase.legend()

    plt.savefig(f'../img/fig1_{label}.png', dpi=300)


from control import nichols_grid, tf, bode, feedback, step_response
import matplotlib.pyplot as plt
import numpy as np

cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])

# Define the transfer function directly
G = tf([0.4], [1, 3, 1, 1])

# Compute bode response
mag, phase, omega = G.frequency_response(omega=np.logspace(-1, 3, 200))
plt.plot(180*np.unwrap(phase)/np.pi,  20*np.log10(np.abs(mag)) , label="$G(s)$")

G1 = 2*G
mag, phase, omega = G1.frequency_response(omega=np.logspace(-1, 3, 200))
plt.plot(180*np.unwrap(phase)/np.pi,  20*np.log10(np.abs(mag)), "r--", label="$2G(s)$")

G2= G /2 
mag, phase, omega = G2.frequency_response(omega=np.logspace(-1, 3, 200))
plt.plot(180*np.unwrap(phase)/np.pi,  20*np.log10(np.abs(mag)), "r:", label="$0.5G(s)$")

plt.plot([-180], [0], "ro")

nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')


# Axis limits and labels
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])
plt.ylim([-40, 20])
plt.legend()

# Save the figure
plt.savefig('../img/fig1.png', dpi=300)


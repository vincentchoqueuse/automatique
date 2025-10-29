from control import nichols_grid, tf, bode, feedback, step_response
import matplotlib.pyplot as plt
import numpy as np

cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])

# Define the transfer function directly
H = tf([1.1], [3, 1, 1])

# Compute bode response
mag, phase, omega = bode(H, plot=False)

# Plot
plt.plot((180*phase)/np.pi, 20*np.log10(mag))
plt.plot([-180], [0], 'ro', markersize=5)

print(20*np.log10(mag[630]))

plt.plot([(180*phase[633])/np.pi], [20*np.log10(mag[633])], 'ko', markersize=5)
plt.text(180*phase[633]/np.pi, 20*np.log10(mag[633])+2, f"wr={int(omega[633]*1000)/1000} rad/s")

print(omega[633])

nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

# Axis limits and labels
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])

# Save the figure
plt.savefig('../img/fig2_1.png', dpi=300)


H_BF = feedback(H, 1)
t, y =  step_response(H_BF)

# Plot
plt.figure()
plt.plot(t, y)
plt.xlabel("Time [s]")
plt.ylabel("Step Response")
plt.xlim([0, 40])
plt.grid(True)
plt.savefig('../img/fig2_2.png', dpi=300)



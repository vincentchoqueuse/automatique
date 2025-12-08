import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode, nichols_grid, feedback, step_response

# Parameters
K = 27
a = 0.09
T = 0.111

w_m = 1/(T*np.sqrt(a))


# Transfer function of PI: Kp * (1 + wi/s)
C_s_0 = tf([T, 1], [a*T, 1])
C_s_1 = K * tf([T, 1], [a*T, 1])
G_s = tf([10], [1, 1.8, 1])

H_bo1 = G_s
H_bo2 = C_s_0*G_s
H_bo3 = C_s_1*G_s
H_bf3 = feedback(H_bo3, 1)

# Compute bode response
omega = np.logspace(-2, 3.5, 400)
mag1, phase1, omega1 = H_bo1.frequency_response(omega=omega)
mag2, phase2, omega2 = H_bo2.frequency_response(omega=omega)
mag3, phase3, omega3 = H_bo3.frequency_response(omega=omega)

magD, phaseD, omegaD = H_bo1.frequency_response(omega=[w_m])
magI, phaseI, omegaI = H_bo2.frequency_response(omega=[w_m])
magA, phaseA, omegaA = H_bo3.frequency_response(omega=[w_m])

# figure 1
plt.figure(figsize=(10, 6))
plt.plot(180*np.unwrap(phase1)/np.pi, 20*np.log10(mag1), label="$G(s)$")
plt.plot(180*np.unwrap(phaseD)/np.pi, 20*np.log10(magD), "ko")
plt.text(180*np.unwrap(phaseD)/np.pi, 20*np.log10(magD), r"$\omega_m$", color="black")
cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])
nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

plt.plot([-360, 0], [0, 0], 'k--')          # 0 dB
plt.plot([-120, -120], [-60, 30], 'k--')   
plt.scatter(-180, 0, color="r", s=50)       # point critique -180°, 0 dB

# Mise en forme
plt.xlabel("Phase (deg)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])
plt.ylim([-60, 30])
plt.grid(True)
plt.legend()

plt.savefig('../img/fig2_1.png', dpi=300)


# figure 2
plt.figure(figsize=(10, 6))
plt.plot(180*np.unwrap(phase1)/np.pi, 20*np.log10(mag1), label="$G(s)$")
plt.plot(180*np.unwrap(phase2)/np.pi, 20*np.log10(mag2), label="$C_{av1}(s)G(s)$")
plt.plot(180*np.unwrap(phaseI)/np.pi, 20*np.log10(magI), "ko")
plt.text(180*np.unwrap(phaseI)/np.pi, 20*np.log10(magI), r"  $\omega_m$", color="black")
cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])
nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

plt.plot([-360, 0], [0, 0], 'k--')          # 0 dB
plt.plot([-120, -120], [-60, 30], 'k--')    # repère -135°
plt.scatter(-180, 0, color="r", s=50)       # point critique -180°, 0 dB

# Mise en forme
plt.xlabel("Phase (deg)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])
plt.ylim([-60, 30])
plt.grid(True)
plt.legend()

plt.savefig('../img/fig2_2.png', dpi=300)


# figure 3
plt.figure(figsize=(10, 6))
plt.plot(180*np.unwrap(phase2)/np.pi, 20*np.log10(mag2), label="$C_{av1}(s)G(s)$")
plt.plot(180*np.unwrap(phase3)/np.pi, 20*np.log10(mag3), label="$C_{av}(s)G(s)$")
plt.plot(180*np.unwrap(phaseA)/np.pi, 20*np.log10(magA),"ko")
plt.text(180*np.unwrap(phaseA)/np.pi, 20*np.log10(magA), r"  $\omega_m$", color="r")
cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])
nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

plt.plot([-360, 0], [0, 0], 'k--')          # 0 dB
plt.plot([-120, -120], [-60, 30], 'k--')    # repère -135°
plt.scatter(-180, 0, color="r", s=50)       # point critique -180°, 0 dB

# Mise en forme
plt.xlabel("Phase (deg)")
plt.ylabel("Magnitude (dB)")
plt.xlim([-360, 0])
plt.ylim([-60, 30])
plt.grid(True)
plt.legend()

plt.savefig('../img/fig2_3.png', dpi=300)



plt.figure()
t, y = step_response(H_bf3)
plt.plot(t, y)
plt.xlim([0, 0.5])
plt.ylim([0, 1.2])
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.savefig('../img/fig2_4.png', dpi=300)
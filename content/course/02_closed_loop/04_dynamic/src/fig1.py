import control as ct
import matplotlib.pyplot as plt
import numpy as np

cl_mags = np.array([20, 10, 6, 3, 1, 0, -1, -3, -6, -10, -20, -30])
cl_phases = np.array([-10, -45, -90, -180, -235, -270, -315, -350])


ct.nichols_grid(cl_mags=cl_mags, cl_phases=None, line_style='solid')

# Axis limits and labels
plt.xlabel("Phase (degrees)")
plt.ylabel("Magnitude (dB)")
plt.tight_layout()

# Save the figure
plt.savefig('../img/fig1.png', dpi=300)


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

# Define poles and zeros for the two systems
poles_system1 = [-0.5, -2.5, -3+1j, -3-1j, -4]  # All poles in the left-half plane
poles_system2 = [0.5, -2.5, -3+1j, -3-1j, -4]   # One pole in the right-half plane
zeros = [-1, -2]  # Zeros for both systems

# Create transfer functions
num = np.poly(zeros)
den_system1 = np.poly(poles_system1)
den_system2 = np.poly(poles_system2)
system1 = TransferFunction(num, den_system1)
system2 = TransferFunction(num, den_system2)

for index, system in enumerate([system1, system2]):

    t, y = step(system)

    # Plot setup
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # System 1: Stable system
    axes[0].plot(system.poles.real, system.poles.imag, 'x', label="Poles", markersize=10)
    axes[0].plot(system.zeros.real, system.zeros.imag, 'o', label="Zeros", markersize=8)
    axes[0].set_title("Poles and Zeros")
    axes[0].set_xlabel("Re")
    axes[0].set_ylabel("Im")
    axes[0].grid(True)
    axes[0].axis("equal")
    axes[0].set_xlim([-5, 1])
    axes[0].legend()

    axes[1].plot(t, y, label="Step Response")
    axes[1].set_title("Step Response")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)
    axes[1].legend()
    axes[1].set_xlim([0, 14])

    plt.savefig(f'../img/fig1_{index+1}.png', dpi=300)

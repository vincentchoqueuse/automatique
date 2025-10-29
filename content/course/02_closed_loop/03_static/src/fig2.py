import numpy as np
from control import tf, feedback, forced_response
import control
import matplotlib.pyplot as plt

K = 2
G_list = [
    tf([0.1*K],[1, 10, 1]),
    tf([0.1*K],[1, 10, 1, 0])
]

E = 1
t = np.arange(0, 100, 0.1)
plt.plot(t, E*t*(t>=0), label="$u(t)$")
for L, G in enumerate(G_list):
    H = feedback(G, 1)
    # Compute step response
    t, y =  forced_response(H, T=t, U=E*t)
    # Plot
    plt.plot(t, E*y, label=f"$G(s)$: classe L={L}")

plt.xlim([0, 100])
plt.ylim([0, 100])
plt.xlabel("Time [s]")
plt.grid(True)
plt.legend()

plt.savefig(f'../img/fig2.png', dpi=300)

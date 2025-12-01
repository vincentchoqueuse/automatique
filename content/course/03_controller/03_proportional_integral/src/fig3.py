import numpy as np
import matplotlib.pyplot as plt
from control import tf, feedback, step_response, bode, nichols_grid

# -----------------------------
# Paramètres
# -----------------------------
Kp = 6/4
wi = 0.16073226011609948

G = tf([1.5], [1, 1, 1])

H = feedback(G, 1)
H_p = feedback(Kp * G, 1)

C_pi = Kp * tf([1, wi], [1, 0])
H_pi = feedback(C_pi* G, 1)

names = ["$G(s)$", "$K_p G(s)$", "$C_{pi} G(s)$"]

plt.figure(figsize=(10, 6))
for index, sys in enumerate([H, H_p, H_pi]):
    t, y = step_response(sys)
    plt.plot(t, y, label=names[index])

# Mise en forme
plt.xlabel("temps (s)")
plt.xlim([0, 20])
plt.grid(True)
plt.legend()

plt.savefig('../img/fig3.png', dpi=300)
plt.show()


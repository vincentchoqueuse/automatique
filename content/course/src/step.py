import matplotlib.pyplot as plt
from control.matlab import tf, step

K = 1
tau = 3
H = tf([K], [tau, 1])
s, t = step(H)
plt.plot(t, s)
plt.xlabel("temps [s]")
plt.ylabel("y(t)")
plt.grid()
plt.show()
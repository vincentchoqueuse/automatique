# Python Cheatsheet


## Plotting


### Poles and zeros diagram

```python
import matplotlib.pyplot as plt
from control import tf

# Define the transfer function directly
H = tf([2], [3, 1])  # H(s) = 2 / (3s + 1)

# Compute poles and zeros
poles = H.poles()
zeros = H.zeros()

# Plot
plt.scatter(zeros.real, zeros.imag, marker='o', label='Zeros')
plt.scatter(poles.real, poles.imag, marker='x', label='Poles')
plt.xlabel("Real Part")
plt.ylabel("Imag Part")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("Pole-Zero Diagram")
```

### Step Response

```python
import matplotlib.pyplot as plt
from control import tf, step_response

# Define the transfer function directly
H = tf([2], [3, 1])  # H(s) = 2 / (3s + 1)

# Compute step response
E = 2
t, y =  step_response(H)

# Plot
plt.plot(t, E*y)
plt.xlabel("Time [s]")
plt.ylabel("Step Response")
plt.grid(True)
plt.title("Step Response")
```

### Bode Plot

```python
import matplotlib.pyplot as plt
from control import tf,  bode

# Define the transfer function directly
H = tf([2], [3, 1])  # H(s) = 2 / (3s + 1)

# Compute bode response
mag, phase, omega = bode(H, plot=False)

# Plot
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True)

ax_mag.semilogx(omega, 20*np.log10(mag))
ax_mag.set_ylabel('Magnitude [dB]')
ax_mag.grid()

ax_phase.semilogx(omega, (180*phase)/np.pi)
ax_phase.set_xlabel('Frequency [rad/s]')
ax_phase.set_ylabel('Phase [deg]')
ax_phase.grid()
plt.tight_layout()
```

### Black-Nichols Diagram

```python
import matplotlib.pyplot as plt
from control import tf,  plot

# Define the transfer function directly
H = tf([2], [3, 1])  # H(s) = 2 / (3s + 1)

# Compute bode response
mag, phase, omega = bode(H, plot=False)

# Plot
plt.plot((180*phase)/np.pi, 20*np.log10(mag))
plt.xlabel('Phase [deg]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.tight_layout()
```



## Closed Loop System

```python
import matplotlib.pyplot as plt
from control import tf, feedback

# system
H = tf([2], [5, 1])

# closed loop system with correction
G = 3/2
H_cl = feedback(G*H, 1)
```
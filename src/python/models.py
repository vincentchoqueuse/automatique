# models.py
import numpy as np
from scipy import signal

class LTISystem:
    """Classe de base pour un système LTI continu."""
    def __init__(self):
        self.system = None

    def get_time_vector(self, n_points=1000):
        """Détermine automatiquement la durée de simulation à partir des pôles."""
        poles = np.abs(np.real(self.system.poles))
        if len(poles) == 0:
            t_end = 10
        else:
            t_end = 5 * (1 / np.min(poles[poles > 0])) if np.any(poles > 0) else 10
        return np.linspace(0, t_end, n_points)

    def get_freq_vector(self, n_points=500):
        """Détermine automatiquement l’échelle fréquentielle utile."""
        poles = np.abs(self.system.poles)
        if len(poles) == 0:
            wmin, wmax = 1e-2, 1e2
        else:
            wmin = np.min(poles) / 100
            wmax = np.max(poles) * 100
        return np.logspace(np.log10(wmin), np.log10(wmax), n_points)

    def step_response(self, amplitude=1.0):
        t = self.get_time_vector()
        t_out, y = self.system.step(T=t)
        return t_out, y * amplitude

    def impulse_response(self):
        t = self.get_time_vector()
        t_out, y = self.system.impulse(T=t)
        return t_out, y

    def bode_response(self):
        w = self.get_freq_vector()
        w, mag, phase = self.system.bode(w)
        return w, mag, phase

    def black_response(self):
        w = self.get_freq_vector()
        w, H = signal.freqresp(self.system, w=w)
        mag = 20 * np.log10(np.abs(H))
        phase = np.angle(H, deg=True)
        return w, phase, mag


class FirstOrderSystem(LTISystem):
    """Système du premier ordre : G(s) = K / (tau*s + 1)"""
    def __init__(self, K, tau):
        super().__init__()
        self.K = K
        self.tau = tau
        self.system = signal.lti([K], [tau, 1])


class SecondOrderSystem(LTISystem):
    """Système du second ordre : G(s) = K * wn² / (s² + 2ζwn*s + wn²)"""
    def __init__(self, K, zeta, wn):
        super().__init__()
        self.K = K
        self.zeta = zeta
        self.wn = wn
        num = [K * wn**2]
        den = [1, 2 * zeta * wn, wn**2]
        self.system = signal.lti(num, den)

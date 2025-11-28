# Fast generation of three interactive HTML plots:
# 1) Overshoot vs zeta
# 2) Settling time (±5%) vs ω_n and zeta (analytical/approx formulas for speed)
# 3) Resonance factor vs zeta
import numpy as np
from scipy import signal
import plotly.graph_objects as go
import plotly.io as pio
import os


def settling_time_5_percent(zeta, wn=1.0, amplitude=1.0):
    """Calcule numériquement le temps de réponse à ±5 % pour un second ordre."""
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    system = signal.lti(num, den)

    tout, y = signal.step(system, N=1000)
    y *= amplitude

    # Valeur finale attendue = amplitude * gain statique = amplitude
    y_final = amplitude
    err = np.abs(y - y_final) / np.abs(y_final)

    within = err <= 0.05
    if not np.any(within):
        return np.nan
    # Cherche la dernière violation du critère ±5 %
    last_violate = np.max(np.where(~within)[0]) if np.any(~within) else -1
    if last_violate >= len(tout) - 1:
        return np.nan
    return tout[last_violate + 1]


folder = "../../public/lookup_charts"
os.makedirs(folder, exist_ok=True)

# ---------- 1) Overshoot vs zeta ----------
zeta = np.linspace(0.01, 1.5, 600)
Mp = np.zeros_like(zeta)
mask_ud = zeta < 1.0
Mp[mask_ud] = np.exp(-np.pi * zeta[mask_ud] / np.sqrt(1 - zeta[mask_ud]**2))

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=zeta, y=100*Mp, mode="lines",
    name="Mₚ(%)",
    hovertemplate="ζ = %{x:.3f}<br>Mₚ = %{y:.2f}%<extra></extra>"
))
fig1.update_layout(
    title="Premier dépassement relatif Mₚ (%) en fonction de ζ",
    xaxis_title="ζ (facteur d'amortissement)",
    yaxis_title="Mₚ (%)"
)
out1 = f"{folder}/overshoot.html"
pio.write_html(fig1, file=out1, auto_open=False, include_plotlyjs="cdn")

# second charts

wn = 1.0  # pulsation naturelle en rad/s
zeta_values = np.logspace(-1, 1, 200) 

Ts = []
for z in zeta_values:
    Ts.append(settling_time_5_percent(z, wn=wn))
Ts = np.array(Ts)

# --- Création du graphique Plotly ---
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=zeta_values,
    y=Ts,
    mode="lines",
    name="Tₛ,5%",
    hovertemplate="ζ = %{x:.3f}<br>ωₙTₛ = %{y:.3f} s<extra></extra>"
))

fig2.update_layout(
    title="(Normalized) Settling time vs damping ratio",
    xaxis=dict(
        title="ζ (damping ratio)",
        type="log"
    ),
    yaxis=dict(
        title="ωₙTₛ",
        type="log"
    ),
    template="plotly_white"
)

out2 = f"{folder}/settling_time.html"
pio.write_html(fig2, file=out2, auto_open=False, include_plotlyjs="cdn")


# ---------- 3) Resonance factor M_r vs zeta ----------
zeta_r = np.linspace(0.01, 1.2, 600)
Mr = np.full_like(zeta_r, np.nan, dtype=float)
limit = 1/np.sqrt(2)
mask = zeta_r < limit
Mr[mask] = 1.0 / (2.0 * zeta_r[mask] * np.sqrt(1 - zeta_r[mask]**2))
Mr_dB = 20 * np.log10(Mr)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=zeta_r,
    y=Mr_dB,
    mode="lines",
    name="M_r (dB)",
    hovertemplate="ζ = %{x:.3f}<br>M_r = %{y:.2f} dB<extra></extra>"
))
fig3.add_vline(
    x=limit,
    line_dash="dash",
    annotation_text="ζ = 1/√2",
    annotation_position="top right"
)
fig3.update_layout(
    title="Facteur de résonance M_r (dB) en fonction de ζ",
    xaxis_title="ζ (damping ratio)",
    yaxis_title="M_r (dB)"
)

out3 = f"{folder}/resonance_factor.html"
pio.write_html(fig3, file=out3, auto_open=False, include_plotlyjs="cdn")


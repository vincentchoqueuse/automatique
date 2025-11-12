# plotter.py
import plotly.graph_objects as go
import plotly.io as pio

class SystemPlotter:
    """Classe utilitaire pour afficher et enregistrer les réponses Plotly."""
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir

    def plot_step(self, name, t, y, amplitude):
        u = [amplitude] * len(t)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=u, mode="lines", name="Consigne", line=dict(dash="dash")))
        fig.add_trace(go.Scatter(x=t, y=y, mode="lines", name="Réponse système"))
        fig.update_layout(title=f"Réponse indicielle — {name}", xaxis_title="Temps (s)", yaxis_title="Amplitude")
        pio.write_html(fig, f"{self.output_dir}/{name}_step.html", include_plotlyjs="cdn")

    def plot_impulse(self, name, t, y):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=y, mode="lines", name="Réponse impulsionnelle"))
        fig.update_layout(title=f"Réponse impulsionnelle — {name}", xaxis_title="Temps (s)", yaxis_title="Amplitude")
        pio.write_html(fig, f"{self.output_dir}/{name}_impulse.html", include_plotlyjs="cdn")

    def plot_bode(self, name, w, mag, phase):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=w, y=mag, mode="lines", name="Gain (dB)"))
        fig.add_trace(go.Scatter(x=w, y=phase, mode="lines", name="Phase (°)", yaxis="y2"))
        fig.update_layout(
            title=f"Diagramme de Bode — {name}",
            xaxis=dict(title="Pulsation (rad/s)", type="log"),
            yaxis=dict(title="Gain (dB)"),
            yaxis2=dict(title="Phase (°)", overlaying="y", side="right"),
        )
        pio.write_html(fig, f"{self.output_dir}/{name}_bode.html", include_plotlyjs="cdn")

    def plot_black(self, name, w, phase, mag):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=phase,
            y=mag,
            mode="lines",
            name="Black",
            customdata=w,  # attach angular frequency to each point
            hovertemplate=(
                "Phase: %{x:.2f}°<br>"
                "Gain: %{y:.2f} dB<br>"
                "ω: %{customdata:.3f} rad/s<br>"
                "<extra></extra>"  # hides the default trace name box
            )
        ))
        fig.update_layout(
            title=f"Diagramme de Black — {name}",
            xaxis_title="Phase (°)",
            yaxis_title="Gain (dB)"
        )
        pio.write_html(fig, f"{self.output_dir}/{name}_black.html", include_plotlyjs="cdn")

# build_from_json.py
import os
import json
import numpy as np
from control import tf, feedback
from control_plotly import bode, nichols, step

# Charger la configuration
with open("systems_nichols.json") as f:
    systems = json.load(f)

# Créer le dossier de sortie
folder = "../../public/aav2"
os.makedirs(folder, exist_ok=True)

for sys in systems:
    id = sys["id"]
    name = sys["name"]
    params = sys["params"]
    num = params["num"]
    den = params["den"]
    w_param = sys.get("w")
    if w_param:
        w = np.logspace(w_param["min"], w_param["max"], 400)
    else:
        w = None

    sys = tf(num, den)
    sys_cl = feedback(sys, 1)

    # step response open loop
    fig = step(sys)
    fig.update_layout(title=f"Step response (open loop): {name}", height=None, autosize=True)
    fig.write_html(f"{folder}/{id}_step_ol.html", include_plotlyjs="cdn")

    fig = bode(sys, w=w)
    fig.update_layout(title=f"Bode diagram (open loop): {name}", height=None, autosize=True)
    fig.write_html(f"{folder}/{id}_bode_ol.html", include_plotlyjs="cdn")

    fig = nichols(sys, w=w)
    fig.update_layout(title=f"Nichols diagram (open loop): {name}", height=None, autosize=True)
    fig.write_html(f"{folder}/{id}_nichols_ol.html", include_plotlyjs="cdn")

    fig = step(sys_cl)
    fig.update_layout(title=f"Step response (closed loop): {name}", height=None, autosize=True)
    fig.write_html(f"{folder}/{id}_step_cl.html", include_plotlyjs="cdn")

    fig = bode(sys_cl)
    fig.update_layout(title=f"Bode diagram (closed loop): {name}", height=None, autosize=True)
    fig.write_html(f"{folder}/{id}_bode_cl.html", include_plotlyjs="cdn")


print("✅ Tous les graphiques générés dans /outputs")

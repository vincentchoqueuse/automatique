# build_from_json.py
import os
import json
from python_control import bode, nichols, step

# Charger la configuration
with open("systems_nichols.json") as f:
    systems = json.load(f)

# Créer le dossier de sortie
folder = "../../public/aav2"
os.makedirs(folder, exist_ok=True)
plotter = SystemPlotter(folder)

for sys in systems:
    name = sys["name"]
    s_type = sys["type"]
    params = sys["params"]

    if s_type == 1:
        system = FirstOrderSystem(params["K"], params["tau"])
    elif s_type == 2:
        system = SecondOrderSystem(params["K"], params["zeta"], params["wn"])
    else:
        print(f"⚠️ Type inconnu pour {name}, ignoré.")
        continue

    for resp in sys["response"]:
        rtype = resp["type"]

        if rtype == "step":
            t, y = system.step_response(amplitude=resp["input"])
            plotter.plot_step(name, t, y, resp["input"])

        elif rtype == "impulse":
            t, y = system.impulse_response()
            plotter.plot_impulse(name, t, y)

        elif rtype == "bode":
            w, mag, phase = system.bode_response()
            plotter.plot_bode(name, w, mag, phase)

        elif rtype == "black":
            w, phase, mag = system.black_response()
            plotter.plot_black(name, w, phase, mag)

print("✅ Tous les graphiques générés dans /outputs")

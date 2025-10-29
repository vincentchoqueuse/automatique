# Affichage de la réponse indicielle en Python 

Pour ce tutoriel, nous allons implémenter une simulation de la réponse indicielle d'un système dynamique en utilisant les bibliothèques `matplotlib` et `control` en Python. Le but est de représenter graphiquement la réponse du système suite à une excitation de type échelon, en utilisant la bibliothèque `control` pour modéliser le système et `matplotlib` pour les représentations graphiques.

## Méthodologie

### Importer les bibliothèques nécessaires
Nous allons commencer par importer les bibliothèques Python que nous allons utiliser :
```python
import numpy as np
import matplotlib.pyplot as plt
from control import tf, step_response
```

- `numpy` est utilisé pour la gestion des vecteurs et matrices.
- `matplotlib.pyplot` est utilisé pour la création de graphiques.
- `control` est utilisé pour modéliser des systèmes dynamiques linéaires.

### Créer la fonction de transfert
Nous allons définir la fonction de transfert du système. Dans cet exemple, nous avons un système avec une fonction de transfert de la forme :

$$ H(s) = \frac{2}{0.5s^2 + s + 1} $$

Pour implémenter cela en Python avec la bibliothèque `control` :
```python
H = tf([2], [0.5, 1, 1])
```
- Le premier argument représente le numérateur (ici `[2]`).
- Le deuxième argument représente le dénominateur du polynôme caractéristique (ici `[0.5, 1, 1]`).

### Calculer la réponse indicielle
Ensuite, nous allons calculer la réponse indicielle du système. Utilisons la fonction `step_response` pour obtenir la réponse d'un échelon unitaire.

```python
t, s = step_response(H)
```
- `t` représente le vecteur temps.
- `s` représente la réponse du système pour une entrée échelon unitaire.

### Tracer la réponse indicielle
Nous pouvons maintenant tracer la réponse du système avec `matplotlib` :

```python
plt.figure()
plt.plot(t, s, label="Réponse indicielle (Python)")
plt.xlabel("Temps (s)")
plt.ylabel("Sortie")
plt.grid()
plt.legend()
plt.show()
```
- `plt.plot(t, s, ...)` trace la réponse du système en fonction du temps.
- Les labels des axes sont définis avec `plt.xlabel` et `plt.ylabel`.
- La fonction `plt.grid()` ajoute une grille pour faciliter la lecture du graphique.
- `plt.legend()` ajoute une légende au graphique pour identifier la courbe.

Vous verrez apparaître une figure qui montre l'évolution de la sortie du système dans le temps après avoir été excité par un signal échelon unitaire. Cette simulation est très utile pour comprendre comment un système répond à une entrée échelon et pour valider des modèles.

## Code Complet

Ce tutoriel vous a montré comment créer un système dynamique en Python, calculer sa réponse indicielle et visualiser cette réponse avec `matplotlib`. Voici un résumé du code :

```python
import numpy as np
import matplotlib.pyplot as plt
from control import tf, step_response

# Définir la fonction de transfert
H = tf([2], [0.5, 1, 1])

# Calculer la réponse indicielle
t, s = step_response(H)

# Tracer la réponse indicielle
plt.figure()
plt.plot(t, s, label="Réponse indicielle (Python)")
plt.xlabel("Temps (s)")
plt.ylabel("Sortie")
plt.grid()
plt.legend()
plt.show()
```


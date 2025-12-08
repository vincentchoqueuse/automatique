---
outline: [2,3]
---

# Liste des correcteurs 

## Contexte

Pour corriger un système, une stratégie possible consiste à ajouter un correcteur dans la boucle ouverte.

<figure>
    <img src="./img/sys_closed4.png" width="410">
    <figcaption>Système bouclé intégrant un correcteur</figcaption>
</figure>

* $C(s)=U(s)/\epsilon(s)$: fonction de transfert du correcteur où $U(s)$ correspond à la transformée de Laplace du signal de commande,
* $G(s)=Y(s)/U(s)$: fonction de transfert du système non corrigé ou système à corriger,
* $H_{bo}(s)=C(s)G(s)$: fonction de transfert de la boucle ouverte,
* $H_{bf}(s)= H_{bo}(s) / (1+ H_{bo}(s))$: fonction de transfert de la boucle fermée.

## Liste des correcteurs et objectifs


Dans ce chapitre, nous allons considérer les correcteurs:

* correcteur Proportionnel (P),
* Correcteur Proportionnel-Intégral (PI),
* Correcteur par Avance de Phase (AP),
* Correcteur Proportionnel Intégral-Dérivateur (PID).

Chaque correcteur dépend d'un ou de plusieurs paramètres que l'utilisateur peut régler afin de respecter les contraintes d'un cahier des charges. Dans ce chapitre, nous présentons différentes techniques de réglage basées sur le lieu de Black (Nichols) en boucle ouverte.

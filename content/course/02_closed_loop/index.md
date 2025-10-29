# Introduction

Ce chapitre développe une méthodologie complète pour analyser le comportement d’un système en boucle fermée :

*  Stabilité : lien entre pôles et stabilité, critère du revers, marges de robustesse.
* Performances statiques : influence de la classe du système sur la précision et le rejet des perturbations.
* Performances dynamiques : estimation graphique des paramètres temporels via l’abaque de Black-Nichols et l’approximation second ordre.

Cette section forme une progression logique allant de la sécurité de fonctionnement (stabilité), à la qualité en régime permanent (précision et robustesse), jusqu’à la qualité transitoire (rapidité et amortissement).

## Hypothèses

L'ensemble de ce chapitre considère que **le retour est unitaire**. Si cette condition n'est pas respectée, il sera nécessaire de manipuler le schéma-bloc au préalable.


<figure>
    <img src="./img/sys_closed2.png" width="350">
    <figcaption>Système bouclé avec un Retour Unitaire</figcaption>
</figure>

* $G(s)$: fonction de transfert du système en **boucle ouverte**,
* $H(s)= \frac{G(s}{1+G(s)}$ : fonction de transfert du système en **boucle fermée**.
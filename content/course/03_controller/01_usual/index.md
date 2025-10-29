---
outline: [2,3]
---

# Liste des correcteurs 

## Contexte

Pour corriger un système, une stratégie possible consiste à ajouter un correcteur dans la boucle ouverte.

<figure>
    <img src="./img/sys_closed3.png" width="410">
    <figcaption>Système bouclé intégrant un correcteur</figcaption>
</figure>

* $C(s)$: fonction de transfert du correcteur,
* $F(s)$: fonction de transfert du système à corriger,
* $G(s)=C(s)F(s)$: fonction de transfert de la boucle ouverte.

Dans ce chapitre, nous allons considérer différents correcteurs usuels.

## Correcteurs Usuels

### Correcteur Proportionnel (P)

#### Fonction de transfert

La fonction de transfert d'un correcteur proportionnel est donnée par :

$$C_p(s)=K$$

* $K>0$: gain ou gain proportionnel.

#### Avantages et inconvénients

**Avantages :**
- Simple à implémenter et à régler.
- Augmente la rapidité de réponse en boucle fermée.

**Inconvénients :**
- N'élimine pas l'erreur statique (erreur résiduelle possible pour une entrée en échelon).


### Correcteur Proportionnel-Intégral (PI)

#### Fonction de transfert

La fonction de transfert d'un correcteur proportionnel-intégral est donnée par :

$$C_{pi}(s)=K_p + \frac{K_i}{s}$$

* $K_p$: gain proportionnel,
* $K_i$: gain intégral.

#### Diagramme de Bode

<figure>
    <img src="./img/fig1_PI.png" width="600">
    <figcaption>Diagramme de Bode d'un correcteur PI</figcaption>
</figure>

L'action intégrale du correcteur PI permet d'apporter du gain en basse-fréquence (diminution de l'erreur en régime permanent). Ce correcteur enlève néanmoins de la phase en basse-fréquence (diminution des marges de phase et de gain)


#### Avantages et inconvénients

**Avantages :**
- Élimine l'erreur statique pour une entrée en échelon (ajout d'un intégrateur dans la boucle ouverte)
- Simple à régler avec des méthodes comme Ziegler-Nichols.

**Inconvénients :**
- Peut ralentir la réponse transitoire (phénomène de dépassement ou d'oscillations).
- Peut déstabiliser le système en boucle fermée si les paramètres sont mal réglés.

### Correcteur Proportionnel-Dérivateur (PID)

#### Fonction de transfert

La fonction de transfert d'un correcteur proportionnel-intégral-dérivateur est donnée par :

$$C(s)=K_p + \frac{K_i}{s} + K_d s$$

* $K_p$: gain du correcteur proportionnel,
* $K_i$: gain de l'action intégrale.
* $K_i$: gain de l'action dérivée.

#### Diagramme de Bode

<figure>
    <img src="./img/fig1_PID.png" width="600">
    <figcaption>Diagramme de Bode d'un correcteur PID</figcaption>
</figure>

Lorsqu'il est bien réglé, un correcteur PID permet à la fois d'apporter du gain en basse-fréquence et d'ajouter de la phase en haute fréquence.

#### Avantages et inconvénients

**Avantages :**
- Combine les avantages des correcteurs P, I et D.
- Élimine l'erreur statique, améliore la stabilité et réduit les oscillations.
- Convient à une large gamme de systèmes.

**Inconvénients :**
- Plus complexe à régler (besoin de méthodes adaptées).
- Sensible au bruit (composante dérivée).



### Correcteur par Avance de Phase

#### Fonction de transfert

La fonction de transfert d'un correcteur à avance de phase est donnée par :

$$C(s)=K \frac{1+aTs}{1+Ts}$$

* $a> 1$: terme permettant d'ajouter de la phase,
* $K$: gain du correcteur,
* $T>0$: constante de temps du correcteur.


#### Diagramme de Bode

L’avance de phase maximale apportée par le correcteur est donnée par :

$$\varphi_{max} = \sin^{-1}\left(\frac{a-1}{a+1} \right)$$

et se produit à la pulsation 

$$\omega_{max} = \frac{1}{T\sqrt{a}}$$

::: details Demonstration : Propriétés du correcteur par avance de phase

En fréquentiel ($s = j\omega$), nous obtenons:
$$
C(j\omega) = K\,\frac{1 + j a T \omega}{1 + j T \omega}.$$

La phase apportée par le correcteur vaut :
$$
\varphi(\omega) = \arg\!\big(1 + j a T \omega\big) - \arg\!\big(1 + j T \omega\big)
= \arctan\!\big(a T \omega\big) - \arctan\!\big(T \omega\big).
$$

Pour rechercher $\varphi_{\max}$, nous allons annuler la dérivée de $\varphi(\omega)$ par rapport à $\omega$. Nous trouvons
$$
\left.\frac{d\varphi}{d\omega}\right|_{\omega=\omega_{max}}=0 \Rightarrow
\frac{aT}{1+(aT\omega_{max})^2} - \frac{T}{1+(T\omega_{max})^2} = 0.
$$

Il en vient que :
$$
a-1 = a(a-1)(T\omega_{max})^2\Rightarrow (T\omega_{max})^2 = \frac{1}{a}
$$ 
Finalement, la phase est maximale pour 
$$
\omega_{max} = \frac{1}{T\sqrt{a}}
$$
Pour cette valeur, la phase est égale à :

$$\varphi_{\max} = \arctan(\sqrt{a}) - \arctan\!\Big(\frac{1}{\sqrt{a}}\Big).$$

En utilisant les propriétés de la fonction $\arctan$, il est possible d'écrire cette expression sous forme plus compacte :

$$ \varphi_{\max} = \arcsin\!\left(\frac{a-1}{a+1}\right)$$

:::

<figure>
    <img src="./img/fig1_PID.png" width="600">
    <figcaption>Diagramme de Bode d'un correcteur PID</figcaption>
</figure>

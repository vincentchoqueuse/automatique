# Réponse Indicielle d'un Système de Premier Ordre

## Objectif

Considérons un système de premier ordre régit par l'équation différentielle suivante pour :
$$\tau \frac{dy(t)}{dt} + y(t) = K u(t)$$

où :
* $\tau$ est la constante de temps du système,
* $K$ est le gain du système,
* $y(t)$ est la sortie du système,
* $u(t)$ est l'entrée du système.


Dans ce tutorial, nous montrons comment calculer la réponse indicielle d'un système de premier ordre avec 3 techniques différentes.

## 1. Approche Directe basée sur l'équation différentielle

### Équation sans second membre

Pour résoudre cette équation différentielle de manière analytique, nous devons d'abord résoudre l'équation homogène (sans second membre) :

$$\tau \frac{dy_h(t)}{dt} + y_h(t) = 0 $$

Il est possible de vérifier que la solution de cette équation homogène est :

$$y_h(t) = A e^{-t/\tau}$$

### Solution particulière

Pour une entrée échelon unitaire $u(t) = 1$, nous cherchons une solution particulière constante de type $y_p(t) = y_p$. En substituant $y_p$ dans l'équation différentielle, nous obtenons :

$$y_p = K$$

### Solution générale

La solution générale de l'équation différentielle est la somme de la solution homogène et de la solution particulière :

$$y(t) = y_h(t) + y_p = A e^{-t/\tau} + K$$

En appliquant la condition initiale $y(0) = 0$, nous trouvons $A$ :

$$y(0) = A + K = 0 \Rightarrow A = -K$$

Donc, la solution est :

$$y(t) = K (1 - e^{-t/\tau})$$

## 2. Approche par la Convolution

### Réponse impulsionnelle

Pour obtenir la réponse impulsionnelle, il faut également utiliser l'approche directe. Lorsque l'entrée est une impulsion, la solution générale s'exprime sous la forme :

$$h(t) = A e^{-t/\tau}$$

L'obtention du coefficient $A$ est plus technique est nécessite d'intégrer l'équation différentielle au voisinage de 0. Après quelques calculs, nous obtenons :

$$h(t) = \frac{K}{\tau} e^{-t/\tau}$$

::: details Démonstration

En intégrant l'équation différentielle autour de $t = 0$ sur un intervalle infinitésimal $[-\epsilon, \epsilon]$ et en prenant la limite $\epsilon \to 0$, nous obtenons :

$$\int_{-\epsilon}^{\epsilon} \left( \tau \frac{dh(t)}{dt} + h(t) \right) dt = \int_{-\epsilon}^{\epsilon} K \delta(t) dt $$

En utilisant la définition du Dirac, nous obtenons :

$$\tau \left[ h(t) \right]_{-\epsilon}^{\epsilon} + \int_{-\epsilon}^{\epsilon} h(t) dt = K$$

Comme $h(t)$ est continue partout sauf en $t = 0$ et en supposant que $h(t)$ est bornée, l'intégrale de $h(t)$ sur un intervalle infinitésimal est négligeable et donc $\tau \left( h(\epsilon) - h(-\epsilon) \right) = K$. En prenant la limite $\epsilon \to 0$, et sachant que $h(-\epsilon) = 0$ pour $t < 0$ (puisque le système est causal et ne peut pas répondre avant l'application de l'impulsion), nous obtenons finalement $\tau h(0^+) = K$, ce qui implique que :

$$h(0^+) = \frac{K}{\tau}$$

La réponse impulsionnelle $h(t)$ d'un système de premier ordre est donnée par :

$$h(t) = \frac{K}{\tau} e^{-t/\tau}$$

:::

### Produit de convolution

La sortie $y(t)$ pour une entrée échelon unitaire $u(t)$ est donnée par le produit de convolution :

$$y(t) = (u * h)(t) = \int_{0}^{t} u(\tau) h(t - \tau)d\tau$$

En substituant $u(\tau) = 1$ et $h(t - \tau) = \frac{K}{\tau} e^{-(t - \tau)/\tau}$, nous obtenons :

$$
\begin{align}
y(t) &= \int_{0}^{t} \frac{K}{\tau} e^{-(t - \tau)/\tau} d\tau \\
&= \frac{K}{\tau} e^{-t/\tau} \int_{0}^{t} e^{\tau/\tau} d\tau \\
&= \frac{K}{\tau} e^{-t/\tau} \left[ e^{\tau/\tau} \right]_{0}^{t} \\
&= \frac{K}{\tau} e^{-t/\tau} (e^{t/\tau} - 1) \\
&= K (1 - e^{-t/\tau})
\end{align}
$$

## 3. Approche par la Transformée de Laplace

#### Transformée de Laplace

En appliquant la transformée de Laplace aux deux membres de l'équation différentielle, nous obtenons : 

$$\tau s Y(s) + Y(s) = K \frac{1}{s}$$

En factorisant $Y(s)$, il en vient que :

$$Y(s) (\tau s + 1) = \frac{K}{s}$$

Finalement,

$$Y(s) = \frac{K}{s (\tau s + 1)}$$

#### Transformation inverse

Pour trouver $y(t)$, nous devons appliquer la transformée de Laplace inverse à $Y(s)$. En décomposant la fraction, nous obtenons :

$$Y(s) = \frac{K}{\tau} \left( \frac{1}{s} - \frac{1}{s + 1/\tau} \right)$$

En appliquant la transformée de Laplace inverse à chaque membre, nous obtenons :

$$y(t) = K \left( 1 - e^{-t/\tau} \right)$$

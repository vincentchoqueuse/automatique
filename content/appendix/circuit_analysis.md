---
outline: [2,3]
---

# Rappels d'Electronique

## Objectif

Ces rappels présentent les bases de la mise en équation des circuits électroniques.

## Dipôles de Base

### Résistance

<figure>
    <img src="./img/resistor.svg" width="180">
</figure>

-   Modèle : $u(t)=Ri(t)$
-   Impedance généralisée : $Z_R=R$

### Condensateur

<figure>
    <img src="./img/capacitor.svg" width="180">
</figure>

-   Modèle : $i(t)=C\frac{du(t)}{dt}$
-   Impedance généralisée : $Z_C=\frac{1}{Cs}$

### Bobine


<figure>
    <img src="./img/inductor.svg" width="180">
</figure>

-   Modèle : $u(t)=L\frac{di(t)}{dt}$
-   Impedance généralisée: $Z_L=Ls$

## Associations de dipôles

### Mise en série

<figure>
    <img src="./img/serie.svg" width="200">
</figure>

-   Impedance généralisée équivalente :

$$Z_{eq}=Z_1+Z_2$$

### Mise en parallèle

<figure>
    <img src="./img/parallel.svg" width="200">
</figure>

-   Impedance généralisée équivalente :

$$\frac{1}{Z_{eq}}=\frac{1}{Z_1}+\frac{1}{Z_2}$$

### Pont diviseur

<figure>
    <img src="./img/voltage_divider.svg" width="200">
</figure>

-   Mise en équation :

$$\frac{V_2(s)}{V_1(s)}=\frac{Z_2}{Z_1+Z_2}$$

### Potentiel des noeuds

<figure>
    <img src="./img/node.svg" width="300">
</figure>

-   Mise en équation :

$$\frac{V_1(s)-V_A(s)}{Z_1}+\frac{V_2(s)-V_A(s)}{Z_2}+\frac{V_3(s)-V_A(s)}{Z_3}=0$$

## Exemples

### Circuit 1

On considère le circuit suivant :

<figure>
    <img src="./img/RLC_BP2.svg" width="400">
</figure>

#### Mise en équation

Pour ce type de circuit, il est recommandé de déterminer l'impédance équivalente à la mise en parallèle des composants $C$, $L$ et $R_2$, puis d'utiliser la loi du pont diviseur de tension. 

- Calcul de l'impédance équivalente :

$$
\begin{align}
\frac{1}{Z_{eq}} &= \frac{1}{Z_C} + \frac{1}{Z_L} + \frac{1}{R_2}\\
&=Cs + \frac{1}{Ls} + \frac{1}{R_2} = \frac{R_2 CL s^2 + R_2 + L s}{R_2 L s}
\end{align}
$$

- Application du pont diviseur : 

$$
\frac{V_{out}(s)}{V_{in}(s)}=\frac{Z_{eq}}{Z_{eq}+Z_{R_1}}=\frac{Z_{eq}}{Z_{eq}+R_1}
$$

#### Fonction de transfert

En manipulant la dernière équation, la fonction de transfert s'exprime sous la forme : 

$$
\begin{align}
H(s) &= \frac{1}{1 + \frac{R_1}{Z_{eq}}} \\
&=\frac{R_2 L s}{R_2 L s + R_1 R_2 CL s^2 + R_1 R_2 + R_1 L s}\\
&=\frac{\frac{L}{R_1} s}{\frac{L}{R_1}s + CL s^2 + 1 + \frac{L}{R_2} s}\\
&=\frac{\frac{L}{R_1} s}{CL s^2+ \left(\frac{1}{R_1}+\frac{1}{R_2}\right)Ls  + 1}\\
&=\frac{\frac{L}{R_1} s}{CL s^2+ \left(\frac{R_1+R_2}{R_1R_2}\right)Ls  + 1}\\
\end{align}
$$

Ce circuit correspond à un second ordre.






### Circuit 2

On considère le circuit suivant :

<figure>
    <img src="./img/MFB_BP2.svg" width="400">
</figure>


#### Mise en équation

Notons $V$ la tension aux bornes de $R_2$.

-   Equation 1 (loi des noeuds)

$$\frac{V_e(s) - V(s)}{R_1} + \frac{0-V(s)}{R_2}+\frac{V_s(s) - V(s)}{Z_{C2}}+\frac{V_-(s) - V(s)}{Z_{C1 }} =0$$

-   Equation 2 (loi des noeuds)

$$\frac{V(s) - V_-(s)}{Z_{C1}} + \frac{V_s(s)-V_-(s)}{R_3} =0$$

-   Equation 3 (AOP régime linéaire)

$$V_+(s) = V_-(s)$$

-   Equation 4 (entrée +):

$$V_+(s) = 0$$

#### Fonction de transfert

Pour obtenir la fonction de transfert, nous allons déterminer une
équation avec que des termes en $V_e(s)$ d\'un côté et que des termes en
$V_s(s)$ de l\'autre côté.

En manipulant les 4 équations, nous obtenons :

$$\frac{V_e(s)}{R_1}  = -\frac{V_s(s)}{Z_{C2}} +\frac{V(s)}{Z_{C2}}+ \frac{V(s)}{R_2}+ \frac{V(s)}{Z_{C1 }} + \frac{V(s)}{R_1}$$

$$V(s)  = -\frac{Z_{C1}}{R_3}V_s(s)$$

Il en vient que

$$\frac{V_e(s)}{R_1}  = -V_s(s)\left(\frac{1}{Z_{C2}} -\frac{Z_{C1}}{Z_{C2}R_3} -\frac{Z_{C1}}{R_2R_3}-\frac{1}{R_3} -\frac{Z_{C1}}{R_1R_3}\right)$$

En remplaçant les impédances par leur expressions et en mettant tout
sous le même dénominateur pour le terme de droite, nous obtenons

$$\frac{V_e(s)}{R_1}  = -\frac{V_s(s)}{R_1R_2R_3C_1s} \left( R_1R_2R_3C_1C_2s^2  + R_1R_2C_2s + R_1 + R_1R_2C_1s + R_2\right)$$

Finalement,

$$H(s) = \frac{V_s(s)}{V_e(s)} = -\frac{\frac{R_2R_3}{R_1 + R_2}C_1s}{ \frac{R_1R_2R_3}{R_1 + R_2}C_1C_2s^2  + \frac{R_1R_2}{R_1 + R_2}(C_1+C_2)s + 1}$$

Ce circuit correspond donc à un circuit de second ordre.

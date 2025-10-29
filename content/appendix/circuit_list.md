---
title: Liste des Circuits
outline: [2, 3]
---

# Liste des Circuits

## Premier Ordre

### Circuits Passifs

#### Passe-bas RC

<figure>
    <img src="./img/RC_LP.svg" width="300">
    <figcaption>RC LP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{LP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{1 + sRC}
$$

#### Passe-haut RC

<figure>
    <img src="./img/RC_HP.svg" width="300">
    <figcaption>RC HP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{HP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{sRC}{1 + sRC}
$$

### Circuits Actifs


#### Passe-bas SP

<figure>
    <img src="./img/SP_LP.svg" width="300">
    <figcaption>SP LP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{LP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{-\frac{R_2}{R_1}}{1 + R_2C s}
$$


#### Passe-haut SP

<figure>
    <img src="./img/SP_HP.svg" width="300">
    <figcaption>SP HP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{HP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{-R_2Cs }{1 + R_1 C s}
$$

## Second Ordre

### Passe-bas RC/RC

<figure>
    <img src="./img/RC_RC_LP.svg" width="300">
    <figcaption>RC/RC LP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{LP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{1 + (C_2R_2+C_2R_1+C_1R_1)s+ R_1R_2C_1C_2s^2}
$$

### Passe-bande RC/RC

<figure>
    <img src="./img/RC_RC_BP.svg" width="300">
    <figcaption>RC/RC BP Filter</figcaption>
</figure>


La fonction de transfert pour ce filtre est donnée par :
$$
H_{LP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{R_2C_1s}{1 + (C_2R_2+C_1R_2+C_1R_1)s+ R_1R_2C_1C_2s^2}
$$

### Passe-haut RC/RC

<figure>
    <img src="./img/RC_RC_HP.svg" width="300">
    <figcaption>RC/RC HP Filter</figcaption>
</figure>


La fonction de transfert pour ce filtre est donnée par :
$$
H_{HP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{R_1R_2C_1C_2s^2}{1 + (C_2R_2+C_2R_1+C_1R_1)s+ R_1R_2C_1C_2s^2}
$$


### Passe-bas RLC

<figure>
    <img src="./img/RLC_LP.svg" width="300">
    <figcaption>RLC LP Filter</figcaption>
</figure>


La fonction de transfert pour ce filtre est donnée par :
$$
H_{LP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{1 + RCs+ LC s^2}
$$

### Passe-bande RLC (forme 1)

<figure>
    <img src="./img/RLC_BP1.svg" width="300">
    <figcaption>RLC BP1 Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{BP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{RCs}{1 + RCs+ LC s^2}
$$


### Passe-bande RLC (forme 2)

<figure>
    <img src="./img/RLC_BP2.svg" width="300">
    <figcaption>RLC BP2 Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{BP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{\frac{L}{R_1}s}{1 + L\left( \frac{R_1+R_2}{R_1R_2}\right)s+ LC s^2}
$$


### Passe-haut RLC

<figure>
    <img src="./img/RLC_HP.svg" width="300">
    <figcaption>RLC HP Filter</figcaption>
</figure>

La fonction de transfert pour ce filtre est donnée par :
$$
H_{HP}(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{LCs^2}{1 + RCs+ LC s^2}
$$
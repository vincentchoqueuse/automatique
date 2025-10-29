---
outline: [2,3]
---

# Table des transformées de Laplace

| Fonction temporelle $f(t)$  | Transformée de Laplace $F(s)$       | Conditions |
| ----------------------------| ------------------------------------| ---------- |
| $\delta(t)$                 | $1$                                 |            |
| $u(t)$                      | $\frac{1}{s}$                       | $s > 0$|
| $e^{at}u(t)$                | $\frac{1}{s-a}$                     | $s > a$|
| $t^nu(t)$                   | $\frac{n!}{s^{n+1}}$                | $s > 0$, $n$ entier |
| $\sin(\omega t)u(t)$        | $\frac{\omega}{s^2 + \omega^2}$     | $s > 0$|
| $\cos(\omega t)u(t)$        | $\frac{s}{s^2 + \omega^2}$          | $s > 0$|
| $e^{-at}\sin(\omega t)u(t)$ | $\frac{\omega}{(s+a)^2 + \omega^2}$ | $s > 0$|
| $e^{-at}\cos(\omega t)u(t)$ | $\frac{s+a}{(s+a)^2 + \omega^2}$    | $s > 0$|
| $\cos(\omega t)u(t)$        | $\frac{s}{s^2 + \omega^2}$          | $s > 0$|
| $t e^{at}u(t)$              | $\frac{1}{(s-a)^2}$                 | $s > a$|
| $e^{-at}u(t)$               | $\frac{1}{s+a}$                     | $s > -a$|
| $\sinh(\omega t)u(t)$       | $\frac{\omega}{s^2 - \omega^2}$     | $s > \omega$|
| $\cosh(\omega t)u(t)$       | $\frac{s}{s^2 - \omega^2}$          | $s > \omega$|

# Installation des outils

## Installation de Miniconda

### Présentation de Miniconda

Miniconda est une distribution légère de Conda, un gestionnaire de paquets et d'environnements pour les langages de programmation, notamment Python. Miniconda comprend Conda, Python et ses dépendances essentielles, permettant ainsi aux utilisateurs de créer des environnements isolés pour différents projets. Cela garantit que les bibliothèques et les dépendances d'un projet n'interfèrent pas avec celles d'un autre.

**Avantages de Miniconda :**
- Installation rapide et légère.
- Permet de gérer facilement les dépendances des projets.
- Crée des environnements isolés.
- Compatible avec de nombreuses plateformes (Windows, macOS, Linux).

### Installation

::: details Windows

1. **Télécharger l'installateur :**
   - Rendez-vous sur la page de [téléchargement de Miniconda](https://docs.conda.io/en/latest/miniconda.html).
   - Choisissez l'installateur pour Windows (64-bit ou 32-bit selon votre système).

2. **Lancer l'installateur :**
   - Double-cliquez sur le fichier téléchargé pour lancer l'installation.
   - Suivez les instructions à l'écran. Il est recommandé de choisir l'option "Add Miniconda to my PATH environment variable".

3. **Vérifier l'installation :**
   - Ouvrez le programme Anaconda Prompt.
   - Tapez `conda --version` pour vérifier que Conda est bien installé.

:::


::: details macOS

1. **Télécharger l'installateur :**
   - Rendez-vous sur la page de [téléchargement de Miniconda](https://docs.conda.io/en/latest/miniconda.html).
   - Choisissez l'installateur pour macOS (64-bit).

2. **Lancer l'installateur :**
   - Ouvrez un terminal.
   - Naviguez jusqu'au répertoire où l'installateur a été téléchargé.
   - Tapez `bash Miniconda3-latest-MacOSX-x86_64.sh` et suivez les instructions à l'écran.

3. **Vérifier l'installation :**
   - Ouvrez un nouveau terminal.
   - Tapez `conda --version` pour vérifier que Conda est bien installé.

:::

::: details Linux

1. **Télécharger l'installateur :**
   - Rendez-vous sur la page de [téléchargement de Miniconda](https://docs.conda.io/en/latest/miniconda.html).
   - Choisissez l'installateur pour Linux (64-bit ou 32-bit selon votre système).

2. **Lancer l'installateur :**
   - Ouvrez un terminal.
   - Naviguez jusqu'au répertoire où l'installateur a été téléchargé.
   - Tapez `bash Miniconda3-latest-Linux-x86_64.sh` (ou la version 32-bit si applicable) et suivez les instructions à l'écran.

3. **Vérifier l'installation :**
   - Ouvrez un nouveau terminal.
   - Tapez `conda --version` pour vérifier que Conda est bien installé.

:::

## Création d'un environnement dédié

Pour illustrer le contenu de ce cours, nous allons utiliser un environnement python 3.11 et des librairies Python spécifiques. 

1. **Créer un nouvel environnement :**
   ```bash
   conda create --name enib_asa python=3.11
   ```

2. **Activer l'environnement :**
   ```bash
   conda activate enib_asa
   ```

3. **Installer des paquets avec conda :**
   ```bash
   conda install -c conda-forge plotly control jupyterlab
   ```

4. **Installer control-plotly avec pip :**
   ```bash
   pip install control-plotly
   ```

## Utilisation de Jupyter Lab

Dans votre terminal, lancez la commande 
    
```bash
jupyter lab 
```
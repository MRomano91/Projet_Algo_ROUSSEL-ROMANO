# Projet Algo - MOTUS
Projet bonus d'Algo APP3 : Implémentation du jeu MOTUS

## Description

Ce projet implémente un jeu de type **MOTUS** (similaire à Wordle) en Python. Le joueur dispose d'un nombre limité d'essais pour deviner un mot secret choisi aléatoirement par le jeu. Pour chaque proposition, le programme indique si les lettres sont bien placées, mal placées ou absentes du mot secret.

## Architecture du Projet

```
Projet_Algo_ROSSEL-ROMANO/
├── README.md                     # Documentation du projet
├── datas/
│   └── scrabble.txt              # Dictionnaire des mots valides
├── Gaphic/
│   └── Output.py                 # Utilitaires d'affichage avec couleurs
├── Modus/                        # Code du jeu MOTUS
│   ├── main.py                   # Point d'entrée principal
│   ├── GameLuncher/
│   │   └── FileName.py           # Fonction principale (partie) du jeu
│   ├── Tools/
│   │   ├── GameTools.py          # Outils de jeu (validation, comparaison)
│   │   ├── RandomWord.py         # Sélection aléatoire de mots
│   │   ├── Rechercher.py         # Recherche dichotomique
│   │   └── Trier.py              # Tri fusion pour les mots
│   └── TxtLoader/                
│       └── DataLoader.py         # Chargement des fichiers texte
└── IA/                           # Intelligence Artificielle pour MOTUS
    ├── Exercice2/
    │   └── Fonctions.py          # Implémentation IA naïve
    └── Exercice3/
        ├── Fonctions.py          # Implémentation IA avancée avec heuristiques
        └── Tests.py              # Tests de performance (naïve vs IA)
```

## Modules et Fonctions

### 1. **src/Tools/GameTools.py**
Contient les fonctions principales de la logique du jeu:

- **`isValid(w: str, x: str, dico: dict[int, list[str]]) -> bool`**
  - Vérifie si une proposition est valide
  - Critères: bonne longueur, première lettre correcte, mot dans le dictionnaire
  - Complexité: O(log n_l)

- **`compare(w: str, x: str) -> list[int]`**
  - Compare deux mots et retourne un tableau de codes:
    - `2`: lettre bien placée
    - `1`: lettre mal placée
    - `0`: lettre absente
  - Gère correctement les doublons
  - Complexité: O(len(w))

### 2. **src/Tools/RandomWord.py**
Sélection aléatoire de mots:

- **`randomWord(dico: list[str]) -> str`** (Surcharge 1)
  - Retourne un mot aléatoire d'une liste
  - Complexité: O(1) temps et espace

- **`randomWord(dico: dict[int, list[str]], l: int) -> str`** (Surcharge 2)
  - Retourne un mot aléatoire d'une longueur spécifique
  - Utilise le dictionnaire organisé par longueur
  - Complexité: O(1) temps et espace

### 3. **src/Tools/Rechercher.py**
Algorithme de recherche:

- **`inside(w: str, l: list[str]) -> bool`**
  - Recherche dichotomique d'un mot dans une liste triée
  - Vérifie si un mot existe dans le dictionnaire
  - Complexité: O(log(|n_l|))

### 4. **src/Tools/Trier.py**
Algorithme de tri:

- **`TrieFusionListeString(l: list[str]) -> list[str]`**
  - Trie une liste de chaînes de caractères par ordre alphabétique
  - Utilise l'algorithme du tri fusion
  - Complexité: O(n log n)

### 5. **src/GameLuncher/FileName.py**
Lance et gère une partie complète:

- **`partie(n: int) -> None`**
  - Lance une partie avec n essais maximum
  - Le programme:
    1. Choisit un mot aléatoire et en affiche la longueur et la première lettre
    2. Récupère les propositions du joueur
    3. Valide chaque proposition
    4. Affiche les lettres bien et mal placées
    5. S'arrête quand le mot est trouvé ou les essais épuisés
  - Affiche le résultat final

### 6. **Gaphic/Output.py**
Utilitaires d'affichage:

- **`printRed(a: str) -> None`**
  - Affiche du texte en fond rouge

- **`printGreen(a: str) -> None`**
  - Affiche du texte en fond vert

- Utilise la bibliothèque `colorama` pour les couleurs

## Exercices IA - MOTUS Automatisé

Le projet inclut deux exercices avancés permettant à une IA de jouer automatiquement à MOTUS et de comparer différentes stratégies.

### **IA/Exercice2/ - Approche Naïve**

Implémentation d'une intelligence artificielle basique pour jouer à MOTUS.

Fonctions principales (`Exercice2/Fonctions.py`):

- **`GetPossibleWords(w: str, dico: dict[int, list[str]]) -> list[str]`**
  - Retourne tous les mots du dictionnaire qui peuvent être obtenus à partir de w
  - Filtre les mots possibles basé sur les contraintes de longueur

- **`update(words: list[str], w: str, comp: list[int]) -> list[str]`**
  - Filtre les mots possibles en fonction du résultat de comparaison
  - Paramètres:
    - `words`: liste des mots possibles
    - `w`: proposition faite
    - `comp`: résultat de la comparaison (2=bien placé, 1=mal placé, 0=absent)
  - Retourne uniquement les mots cohérents avec la réponse

- **`partieNaive(x: str) -> int`**
  - Lance une partie automatique où l'IA joue naïvement pour deviner le mot `x`
  - Stratégie: essaie aléatoirement parmi les mots possibles
  - Retourne le nombre d'essais effectués

### **IA/Exercice3/ - Approche Intelligente avec Heuristiques**

Implémentation d'une IA optimisée utilisant des heuristiques pour minimiser le nombre d'essais.

Fonctions principales (`Exercice3/Fonctions.py`):

- **`choice(dico: list[str], heuristique: int = 0) -> str`**
  - Choisit la meilleure proposition parmi les mots possibles
  - Utilise l'heuristique spécifiée pour évaluer chaque mot
  - Paramètres:
    - `dico`: liste des mots possibles
    - `heuristique`: indice de l'heuristique à utiliser (0, 1, 2, ...)
  - Retourne le mot sélectionné par l'IA

- **`partieIA(x: str, heuristique: int = 0) -> int`**
  - Lance une partie automatique avec l'IA intelligente
  - Utilise l'heuristique choisie pour prendre les décisions
  - Paramètres:
    - `x`: mot à deviner
    - `heuristique`: heuristique à utiliser
  - Retourne le nombre d'essais effectués

Tests et Comparaison (`Exercice3/Tests.py`):

- Compare les performances entre:
  - L'approche naïve (Exercice2)
  - L'approche intelligente (Exercice3) avec différentes heuristiques
- Mesure le nombre moyen d'essais pour chaque stratégie
- Permet d'évaluer l'efficacité des heuristiques utilisées

## Données

### Dictionnaire (`datas/scrabble.txt`)
Fichier contenant tous les mots valides du jeu. Le programme doit:
1. Charger ce dictionnaire
2. Organiser les mots par longueur dans une structure `dict[int, list[str]]`
3. Trier chaque liste pour permettre la recherche dichotomique

## Dépendances

- **Python 3.7+**
- **colorama**: Pour les affichages en couleur
  ```bash
  pip install colorama
  ```

## Utilisation

### Installation
```bash
# Cloner le repository
git clone https://github.com/MRomano91/Projet_Algo_ROUSSEL-ROMANO.git
cd Projet_Algo_ROUSSEL-ROMANO

# Installer les dépendances
pip install colorama
```

### Lancer une partie
```bash
python src/main.py
```

Le jeu demandera le nombre d'essais souhaités et affichera les indices en temps réel.

## Exemple de Déroulement

```
=== MOTUS ===
Mot à deviner: 6 lettres commençant par M
Nombre d'essais: 6

Essai 1/6 - Proposition: MOTEUR
M [2] bien placé
O [1] mal placé
T [1] mal placé
E [1] mal placé
U [1] mal placé
R [0] absent

Essai 2/6 - Proposition: MAUDIT
M [2] bien placé
A [0] absent
U [1] mal placé
D [0] absent
I [0] absent
T [1] mal placé

Essai 3/6 - Proposition: MOULIN
M [2] bien placé
O [1] mal placé
U [1] mal placé
L [0] absent
I [0] absent
N [0] absent

Essai 4/6 - Proposition: MUTTON
Mot invalide! Réessayez.

Essai 4/6 - Proposition: MUTISM
M [2] bien placé
U [1] mal placé
T [1] mal placé
I [0] absent
S [0] absent
M [1] mal placé

Essai 5/6 - Proposition: MURMUR
M [2] bien placé
U [1] mal placé
R [1] mal placé
M [1] mal placé
U [1] mal placé
R [1] mal placé

Essai 6/6 - Proposition: MUSCAT
M [2] bien placé
U [1] mal placé
S [0] absent
C [0] absent
A [0] absent
T [1] mal placé

=== PARTIE TERMINÉE ===
Le mot était: MUTTON
Vous avez trouvé en 6 essais!
```

## Complexité Globale

| Opération | Complexité | Notes |
|-----------|-----------|-------|
| Charger dictionnaire | O(n log n) | Tri de tous les mots |
| Recherche dichotomique | O(log n) | Pour valider une proposition |
| Comparaison de mots | O(m) | m = longueur du mot |
| Sélection aléatoire | O(1) | Accès direct à un élément |

## Notes de Développement

### V1.0.0
- Les fonctions principales sont déclarées mais non implémentées (squelette du projet)
- Le dossier `TxtLoader/` est destiné aux utilitaires de chargement de fichiers
- Le GameLauncher doit être renommé (voir commentaire dans FileName.py)
- Le fichier `main.py` doit servir de point d'entrée pour lancer le jeu

## � Informations Supplémentaires

### Flux du Jeu
1. **Initialisation** - Le programme charge le dictionnaire depuis `scrabble.txt`
2. **Sélection du mot** - Un mot aléatoire est choisi
3. **Affichage des indices** - Longueur et première lettre sont révélées
4. **Boucle de jeu**:
   - Récupération de la proposition du joueur
   - Validation (longueur, première lettre, existence dans dictionnaire)
   - Si invalide: nouvelle tentative sans incrémenter le compteur
   - Si valide: comparaison et affichage du résultat
5. **Fin** - Affichage du résultat (gagné/perdu et nombre d'essais)

### Structure des Données
- **Dictionnaire principal** : `dict[int, list[str]]`
  - Clés: longueur des mots (5, 6, 7, ...)
  - Valeurs: listes de mots triés alphabétiquement
- **Codes de comparaison** :
  - `2`: Vert (bien placé)
  - `1`: Orange (mal placé)
  - `0`: Gris (absent)

### Optimisations Algorithmiques
- Dictionnaire organisé par longueur pour accès O(1)
- Listes triées pour recherche dichotomique O(log n)
- Pas de re-tri à chaque partie

## Auteurs

- ROUSSEL Marque
- ROMANO Matheo

## Historique des Versions

### V1.0.0 (Squelette)
- Structure du projet définie
- Signatures des fonctions avec documentations complètes
- Dictionnaire Scrabble intégré
- Dépendance colorama ajoutée

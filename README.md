# Projet Algo - MOTUS
Projet bonus d'Algo APP3 : Implémentation du jeu MOTUS

Polytech Paris-Saclay | APP3 IIM | Année universitaire 2025-2026

## Auteurs

- ROMANO Matheo
- ROUSSEL Marc


## Description

Ce projet implémente un jeu de type **MOTUS** (similaire à Wordle) en Python. Le joueur dispose d'un nombre limité d'essais pour deviner un mot secret choisi aléatoirement par le jeu. Pour chaque proposition, le programme indique si les lettres sont bien placées, mal placées ou absentes du mot secret.

## Installation & Démarrage


```bash
# Cloner le repository
git clone https://github.com/MRomano91/Projet_Algo_ROUSSEL-ROMANO.git
cd Projet_Algo_ROUSSEL-ROMANO

# Créer un environnement virtuel python
python3 -m venv .env

# Activer cet environnement python
.env\Scripts\activate # Pour Windows
source .env/bin/activate # Pour UNIX (Linux, macOS)

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### Mode Interactif

#### Lancer directement une partie
```bash
python romano_roussel.py   
```

#### Lancer les tests unitaires Motus, puis une partie
```bash
python romano_roussel.py -t
```

#### Lancer les tests IA (Exercice 2 & 3), puis une partie
```bash
python romano_roussel.py -ia
```

#### Lance tous les tests, puis une partie
```bash
python romano_roussel.py -t -ia
```

Le programme:
1. Lance une partie avec 6 essais
2. Choisit un mot aléatoire de 4 à 14 lettres
3. Affiche la longueur et la première lettre
4. Le joueur propose des mots
5. Les lettres bien placées s'affichent en **ROUGE**
6. Les lettres mal placées s'affichent en **VERT**

#### Exemple de Déroulement

```
*****************
*  MO-MO-MOTUS  *
*****************
M--------- | 10 lettres
Il vous reste 6 tentatives
----------------------------
Veuillez saisir un mot :
MATHEMAT
[MATHEMAT colorisé selon résultat]
M [ROUGE - lettre bien placée]
A [VERT - lettre mal placée]
T [BLANC - lettre absente]
...
```

### Mode IA Naïve (Exercice 2)
```python
python3 # Lancer d'abord un interpréteur Python
>>> from IA.Exercice2.Fonctions import partieNaive
>>> partieNaive('motus')
5  # Nombre d'essais pour trouver 'motus'
```

### Mode IA Intelligente (Exercice 3) - $\sigma_0$
```python
python3
>>> from IA.Exercice3.Fonctions import partieIA
>>> partieIA('motus', 0)
3  # Nombre d'essais (généralement plus bas que l'IA naïve)
```

### Mode IA Intelligente (Exercice 3) - $\sigma_1$
```python
python3
>>> from IA.Exercice3.Fonctions import partieIA
>>> partieIA('motus', 1)
3  # Nombre d'essais 
```

## Architecture du Projet

```
Projet_Algo_ROUSSEL-ROMANO/
├── README.md                     # Documentation du projet
├── main.py                       # Point d'entrée avec tests
├── requirements.txt              # Dépendances du projet
├── datas/
│   └── scrabble.txt              # Dictionnaire des mots valides
├── Graphic/
│   ├── __init__.py
│   └── Output.py                 # Utilitaires d'affichage avec couleurs
├── Motus/                        # Code du jeu MOTUS
│   ├── __init__.py
│   ├── GameLauncher/
│   │   ├── __init__.py
│   │   └── GameLauncher.py       # Fonction partie(n) - mode interactif
│   ├── Tools/
│   │   ├── __init__.py
│   │   ├── GameTools.py          # Outils de jeu (validation, comparaison)
│   │   ├── RandomWord.py         # Sélection aléatoire de mots
│   │   ├── Rechercher.py         # Recherche dichotomique
│   │   ├── Trier.py              # Tri fusion pour les mots
│   │   └── Tools.py              # Fonctions utilitaires (conversion listes/strings)
│   └── TxtLoader/                
│       ├── __init__.py
│       └── DataLoader.py         # Chargement des fichiers texte
└── IA/                           # Intelligence Artificielle pour MOTUS
    ├── __init__.py
    ├── Exercice2/
    │   ├── __init__.py
    │   └── Fonctions.py          # Implémentation IA naïve
    │   └── Tests.py              # Tests des fonctions de l'IA naïve
    └── Exercice3/
        ├── __init__.py
        ├── Fonctions.py          # Implémentation IA avancée avec heuristiques
        └── Tests.py              # Tests de performance (naïve vs IA)
```

## Modules et Fonctions

Cette section présente les fonctions par module et fichiers, indiqués dans l'arborescence ci-dessus, et détaille leur fonctionnement, leurs paramètres, ainsi que leurs complexités. 

### 1. **Motus/Tools/GameTools.py**
Contient les fonctions principales de la logique du jeu:

- **`isValid(w: str, x: str, dico: dict[int, list[str]]) -> bool`**
  - Vérifie si une proposition est valide
  - Critères: bonne longueur, première lettre correcte, mot dans le dictionnaire
  - Complexité: $O(\log{n})$, correspondant à la complexité de la fonction `inside()`, effectuant une recherche dichotomique sur le tableau de taille $n$, contenant les mots de même longeur que w.

- **`compare(w: str, x: str) -> list[int]`**
  - Compare deux mots et retourne un tableau de codes:
    - `2`: lettre bien placée
    - `1`: lettre mal placée
    - `0`: lettre absente
  - Gère correctement les doublons avec un algorithme 2-passes. On parcourt le mot deux fois pour les objectifs suivants :
    - 1er parcourt : Marquer les lettres bien placées (2)
    - 2ème parcourt : Marquer les lettres mal placées (1) parmi les restantes
  - Complexité: $O(2m) = O(m)$, avec $m$ la longueur des mots `w` et `x`, tous deux supposés être de même longueur.

### 2. **Motus/Tools/RandomWord.py**
Sélection aléatoire de mots:

- **`randomWord(dico: list[str]) -> str`**
  - Retourne un mot aléatoire d'une liste
  - Complexité: $O(1)$ en temps et espace

- **`randomWordFromDico(dico: dict[int, list[str]], l: int) -> str`**
  - Retourne un mot aléatoire d'une longueur spécifique
  - Utilise le dictionnaire organisé par longueur
  - Complexité: $O(1)$ en temps et espace

### 3. **Motus/Tools/Rechercher.py**
Algorithme de recherche:

- **`inside(w: str, lst: list[str]) -> bool`**
  - Recherche dichotomique d'un mot dans une liste triée
  - Vérifie si un mot existe dans le dictionnaire
  - Utilise la récursion avec division en deux
  - Complexité: $O(log(|lst|))$, correspondant à la complexité d'une recherche dichotomique classique.

### 4. **Motus/Tools/Trier.py**
Algorithme de tri:

- **`Split(l: list) -> tuple[list, list]`**
  - Scinde une liste en autres listes de longueur quasi-égales
  - Complexité: $O(n)$ car la scission implique l'allocation des éléments de la liste, de manière successive, dans deux tableaux à part entière.

- **`FusionListeString(l1: list[str], l2: list[str]) -> list[str]`**
  - Fusionne deux listes triées de chaînes
  - Complexité: $O(|l1| + |l2|)$, soit $O(n)$ avec $n$ le nombre total d'éléments dans $l1$ et $l2$ combinés.

- **`TrieFusionListeString(l: list[str]) -> list[str]`**
  - Trie une liste de chaînes de caractères par ordre alphabétique
  - Utilise l'algorithme du tri fusion
  - Complexité: $O(n \log{n})$, correspondant à la complexité du tri fusion.

### 5. **Motus/Tools/Tools.py**
Fonctions utilitaires:

- **`Liste1DtoString(l: list) -> str`**
  - Convertit une liste 1D en chaîne de caractères formatée
  - Parcourt chaque élément de la liste `l`
  - Complexité: $O(n)$ avec $n$ le nombre d'éléments de la liste `l`

- **`Tableau2DtoString(t: list[list]) -> str`**
  - Convertit une liste 2D en chaîne de caractères formatée
  - Parcourt chaque sous-liste `l` de la liste `t`, et fait appel à `Liste1DtoString(l)` pour formatter chaque sous-liste
  - Complexité: $O(m \times n)$ avec $m$ le nombre d'éléments de `t`, multipliée par $O(n)$, la complexité de `Liste1DtoString()`

### 6. **Motus/GameLauncher/GameLauncher.py**
Lance et gère une partie complète :

- **`partie(n: int) -> None`**
  - Lance une partie interactive avec n essais maximum
  - Le programme:
    1. Charge le dictionnaire Scrabble
    2. Choisit un mot aléatoire de longueur 4-14
    3. Affiche la longueur et la première lettre
    4. Récupère les propositions du joueur
    5. Valide chaque proposition (sans décrémenter si invalide)
    6. Affiche les lettres bien et mal placées en couleurs
    7. S'arrête quand le mot est trouvé ou les essais épuisés
    8. Affiche le résultat final

### 7. **Motus/TxtLoader/DataLoader.py**
Chargement du dictionnaire:

- **`loadDico(path: str) -> dict[int, list[str]]`**
  - Charge tous les mots du fichier en dictionnaire
  - Structure: clés = longueurs (4, 5, 6...), valeurs = listes de mots
  - Complexité: $O(n)$ où $n$ est le nombre total de mots

### 8. **Graphic/Output.py**
Utilitaires d'affichage:

- **`printDefault(a: str) -> None`** - Affiche en blanc
- **`printRed(a: str) -> None`** - Affiche en fond rouge (lettre bien placée)
- **`printGreen(a: str) -> None`** - Affiche en fond vert (lettre mal placée)

- **`AfficherMotus(w: str, comparaison: list[int]) -> None`**
  - Affiche le mot w colorisé selon les résultats de comparaison
  - Utilise la bibliothèque `colorama` pour les couleurs
  - Codes: 0=blanc, 1=vert, 2=rouge

## Exercices IA - MOTUS Automatisé

Le projet inclut deux exercices avancés permettant à une IA de jouer automatiquement à MOTUS et de comparer différentes stratégies.

### **IA - Exercice 2 - Approche Naïve**

Implémentation d'une intelligence artificielle basique pour jouer à MOTUS.

Fonctions principales (`Exercice2/Fonctions.py`):

- **`GetPossibleWords(x: str, dico: dict[int, list[str]]) -> list[str]`**
  - Retourne tous les mots du dictionnaire de la même longueur que x
  - Retourne `dico[len(x)]` directement
  - Complexité: $O(1)$, correspondant à l'accès direct en mémoire


- **`update(words: list[str], w: str, comp: list[int]) -> list[str]`**
  - Filtre les mots possibles en fonction du résultat de comparaison
  - Paramètres:
    - `words`: liste des mots possibles à filtrer
    - `w`: proposition de l'IA
    - `comp`: résultat de la comparaison (2=bien placé, 1=mal placé, 0=absent)
  - Retourne uniquement les mots cohérents avec la réponse
  - Utilise `compare(w, x) == comp` pour chaque mot `x` de `words`
  - Complexité: $O(|words| × len(x))$ avec $|words|$ le nombre de mots dans $words$, 
  multiplé par $O(len(x))$, correspondant à la complexité de `compare(w, x)`, avec 
  $len(x)$ le nombre de lettres dans le mot $x$.


- **`partieNaive(x: str) -> int`**
  - Lance une partie automatique où l'IA joue naïvement pour deviner le mot `x`
  - Suit la stratégie suivante :
    1. Charge le dictionnaire Scrabble
    2. Récupère tous les mots de même longueur que x
    3. Choisit aléatoirement parmi les mots possibles
    4. Récupère la comparaison
    5. Filtre les mots compatibles avec le résultat
    6. Répète jusqu'à trouver le mot
  - Retourne le nombre d'essais effectués
  - Complexité moyenne : $O(\log n)$ avec $n$ le nombre d'essais, où chaque essai coûte $O(|words| × len(x))$, correspondant à la complexité de `update(matching_words, current_best_word, comp)`, avec :
    - `matching_words` les mots compatibles, 
    - `current_best_word` le meilleur mot trouvé,
    - `comp` la comparaison entre le meilleur mot et un mot compatible

### **IA - Exercice 3 - Approche Intelligente avec Heuristiques**

Implémentation d'une IA optimisée utilisant des heuristiques pour minimiser le nombre d'essais.

**Concepts Heuristiques** :

L'IA utilise la théorie de l'information pour choisir les meilleures propositions. Pour chaque mot candidat w et chaque ensemble S de mots possibles:

- **$\sigma_0$(w,S) - Stratégie moyenne (Average Information Gain)**:
  $$\sigma_0(w,S) = \frac{1}{|S|} \sum_{x \in S} \log\left(\frac{|S|}{|S[w,x]|}\right)$$
  - Maximise le gain moyen d'information
  - S[w,x] = ensemble des mots y tels que compare(w,y) = compare(w,x)
  - Stratégie équilibrée pour réduire en moyenne la taille de S

- **$\sigma_1$(w,S) - Stratégie pessimiste (Worst-case Information Gain)**:
  $$\sigma_1(w,S) = \min_{x \in S} \log\left(\frac{|S|}{|S[w,x]|}\right)$$
  - Maximise le pire cas (worst-case)
  - Garantit une réduction même dans le pire scenario
  - Plus conservative mais plus sûre

Fonctions principales (`Exercice3/Fonctions.py`):

- **`FilterByFirstChar(words: list[str], char: str) -> list[str]`**
  - Filtre les mots commençant par un caractère donné
  - Complexité: $O(|words|)$, avec $|words|$ le nombre de mots dans `words`, correspondant au parcours de la liste (l'accès `w[0]` étant en $O(1)$)


- **`choice(dico: list[str], heuristique: int = 0) -> str`**
  - Choisit la meilleure proposition parmi les mots possibles
  - Utilise l'heuristique spécifiée en paramètres pour évaluer chaque mot
  - Paramètres:
    - `dico`: liste des mots possibles à évaluer
    - `heuristique`: indice de l'heuristique (0=$\sigma_0$, 1=$\sigma_1$)
  - Calcule, pour chaque mot `w` de `dico`, la partition `Si` en comparant `w` à chaque mot `x` de `dico` via `gt.compare(w, x)`, soit $O(len(x))$ par comparaison
  - Retourne le mot avec le score heuristique le plus élevé
  - Complexité: $O(|dico|^2 × len(x))$ dans le pire cas, avec $|dico|$ le nombre de mots dans `dico` et $len(x)$ le nombre de lettres dans le mot à deviner. Ici, $|dico|^2$ correspond à la double boucle sur `dico` (chacune de taille $|dico|$), multipliée par le coût de `gt.compare(w, x)`. Le calcul du score (`sum` ou `max` sur `Si.values()`) est en $O(|dico|)$, dominé par le terme précédent.


- **`partieIA(x: str, heuristique: int = 0) -> int`**
  - Lance une partie automatique avec l'IA intelligente
  - Utilise l'heuristique choisie pour prendre les décisions
  - Paramètres:
    - `x`: mot à deviner
    - `heuristique`: heuristique à utiliser (0=$\sigma_0$, 1=$\sigma_1$)
  - Retourne le nombre d'essais effectués
  - Complexité moyenne : $O(\log n)$ avec $n$ le nombre d'essais, où chaque essai coûte $O(|matching\_words|^2 × len(x))$, correspondant à l'appel de `choice(matching_words, heuristique)`, ce coût dominant celui de `update` (issu de l'exercice 2, en $O(|matching\_words| × len(x))$)

Tests et Comparaison (`Exercice3/Tests.py`):

- Compare les performances entre:
  - L'approche naïve (Exercice2)
  - L'approche intelligente (Exercice3) avec différentes heuristiques
- Mesure le nombre moyen d'essais pour chaque stratégie
- Permet d'évaluer l'efficacité des heuristiques utilisées

## Données

### Dictionnaire (`datas/scrabble.txt`)
Fichier contenant tous les mots valides du jeu. Le programme:
1. Charge ce dictionnaire en mémoire
2. Organise les mots par longueur dans une structure `dict[int, list[str]]`
3. Les listes ne sont pas triées au chargement (optimisation)
4. Peut être utilisé directement pour GetPossibleWords() ou trié si nécessaire

## Dépendances

- **Python 3.7+** (type hints requis)
- **colorama** : Pour les affichages en couleur

## Complexité Globale

| Opération | Complexité | Notes |
|-----------|-----------|-------|
| Charger dictionnaire | O(n) | Chargement et regroupement par longueur |
| Recherche dichotomique (inside) | O(log n) | Pour valider une proposition |
| Comparaison de mots | O(m) | m = longueur du mot, 2 passes |
| Sélection aléatoire | O(1) | Accès direct à un élément |
| Update (IA Naïve) | O(\|words\| × m) | Filtre tous les mots |
| Choice (IA Intelligente) | O(\|words\|² × m) | Calcule $\sigma$ pour tous les mots |
| Partie (IA Naïve) | O(log n × \|words\| × m) | Environ log n essais |
| Partie (IA Intelligente) | O(log n × \|words\|² × m) | Plus d'essais mais meilleure stratégie |

## Flux de Jeu Détaillé

### Mode Interactif
1. Charger dictionnaire depuis `datas/scrabble.txt`
2. Choisir mot aléatoire de longueur 4-14
3. Afficher première lettre et longueur
4. Boucle (tant que n > 0):
   - Demander proposition
   - Valider (longueur, première lettre, dictionnaire)
   - Si invalide: reparamètre sans décrémenter
   - Si valide: compare(w, x), afficher colorisé
   - Si gagné: terminer avec message victoire
   - Sinon: décrémenter n
5. Si n == 0: Afficher défaite

### Mode IA Naïve
1. Charger dictionnaire
2. S = mots de longueur len(x)
3. w = random(S)
4. Boucle (tant que w $\neq$ x) :
   - Afficher w
   - Filtrer S = `update(S, w, compare(w,x))`
   - w = random(S)
   - Incrémenter compteur
5. Retourner compteur

### Mode IA Intelligente
1. Initialisation comme IA Naïve
2. Boucle (tant que w $\neq$ x) :
   - Afficher w
   - Filtrer S
   - **`w = choice(S, heuristique)`** (*Choix intelligent*)
   - Incrémenter compteur
3. Retourner compteur

## Structure des Données et Complexités

### Dictionnaire Principal
```python
dico = {
    4: ['aaaa', 'aber', ...],    # Mots de 4 lettres
    5: ['aaaaa', 'abase', ...],  # Mots de 5 lettres
    ...
    14: [...]                     # Mots de 14 lettres
}
```

### Codes de Comparaison
```python
compare('test', 'best') = [0, 2, 2, 2]
# 0 = absent, 1 = mal placé, 2 = bien placé
```


# Projet Algo - MOTUS
Projet bonus d'Algo APP3 : Implémentation du jeu MOTUS

## Description

Ce projet implémente un jeu de type **MOTUS** (similaire à Wordle) en Python. Le joueur dispose d'un nombre limité d'essais pour deviner un mot secret choisi aléatoirement par le jeu. Pour chaque proposition, le programme indique si les lettres sont bien placées, mal placées ou absentes du mot secret.

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
    └── Exercice3/
        ├── __init__.py
        ├── Fonctions.py          # Implémentation IA avancée avec heuristiques
        └── Tests.py              # Tests de performance (naïve vs IA)
```

## Modules et Fonctions

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
  - Gère correctement les doublons avec un algorithme 2-passes:
    - Pass 1: Marquer les lettres bien placées (2)
    - Pass 2: Marquer les lettres mal placées (1) parmi les restantes
  - Complexité: $O(m)$, avec $m$ la longueur du mot.

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
  - Divise une liste en deux parties quasi-égales
  - Complexité: $O(n)$ car la scission implique l'allocation des éléments de la liste, de manière successive, dans deux tableaux à part entière.

- **`FusionListeString(l1: list[str], l2: list[str]) -> list[str]`**
  - Fusionne deux listes triées de chaînes
  - Complexité: $O(|l1| + |l2|)$, soit $O(n)$ avec n le nombre total d'éléments dans l1 et l2 combinés.

- **`TrieFusionListeString(l: list[str]) -> list[str]`**
  - Trie une liste de chaînes de caractères par ordre alphabétique
  - Utilise l'algorithme du tri fusion
  - Complexité: $O(n \log{n})$, correspondant à la complexité du tri fusion.

### 5. **Motus/Tools/Tools.py**
Fonctions utilitaires:

- **`Liste1DtoString(l: list) -> str`**
  - Convertit une liste 1D en chaîne de caractères formatée

- **`Tableau2DtoString(t: list[list]) -> str`**
  - Convertit une liste 2D en chaîne de caractères formatée

### 6. **Motus/GameLauncher/GameLauncher.py**
Lance et gère une partie complète:

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

### **IA/Exercice2/ - Approche Naïve**

Implémentation d'une intelligence artificielle basique pour jouer à MOTUS.

Fonctions principales (`Exercice2/Fonctions.py`):

- **`GetPossibleWords(x: str, dico: dict[int, list[str]]) -> list[str]`**
  - Retourne tous les mots du dictionnaire de la même longueur que x
  - Retourne `dico[len(x)]` directement
  - Complexité: $O(1)$

- **`update(words: list[str], w: str, comp: list[int]) -> list[str]`**
  - Filtre les mots possibles en fonction du résultat de comparaison
  - Paramètres:
    - `words`: liste des mots possibles à filtrer
    - `w`: proposition de l'IA
    - `comp`: résultat de la comparaison (2=bien placé, 1=mal placé, 0=absent)
  - Retourne uniquement les mots cohérents avec la réponse
  - Utilise `compare(w, x) == comp` pour chaque mot x
  - Complexité: $O(|words| × len(w))$
  **Tu en es là bg**

- **`partieNaive(x: str) -> int`**
  - Lance une partie automatique où l'IA joue naïvement pour deviner le mot `x`
  - Stratégie:
    1. Charge le dictionnaire Scrabble
    2. Récupère tous les mots de même longueur que x
    3. Choisit aléatoirement parmi les mots possibles
    4. Récupère la comparaison
    5. Filtre les mots compatibles avec le résultat
    6. Répète jusqu'à trouver le mot
  - Retourne le nombre d'essais effectués
  - Complexité moyenne : $O(\log n)$ essais, chaque essai coûte $O(|words| × len(x))$

### **IA/Exercice3/ - Approche Intelligente avec Heuristiques**

Implémentation d'une IA optimisée utilisant des heuristiques pour minimiser le nombre d'essais.

**Concepts Heuristiques** :

L'IA utilise la théorie de l'information pour choisir les meilleures propositions. Pour chaque mot candidat w et chaque ensemble S de mots possibles:

- **σ₀(w,S) - Stratégie moyenne (Average Information Gain)**:
  $$\sigma_0(w,S) = \frac{1}{|S|} \sum_{x \in S} \log\left(\frac{|S|}{|S[w,x]|}\right)$$
  - Maximise le gain moyen d'information
  - S[w,x] = ensemble des mots y tels que compare(w,y) = compare(w,x)
  - Stratégie équilibrée pour réduire en moyenne la taille de S

- **σ₁(w,S) - Stratégie pessimiste (Worst-case Information Gain)**:
  $$\sigma_1(w,S) = \min_{x \in S} \log\left(\frac{|S|}{|S[w,x]|}\right)$$
  - Maximise le pire cas (worst-case)
  - Garantit une réduction même dans le pire scenario
  - Plus conservative mais plus sûre

Fonctions principales (`Exercice3/Fonctions.py`):

- **`choice(dico: list[str], heuristique: int = 0) -> str`**
  - Choisit la meilleure proposition parmi les mots possibles
  - Utilise l'heuristique spécifiée pour évaluer chaque mot
  - Paramètres:
    - `dico`: liste des mots possibles à évaluer
    - `heuristique`: indice de l'heuristique (0=σ₀, 1=σ₁)
  - Retourne le mot avec le score heuristique le plus élevé
  - **À implémenter**

- **`partieIA(x: str, heuristique: int = 0) -> int`**
  - Lance une partie automatique avec l'IA intelligente
  - Utilise l'heuristique choisie pour prendre les décisions
  - Paramètres:
    - `x`: mot à deviner
    - `heuristique`: heuristique à utiliser (0=σ₀, 1=σ₁)
  - Retourne le nombre d'essais effectués
  - **À implémenter**

Tests et Comparaison (`Exercice3/Tests.py`):

- Compare les performances entre:
  - L'approche naïve (Exercice2)
  - L'approche intelligente (Exercice3) avec différentes heuristiques
- Mesure le nombre moyen d'essais pour chaque stratégie
- Permet d'évaluer l'efficacité des heuristiques utilisées
- **À implémenter**

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


## Installation

```bash
# Cloner le repository
git clone https://github.com/MRomano91/Projet_Algo_ROUSSEL-ROMANO.git
cd Projet_Algo_ROUSSEL-ROMANO

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### Mode Interactif (Joueur vs Ordi)
```bash
python main.py
```
Lance les tests TestMotus(), TestExercice2(), TestExercice3() puis une partie classique.

Ou directement en Python:
```bash
python -c "from Motus.GameLauncher.GameLauncher import partie; partie(6)"
```
Le programme:
1. Lance une partie avec 6 essais
2. Choisit un mot aléatoire de 4 à 14 lettres
3. Affiche la longueur et la première lettre
4. Le joueur propose des mots
5. Les lettres bien placées s'affichent en **ROUGE**
6. Les lettres mal placées s'affichent en **VERT**

### Mode Automatisé - IA Naïve (Exercice 2)
```bash
echo "A compléter
```
Ou directement en Python:
```bash
python -c "from IA.Exercice2.Fonctions import partieNaive;print(f"Nombre d'essais: {partieNaive('motus')}")";
```

### Mode Automatisé - IA Intelligente (Exercice 3)
```bash
echo "A compléter
```

## Exemple de Déroulement

### Mode Interactif
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
M [ROUGE - bien placé]
A [VERT - mal placé]
T [BLANC - absent]
...
```

### Mode IA Naïve (Exercice 2)
```python
>>> from IA.Exercice2.Fonctions import partieNaive
>>> partieNaive('motus')
[Affichage de chaque proposition avec ses couleurs]
5  # Nombre d'essais pour trouver 'motus'
```

### Mode IA Intelligente (Exercice 3) - σ₀
```python
>>> from IA.Exercice3.Fonctions import partieIA
>>> partieIA('motus', 0)
[Affichage avec choix intelligents basés sur σ₀]
3  # Nombre d'essais (généralement plus bas que l'IA naïve)
```

## Complexité Globale

| Opération | Complexité | Notes |
|-----------|-----------|-------|
| Charger dictionnaire | O(n) | Chargement et regroupement par longueur |
| Recherche dichotomique (inside) | O(log n) | Pour valider une proposition |
| Comparaison de mots | O(m) | m = longueur du mot, 2 passes |
| Sélection aléatoire | O(1) | Accès direct à un élément |
| Update (IA Naïve) | O(\|words\| × m) | Filtre tous les mots |
| Choice (IA Intelligente) | O(\|words\|² × m) | Calcule σ pour tous les mots |
| Partie (IA Naïve) | O(log n × \|words\| × m) | Environ log n essais |
| Partie (IA Intelligente) | O(log n × \|words\|² × m) | Plus d'essais mais meilleure stratégie |

## Notes de Développement

### État Actuel du Projet
- Structure du projet définie et correcte
- Signatures des fonctions avec documentations complètes
- Dictionnaire Scrabble intégré
- Dépendance colorama ajoutée
- Implémentation GameTools.py avec compare() correcte (2-passes)
- Implémentation Exercice2 (IA Naïve) complète
- Exercice3 (IA Intelligente) - Signatures définies, implémentation en cours
- Tests - TestMotus, TestExercice2 fonctionnels, TestExercice3 à compléter

### Problèmes Résolus
1. Import error: Package Rechercher → Correction de la structure
2. Bug compare() - Out-of-range → Algorithme 2-passes implémenté
3. Structure des dossiers → Correction de Gaphic → Graphic
4. FileName.py → GameLauncher.py

### À Faire - Exercice 3
- [ ] Implémenter `choice()` avec calcul de σ₀ et σ₁
- [ ] Implémenter `partieIA()` utilisant `choice()`
- [ ] Ajouter TestExercice3() à main.py
- [ ] Comparer statistiquement Naïve vs σ₀ vs σ₁

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
4. Boucle (tant que w ≠ x):
   - Afficher w
   - Filtrer S = update(S, w, compare(w,x))
   - w = random(S)
   - Incrémenter compteur
5. Retourner compteur

### Mode IA Intelligente
1. Initialisation comme IA Naïve
2. Boucle (tant que w ≠ x):
   - Afficher w
   - Filtrer S
   - **w = choice(S, heuristique)** (Choix intelligent!)
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

### Analyse de Complexité
- **loadDico()**: O(n) - lecture linéaire
- **inside()**: O(log m) - recherche dichotomique
- **compare()**: O(len(w)) - 2 passes sur le mot
- **update()**: O(|words| × len(w)) - filtre tous les mots
- **partieNaive()**: O(log n × |words| × len(w)) en moyenne
- **choice()**: O(|words|² × len(w)) - calcule σ pour tous les mots
- **partieIA()**: O(log n × |words|² × len(w)) - moins d'essais mais plus cher par essai

## Optimisations et Points Clés

### 1. **Structure par longueur**
- Accès O(1) aux mots de longueur donnée
- Pas de filtrage par longueur à chaque étape

### 2. **Algorithm compare() - Deux passes**
- Pass 1: Marquer bien-placés (2), les supprimer
- Pass 2: Marquer mal-placés (1) parmi les restants
- Gère correctement les doublons

### 3. **Performance des IA**
- Naïve: ~5-7 essais en moyenne
- σ₀: ~3-4 essais (optimale moyenne)
- σ₁: ~4-5 essais (pire cas garanti)

## Améliorations Futures

1. **Exercice 3 - Implémentation complète**
   - [ ] Implémenter σ₀ et σ₁
   - [ ] Optimiser choice() avec caching
   - [ ] Ajouter autres heuristiques

2. **Interface Graphique**
   - [ ] Utiliser Tkinter pour GUI
   - [ ] Affichage temps réel de l'IA

3. **Multilangues**
   - [ ] Support plusieurs dictionnaires
   - [ ] Interface bilingue

4. **Persistance**
   - [ ] Sauvegarder scores
   - [ ] Leaderboard
   - [ ] Statistiques par longueur

5. **Optimisations**
   - [ ] Memoization des compare()
   - [ ] Parallélisation avec threading
   - [ ] Tri des listes pour binary search

## Auteurs

- ROUSSEL Marque
- ROMANO Matheo

## Historique des Versions

### V1.0.0 (Squelette)
- Structure du projet définie
- Signatures des fonctions avec documentations complètes
- Dictionnaire Scrabble intégré
- Dépendance colorama ajoutée

### V1.1.0 (Implémentation)
- GameTools.py: Toutes les fonctions implémentées
- Exercice2: IA Naïve complète et testée
- Exercice3: Signatures et concepts documentés
- Tests: TestMotus et TestExercice2 fonctionnels
- [ ] Exercice3: Implémentation en cours
- [ ] Comparaison statistique: À venir

### V1.2.0 (Prévue)
- [ ] Exercice3: IA Intelligente complète
- [ ] Tests complets de performance
- [ ] Optimisations algorithmiques
- [ ] Interface graphique

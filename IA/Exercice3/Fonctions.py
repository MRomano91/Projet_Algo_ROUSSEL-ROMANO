"""
Fichier à renommer + refaire l'arboraissance
"""

from math import log
from sys import float_info as fi
import IA.Exercice2.Fonctions as e2
import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rd
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out

def FilterByFirstChar(words : list[str], char : str) -> list[str]:
    """
    Filtre les mots pour ne garder que ceux qui commencent par un caractère précis.
    param :
        words : une liste de mots
        char : le caractère à chercher au début
    return :
        la liste des mots commençant par char
    """
    return [w for w in words if w[0] == char]


def choice(dico: list[str], heuristique: int = 0) -> str:
    """
    Choisit la meilleure proposition de l'IA en fonction de l'heuristique choisie
    Optimisé avec arret si partition parfaite trouvée

    param :
        - dico : liste de mots possibles
        - heuristique : heuristique à utiliser
    return :
        - mot choisi par l'IA
    """
    if not dico or len(dico) == 0:
        raise ValueError("Le dictionnaire est vide, impossible de choisir un mot.")

    meilleur_mot : str = None
    meilleur_score : float = fi.max
    perfect_score = 0 if heuristique == 0 else 1
    
    for w in dico:
        Si : dict[tuple[int], int] = {}

        for x in dico:
            tcomp = tuple(gt.compare(w, x))
            if tcomp in Si:
                Si[tcomp] += 1
            else:
                Si[tcomp] = 1
        
        tailles = Si.values()
        if heuristique == 0:
            score = sum(t * log(t) for t in tailles)
        else:
            score = max(tailles)
        
        # Early stopping : si partition parfaite
        if score <= perfect_score:
            return w
        
        # Update meilleur
        if score < meilleur_score:
            meilleur_score = score
            meilleur_mot = w
    
    return meilleur_mot

def partieIA(x: str, heuristique: int = 0) -> int:
    """
    IA  joue à MOTUS avec une des heuristiques proposées lorsque le mot à deviner est x,
    et renvoie le nombre de tentatives effectuées
    
    param :
        - x : mot à deviner
        - heuristique : heuristique à utiliser
    return :
        - nombre de tentatives effectuées
    """
    robert : dict[int, list[str]] = datas.loadDico("datas/scrabble.txt")
    matching_words : list[str] = FilterByFirstChar(e2.GetPossibleWords(x, robert),x[0])
    current_best_word : str = choice(matching_words, heuristique)
    comp = gt.compare(current_best_word, x) 
    tours_de_jeu : int = 1
    
    while current_best_word != x:
        out.AfficherMotus(current_best_word, comp)
        matching_words = e2.update(matching_words, current_best_word, comp)
        
        if not matching_words:
            print("word not found. Current best word :")
            break
            
        current_best_word = choice(matching_words, heuristique)
        comp = gt.compare(current_best_word, x)
        tours_de_jeu += 1
    
    comp = gt.compare(current_best_word, x)
    out.AfficherMotus(current_best_word, comp)
    return tours_de_jeu


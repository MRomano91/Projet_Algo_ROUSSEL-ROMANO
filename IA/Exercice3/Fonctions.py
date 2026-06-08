"""
Fichier à renommer + refaire l'arboraissance
"""

from math import log
from sys import _float_info as fi
import IA.Exercice2.Fonctions as e2
import Motus.Tools.GameTools as gt

def choice(dico: list[str], heuristique: int = 0) -> str:
    """
    Choisit la meilleure proposition de l'IA en fonction de l'heuristique choisie

    param :
        - dico : liste de mots possibles
        - heuristique : heuristique à utiliser
    return :
        - mot choisi par l'IA
    """
    meilleur_mot : str = None
    meilleur_score : float = fi.max  

    for w in dico :
        Si : dict[tuple[int], int]= {}
        
        for x in e2.update(dico,w,comp):
            comp = gt.compare(w,x)
            tcomp = tuple(comp)
            if Si[tcomp]:
                Si[tcomp] += 1
            else :
                Si[tcomp] = 1
        
        tailles = Si.values()
        if heuristique == 0:
            score = sum(t * log(t) for t in tailles)
        else:
            score = max(tailles)
            
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
    return


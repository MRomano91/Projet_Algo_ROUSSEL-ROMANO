"""
Devrait - on  le mettre dans Tools ? main ?
Fonction d'affichage pour le projet
"""

import colorama

colorama.init()
RED = colorama.Back.RED
GREEN = colorama.Back.GREEN
END = colorama.Back.RESET

def printRed(a):
    print(RED+a+END,end='')

def printGreen(a):
    print(GREEN+a+END,end='')

def AfficherMotus(mot: str, comparaison: list[int]):
    """
    Affiche le résultat d'une proposition de mot pour le jeu MOTUS

    param :
        - mot : mot à deviner
        - comparaison : liste des résultats de la comparaison (0 = incorrect, 1 = présent, 2 = correct)
    """
    pass
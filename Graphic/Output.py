"""
Devrait - on  le mettre dans Tools ? main ?
Fonction d'affichage pour le projet
"""

import colorama

colorama.init()
RED = colorama.Back.RED
GREEN = colorama.Back.GREEN
END = colorama.Back.RESET

# ----- Fonctions d'affichage coloré ----- #
def printDefault(a):
    print(a, end='')

def printRed(a):
    print(RED+a+END,end='')

def printGreen(a):
    print(GREEN+a+END,end='')
# ---------------------------------------- #

def AfficherMotus(w: str, comparaison: list[int]):
    """
    Affiche le résultat d'une proposition de mot pour le jeu MOTUS

    param :
        - w : mot du joueur
        - comparaison : liste des résultats de la comparaison (0 = incorrect, 1 = présent, 2 = correct)
    """
    if len(comparaison) != len(w) : raise ValueError("AfficherMotus(w, comparaison) :\n Error : w has not same length as comparaison")

    for i in range(len(w)):

        # Pour les lettres incorrectes
        if comparaison[i] == 0:
            printDefault(w[i])

        # Pour les lettres présentes
        if comparaison[i] == 1:
            printGreen(w[i])

        # Pour les lettres correctes
        if comparaison[i] == 2:
            printRed(w[i])
    print()
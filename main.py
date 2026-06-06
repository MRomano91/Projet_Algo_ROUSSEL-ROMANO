"""

"""

import Motus.Tools.RandomWord as rw
import Motus.TxtLoader.DataLoader as datas

def __main__():
    """
    Point d'entrée du programme
    """

    # Test de chargement du dictionnaire 
    
    print("Chargement du dico")
    dico = datas.loadDico('datas/scrabble.txt')

    print("Le nouveau mot de longueur 5 est : " + rw.randomWordFromDico(dico=dico, l=5))
    print("Le nouveau mot de longueur 7 est : " + rw.randomWordFromDico(dico=dico, l=7))

    # return

if __name__ == "__main__":
    __main__()
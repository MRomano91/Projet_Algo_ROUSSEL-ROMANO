"""

"""

import Motus.Tools.RandomWord as rw
import Motus.Tools.Rechercher as rech
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out

def __main__():
    """
    Point d'entrée du programme
    """

    # Test de chargement du dictionnaire 
    print("Chargement du dico")
    dico = datas.loadDico('datas/scrabble.txt')

    print("Le nouveau mot de longueur 5 est : " + rw.randomWordFromDico(dico=dico, l=5))
    print("Le nouveau mot de longueur 7 est : " + rw.randomWordFromDico(dico=dico, l=7))


    # Test de inside
    print("Test de inside: ", + rech.inside("aaaa", dico[4])) # Doit renvoyer 0
    print("Test de inside: ", + rech.inside("amer", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("mise", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("pris", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("gkmx", dico[4])) # Doit renvoyer 0


    # Test de AfficherMotus
    mot = "abcdef"
    comparaison_test = [2, 1, 1, 0, 2, 0] 
    out.AfficherMotus(mot, comparaison_test)

if __name__ == "__main__":
    __main__()
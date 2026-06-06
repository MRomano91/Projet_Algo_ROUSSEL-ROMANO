"""
Ecrire une fonction partie(n) qui lance une partie en n essais.
— Le programme choisit un mot x a faire deviner, et affiche sa longueur et sa
premiere lettre.
— Pour chaque proposition du joueur, le programme verifie que le mot est valide
(autrement il demande une nouvelle proposition sans incrementer le nombre
d'essais effectues), puis affiche les lettres bien et mal placees.
— Le programme s'arrete quand le joueur a trouve le mot, ou bien s'il a epuise ses
essais. Il termine en affichant le resultat de la partie.

"""
import random

import Graphic.Output as gout
import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rw
import Motus.TxtLoader.DataLoader as datas

def partie(n : int) -> None:
    """
    Lance une partie en n essais.
    param :
        n: le nombre d'essais
    return: 
        None
    """

    print("*****************")
    print("*  MO-MO-MOTUS  *")
    print("*****************")

    dico = datas.loadDico('datas/scrabble.txt')
    word = rw.randomWordFromDico(dico=dico, l=random.randint(4, 14))
    partie_gagne = False


    # ---------- Boucle de jeu ---------- #

    # Premier affichage du mot
    print(word[0] + "-"*(len(word)-1) + " | " + str(len(word)) + " lettres", end='\n')

    while n > 0 and not partie_gagne:

        # Affichage des tentatives 
        print("Il vous reste " + str(n) + " tentatives")
        print("----------------------------")

        # Saisie utilisateur
        print("Veuillez saisir un mot :")
        user_input = input()
        print()

        # Vérification de la validité du mot 
        while not gt.isValid(user_input, word, dico):
            print("Votre mot est invalide, veuillez resaisir un mot :")
            user_input = input()
            print()
        
        # Affichage de la comparaison
        tab_comparaison = gt.compare(user_input, word)
        gout.AfficherMotus(user_input, tab_comparaison)

        # Vérification du gain
        if (tab_comparaison == [2 for i in range(len(word))]):
            partie_gagne = True
        else:
            n -= 1
    # ----------------------------------- #

    # Affichage de fin de partie
    if partie_gagne:
        print("Félicitations ! Vous avez trouvé le mot " + word)
    else:
        print("Dommage... Le mot à deviner était " + word)
"""

"""

import argparse
import Motus.GameLauncher.GameLauncher as gl
import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rw
import Motus.Tools.Rechercher as rech
import Motus.Tools.Tools as ts
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out
import IA.Exercice2.Tests as tex2
import IA.Exercice3.Tests as tex3

def TestMotus():
    """
    
    """
    # Test de chargement du dictionnaire 
    print("----------------------------------")
    print("Test de chargement du dictionnaire")
    print("----------------------------------")
    print("Chargement du dico")
    dico = datas.loadDico('datas/scrabble.txt')

    print("Le nouveau mot de longueur 5 est : " + rw.randomWordFromDico(dico=dico, l=5))
    print("Le nouveau mot de longueur 7 est : " + rw.randomWordFromDico(dico=dico, l=7))
    print()

    # Test de inside
    print("----------------------------------")
    print("Test de inside")
    print("----------------------------------")
    print("Test de inside: ", + rech.inside("aaaa", dico[4])) # Doit renvoyer 0
    print("Test de inside: ", + rech.inside("amer", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("mise", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("pris", dico[4])) # Doit renvoyer 1
    print("Test de inside: ", + rech.inside("gkmx", dico[4])) # Doit renvoyer 0
    print()

    # Test de isValid
    print("----------------------------------")
    print("Test de isValid")
    print("----------------------------------")
    print("Test de isValid pour w = bas et x = les : ", + gt.isValid("bas","les",dico) ) # Doit renvoyer 0
    print("Test de isValid pour w = bas et x = b : ", + gt.isValid("bas","b",dico) ) # Doit renvoyer 0
    print("Test de isValid pour w = bbb et x = bas : ", + gt.isValid("bbb","bas",dico) ) # Doit renvoyer 0
    print("Test de isValid pour w = bas et x = bas : ", + gt.isValid("bas","bas",dico) ) # Doit renvoyer 1
    print()
    
    # Test de compare
    print("----------------------------------")
    print("Test de compare")
    print("----------------------------------")
    try : 
        print("Test de inside pour w = aaa  et x = aaaa:")
        gt.compare("aaa","aaaa")
    except Exception as e :
        print(e) # Doit afficher une ValueError
    
    print("Test de inside pour w = aaa et x = aaa : " + ts.Liste1DtoString(gt.compare("aaa","aaa")) ) # Doit renvoyer [2,2,2]
    print("Test de inside pour w = bbb et x = aaa : " + ts.Liste1DtoString(gt.compare("bbb","aaa")) ) # Doit renvoyer [0,0,0]
    print("Test de inside pour w = baa et x = abc : " + ts.Liste1DtoString(gt.compare("baa","abc")) ) # Doit renvoyer [1,1,0]
    print("Test de inside pour w = baa et x = abc : " + ts.Liste1DtoString(gt.compare("nitrataient","normativite")) ) # Doit renvoyer [2,1,1,1,2,2,0,1,1,0,0]
    print()
    
    # Test de AfficherMotus
    print("----------------------------------")
    print("Test de AfficherMotus")
    print("----------------------------------")
    mot = "abcdef"
    comparaison_test = [2, 1, 1, 0, 2, 0] 
    out.AfficherMotus(mot, comparaison_test)
    print()

def __main__():
    """
    Point d'entrée du programme
    """

    # Prise en compte des arguments
    parser = argparse.ArgumentParser(description="MOTUS - Jeu de devinettes")
    parser.add_argument("-t", action="store_true", help="Lancer les tests unitaires Motus avant de jouer")
    parser.add_argument("-ia", action="store_true", help="Lancer les tests IA (Exercice 2 & 3) avant de jouer")
    args = parser.parse_args()

    # Si les tests unitaires sont lancés
    if args.t:
        print ("=================================")
        print ("||                             ||")
        print ("||    TESTS UNITAIRES MOTUS    ||")
        print ("||                             ||")
        print ("=================================")
        TestMotus()
        print("\n\n\n\n")

    # Si les tests d'IA sont lancés
    if args.ia:
        print ("=================================")
        print ("||                             ||")
        print ("||        TEST IA NAIVE        ||")
        print ("||                             ||")
        print ("=================================")
        tex2.test_naive()
        print("\n\n\n\n")

        print ("=================================")
        print ("||                             ||")
        print ("||           TEST IA           ||")
        print ("||              +              ||")
        print ("||    COMPARAISON NAIVE & IA   ||")
        print ("||                             ||")
        print ("=================================")
        tex3.test_performance_comparison(num_tests=10)
        print("\n\n\n\n")

    # Lancement d'un jeu avec
    gl.partie(6)


if __name__ == "__main__":
    __main__()
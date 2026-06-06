"""

"""

import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rw
import Motus.Tools.Rechercher as rech
import Motus.Tools.Tools as ts
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out

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
    print("Test de inside pour w = bas et x = les : ", + gt.isValid("bas","les",dico) ) # Doit renvoyer 0
    print("Test de inside pour w = bas et x = b : ", + gt.isValid("bas","b",dico) ) # Doit renvoyer 0
    print("Test de inside pour w = bbb et x = bas : ", + gt.isValid("bbb","bas",dico) ) # Doit renvoyer 0
    print("Test de inside pour w = bas et x = bas : ", + gt.isValid("bas","bas",dico) ) # Doit renvoyer 1
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
    print()
    
    # Test de AfficherMotus
    print("----------------------------------")
    print("Test de AfficherMotus")
    print("----------------------------------")
    mot = "abcdef"
    comparaison_test = [2, 1, 1, 0, 2, 0] 
    out.AfficherMotus(mot, comparaison_test)
    print()


def TestExercice2():
    pass


def TestExercice3():
    pass



def __main__():
    """
    Point d'entrée du programme
    """

    print ("=================================")
    print ("||                             ||")
    print ("||      TEST DU JEU MODUS      ||")
    print ("||                             ||")
    print ("=================================")
    TestMotus()
    print("\n\n\n\n")
    print ("=================================")
    print ("||                             ||")
    print ("||        TEST IA NAIVE        ||")
    print ("||                             ||")
    print ("=================================")
    TestExercice2()
    print("\n\n\n\n")
    print ("=================================")
    print ("||                             ||")
    print ("||           TEST IA           ||")
    print ("||                             ||")
    print ("=================================")
    TestExercice3()
    print("\n\n\n\n")


if __name__ == "__main__":
    __main__()
"""

"""

import Motus.GameLauncher.GameLauncher as gl
import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rw
import Motus.Tools.Rechercher as rech
import Motus.Tools.Tools as ts
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out
import IA.Exercice2.Fonctions as ex2
import IA.Exercice3.Fonctions as ex3
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


def TestExercice2():
    """
    Tests pour les fonctions de l'IA naïve (Exercice 2)
    """
    dico = datas.loadDico('datas/scrabble.txt')
    
    # Test de GetPossibleWords
    print("----------------------------------")
    print("Test de GetPossibleWords")
    print("----------------------------------")
    words_4 = ex2.GetPossibleWords("test", dico)
    print(f"Nombre de mots de longueur 4 : {len(words_4)}")
    print(f"Premiers mots : {words_4[:5]}")
    
    words_7 = ex2.GetPossibleWords("example", dico)
    print(f"Nombre de mots de longueur 7 : {len(words_7)}")
    print()
    
    # Test de update
    print("----------------------------------")
    print("Test de update")
    print("----------------------------------")
    
    # Test 1: Liste simple avec résultat vide
    test_words_1 = ["chat", "char", "chap", "chas"]
    word_1 = "test"
    comp_1 = [2, 2, 2, 2]
    result_1 = ex2.update(test_words_1, word_1, comp_1)
    print(f"Test 1 - Aucune correspondance attendue:")
    print(f"  Mots : {test_words_1}")
    print(f"  Mot testé : {word_1}, Comparaison : {comp_1}")
    print(f"  Résultat : {result_1}")
    print(f"  Status : {'PASS' if result_1 == [] else 'FAIL'}")
    print()
    
    # Test 2: Liste simple avec une correspondance
    test_words_2 = ["amer", "ames", "amor"]
    word_2 = "amer"
    comp_2 = gt.compare(word_2, "amer")  # [2, 2, 2, 2]
    result_2 = ex2.update(test_words_2, word_2, comp_2)
    print(f"Test 2 - Une correspondance attendue:")
    print(f"  Mots : {test_words_2}")
    print(f"  Mot testé : {word_2}, Comparaison : {comp_2}")
    print(f"  Résultat : {result_2}")
    print(f"  Status : {'PASS' if 'amer' in result_2 and len(result_2) == 1 else 'FAIL'}")
    print()
    
    # Test 3: Plusieurs correspondances
    test_words_3 = ["amer", "amor", "amis"]
    word_3 = "amer"
    comp_3 = [2, 2, 0, 0]  # Positions 0 et 1 bien placées
    result_3 = ex2.update(test_words_3, word_3, comp_3)
    print(f"Test 3 - Plusieurs correspondances:")
    print(f"  Mots : {test_words_3}")
    print(f"  Mot testé : {word_3}, Comparaison : {comp_3}")
    for word in test_words_3:
        comp_calc = gt.compare(word_3, word)
        print(f"    compare('{word_3}', '{word}') = {comp_calc}")
    print(f"  Résultat : {result_3}")
    print()
    
    # Test 4: Avec mots du dictionnaire
    test_words_4 = dico[4][:50]  # Premiers 50 mots de 4 lettres
    word_4 = dico[4][10]
    word_4_bis = dico[4][18]

    comp_4 = gt.compare(word_4, word_4_bis)  # [2, 2, 2, 2]
    result_4 = ex2.update(test_words_4, word_4, comp_4)
    print(f"Test 4 - Mots du dictionnaire:")
    print(f"  Nombre de mots testés : {len(test_words_4)}")
    print(f"  Mot testé : {word_4}, Comparaison : {comp_4}")
    print(f"  Nombre de correspondances trouvées : {len(result_4)}")
    print(f"  Mots trouvés : {result_4}")
    print()
    
    
    # Test de partieNaive
    print("----------------------------------")
    print("Test de partieNaive")
    print("----------------------------------")
    test_mots = ["chat", "rose", "film", "naissances", "frequemment", "freon"]
    for mot in test_mots:
        try:
            tours = ex2.partieNaive(mot)
            print(f"Mot : {mot} -> Nombre de tentatives : {tours}")
        except Exception as e:
            print(f"Erreur pour le mot {mot} : {e}")
    print()

def TestExercice3():
    tex3.test_performance_comparison(num_tests=10)
    print()



def __main__():
    """
    Point d'entrée du programme
    """

    print ("=================================")
    print ("||                             ||")
    print ("||      TEST DU JEU MOTUS      ||")
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

    gl.partie(6)


if __name__ == "__main__":
    __main__()
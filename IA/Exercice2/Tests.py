"""
Procédure de tests de l'approche naïve pour l'exercice 2
"""

import IA.Exercice2.Fonctions as ex2
import Motus.TxtLoader.DataLoader as datas
import Motus.Tools.GameTools as gt

def test_naive():
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
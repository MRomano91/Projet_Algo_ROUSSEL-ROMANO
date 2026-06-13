"""
Test de l'IA + Comparaison des performances entre l'implémentation naïve et l'IA
"""
import IA.Exercice2.Fonctions as e2
import IA.Exercice3.Fonctions as e3
import Motus.Tools.RandomWord as rd
import Motus.TxtLoader.DataLoader as datas
import Motus.Tools.GameTools as gt
import time
import random
from statistics import mean

def print_stats_results(name: str, results: list, times: list):
        avg_result = mean(results) if results else 0
        avg_time = mean(times) if times else 0
        min_result = min(results) if results else 0
        max_result = max(results) if results else 0
        total_result = sum(results) if results else 0
        
        print(f"{name:20}")
        print(f"  Tentatives  : {avg_result:.2f} moyenne (min: {min_result}, max: {max_result}, total: {total_result})")
        print(f"  Temps       : {avg_time:.3f}s moyenne par test")
        print()
    


def test_performance_comparison(num_tests: int = 3):
    """
    Compare les performances entre :
    - Stratégie naïve (random)
    - Heuristique 0 (IA)
    - Heuristique 1 (IA)
    
    param :
        - num_tests : nombre de mots à tester
    """
    print("CHARGEMENT DU DICTIONNAIRE...")
    print("----------------------------------------------")
    
    dico = datas.loadDico("datas/scrabble.txt")
    
    total_words = sum(len(words) for words in dico.values())
    print(f"Dictionnaire chargé : {total_words} mots")
    print()
    
    # Sélectionner les mots à tester
    print(f"SÉLECTION DE {num_tests} MOTS ALÉATOIRES À TESTER...")
    print("----------------------------------------------")
    
    test_words = []
    available_lengths = list(dico.keys())
    
    for _ in range(num_tests):
        length = random.choice(available_lengths)
        word = rd.randomWordFromDico(dico, length)
        test_words.append(word)
    
    print(f"Mots sélectionnés : {test_words}")
    print()
    
    print("EXÉCUTION DES TESTS")
    print("----------------------------------------------")
    print()
    
    results_naive = []
    results_h0 = []
    results_h1 = []
    
    times_naive = []
    times_h0 = []
    times_h1 = []
    
    for i, word in enumerate(test_words, 1):
        print(f"Test {i}/{num_tests} : mot = '{word}'")
        
        # Naïve
        start = time.time()
        attempts_naive = e2.partieNaive(word)
        time_naive = time.time() - start
        results_naive.append(attempts_naive)
        times_naive.append(time_naive)
        print(f"  Naïve (random)      : {attempts_naive} tentatives ({time_naive:.3f}s)")
        
        # Heuristique 0
        start = time.time()
        attempts_h0 = e3.partieIA(word, heuristique=0)
        time_h0 = time.time() - start
        results_h0.append(attempts_h0)
        times_h0.append(time_h0)
        print(f"  Heuristique 0       : {attempts_h0} tentatives ({time_h0:.3f}s)")
        
        # Heuristique 1
        start = time.time()
        attempts_h1 = e3.partieIA(word, heuristique=0)
        time_h1 = time.time() - start
        results_h1.append(attempts_h1)
        times_h1.append(time_h1)
        print(f"  Heuristique 1       : {attempts_h1} tentatives ({time_h1:.3f}s)")
        print()
    
    print("RÉSULTATS FINAUX")
    print("----------------------------------------------")
    print()
    
    
    print_stats_results("Naïve (random)", results_naive, times_naive)
    print_stats_results("Heuristique 0", results_h0, times_h0)
    print_stats_results("Heuristique 1", results_h1, times_h1)
    
    print("COMPARAISON ET AMÉLIORATIONS")
    print("----------------------------------------------")
    print()
    
    avg_naive = mean(results_naive)
    avg_h0 = mean(results_h0)
    avg_h1 = mean(results_h1)
    
    improvement_h0 = ((avg_naive - avg_h0) / avg_naive * 100) if avg_naive > 0 else 0
    improvement_h1 = ((avg_naive - avg_h1) / avg_naive * 100) if avg_naive > 0 else 0
    
    print(f"Heuristique 0 vs Naïve : {improvement_h0:+.1f}% ({avg_h0:.2f} vs {avg_naive:.2f})")
    print(f"Heuristique 1 vs Naïve : {improvement_h1:+.1f}% ({avg_h1:.2f} vs {avg_naive:.2f})")
    
    if avg_h0 > 0 and avg_h1 > 0:
        if avg_h0 < avg_h1:
            diff = ((avg_h1 - avg_h0) / avg_h0 * 100)
            print(f"Heuristique 0 vs 1     : {diff:+.1f}% meilleure")
        else:
            diff = ((avg_h0 - avg_h1) / avg_h1 * 100)
            print(f"Heuristique 1 vs 0     : {diff:+.1f}% meilleure")
    print()


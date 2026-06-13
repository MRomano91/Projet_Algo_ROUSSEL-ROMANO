"""
Fonctions associées à l'approche naïve de l'exercice 2
"""
import Motus.Tools.GameTools as gt
import Motus.Tools.RandomWord as rd
import Motus.TxtLoader.DataLoader as datas
import Graphic.Output as out


def GetPossibleWords(x : str, dico : dict[int, list[str]]) -> list[str]:
    """
    Accede a la liste des propositions valides parmi un dictionnaire dico etant donne un mot x a deviner
    Complexite :
        - Temps : O(1)
    param :
        x : mot à deviner
        dico : un ensemble de mots
    return :
        l'ensemble des mots de dico qui peuvent être obtenus à partir de x 
    """
    return dico[len(x)]

def update(words : list[str], w : str, comp : list[int]) -> list[str]: 
    """
    Renvoie la liste des mots x parmi ceux de la liste words tels que compare(w,x) = comp.
    param :
        words : une liste de mots 
        w : meilleur mot
        comp : un tableau d'entiers de taille len(x) qui décrit le match entre x et le dernier mot testé
    return :
        une liste de mots
    """
    res : list[str] = []
    for x in words :
        if gt.compare(w,x) == comp :
            res.append(x)
    return res

def partieNaive(x : str) -> int:
    """
    Joue automatiquement à MOTUS avec x comme mot à deviner, et renvoie le nombre de tentatives effectuées.
    param :
        x : une chaîne de caractères
    return :
        le nombre de tentatives effectuées
    """
    robert : dict[int, list[str]] = datas.loadDico("datas/scrabble.txt")
    matching_words : list[str] = GetPossibleWords(x, robert)
    current_best_word : str = rd.randomWord(matching_words)
    comp = gt.compare(current_best_word,x) 
    tours_de_jeu : int = 1
    
    while current_best_word != x:

        out.AfficherMotus(current_best_word,comp)
        matching_words = update(matching_words,current_best_word,comp)
        current_best_word = rd.randomWord(matching_words)
        comp = gt.compare(current_best_word,x)
        tours_de_jeu += 1
    
    comp = gt.compare(current_best_word,x)
    out.AfficherMotus(current_best_word,comp)
    return tours_de_jeu

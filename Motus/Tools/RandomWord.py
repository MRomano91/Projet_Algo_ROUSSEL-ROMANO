import random

def randomWord(dico : list[str]) -> str:
    """
    Renvoie un mot aléatoire d'une liste de mots.
    Complexite :
        - Temps : O(1)
        - Espace : O(1)
    param :
        dico: la liste de mots
    return:
        un mot aléatoire de la liste
    """

    return dico[random.randint(0, len(dico) - 1)]

def randomWordFromDico(dico : dict[int, list[str]], l : int) -> str:
    """
    Renvoie un mot aléatoire d'une liste de taille "l" de mots contenue dans un dictionnaire.
    Complexite :
        - Temps : O(1)
        - Espace : O(1)
    param :
        dico: dictionnaire de listes de mots
        l: la longueur du mot à renvoyer
    return:
        un mot aléatoire de la liste
    """
    return dico[l][random.randint(0, len(dico[l]) - 1)]
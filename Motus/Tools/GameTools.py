"""

"""
from . import Rechercher as rech
import copy

def isValid(w : str , x : str , dico : dict[int, list[str]]) -> bool:
    """"
    Determine si w est une proposition valide: 
        - Si w a la bonne longueur ?
        - La bonne premiere lettre ?
        - S'il existe dans le dictionnaire ?
    Complexite :
        - Temps : O(log (n)), avec n le nombre de mots de la longueur de x
    param :
        w: le mot à vérifier
        x: le mot à deviner
        dico: le dictionnaire contenant les mots triés par longueur
    return:
        True si "w" est une proposition valide et False sinon
    """
    if w[0] != x[0] : return False
    if len(w) != len(x) : return False
    return rech.inside(w,dico[len(w)])

def compare(w : str , x : str) -> list[int]:
    """
    Compare deux mots et renvoie un tableau de taille len(w) indiquant pour chaque lettre 
    si elle est bien placée, mal placée ou absente.
    Complexite :
        - Temps : O(len(w)).
    param :
        w: le mot proposé
        x: le mot à deviner
    return :  
        un tableau t de taille l = len(w) dont la valeur en position i est 
            - 2 si w[i] est bien place
            - 1 si w[i] est mal place (attention a ne pas utiliser plusieurs fois la meme lettre de x !)
            - 0 sinon
    
    """
    n = len(w)
    if n != len(x) : raise ValueError(f"compare2(w,x) :\n   len diff Erreur : {w} has not the same shape as {x}")
    
    res : list[int] = [0] * n
    x_list = list(x)
    
    for i in range(n):
        if w[i] == x[i]:
            res[i] = 2
            x_list[i] = None  # Marquer comme utilisée
    
    for i in range(n):
        if res[i] == 0 and w[i] in x_list:
            res[i] = 1
            x_list[x_list.index(w[i])] = None
    
    return res


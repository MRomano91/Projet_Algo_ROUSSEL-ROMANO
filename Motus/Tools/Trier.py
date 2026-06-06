"""
Fonctions de trie utiles pour le projet
"""

def Split(l) :
    """
    Sépare une liste en deux parties égales (ou presque)
    param :
        l: la liste à séparer
    return:
        deux listes résultantes
    """
    n = len(l)
    if n <= 1 :
        return l, []
    mid = n // 2
    return l[:mid], l[mid:]

def FusionListeString(l1,l2) :
    """
    Fusionne deux listes de chaînes de caractères triées en une seule liste triée
    param :
        l1: première liste triée
        l2: deuxième liste triée
    return:
        liste fusionnée et triée
    """
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2) :
        if l1[i] < l2[j] :
            res.append(l1[i])
            i += 1
        else :
            res.append(l2[j])
            j += 1
    res.extend(l1[i:])
    res.extend(l2[j:])
    return res

def TrieFusionListeString(l : list[str]) -> list[str]:
    """
    Trie une liste de chaînes de caractères par ordre alphabétique
    param :
        l: la liste de chaînes de caractères à trier
    return: 
        la liste triée
    """
    if len(l) <= 1 : 
        return l
    l1,l2 = Split(l)
    lt1 = TrieFusionListeString(l1)
    lt2 = TrieFusionListeString(l2)
    return FusionListeString(lt1,lt2)

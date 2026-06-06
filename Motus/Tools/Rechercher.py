def inside(w : str , lst : list[str]) -> bool:
    """
    Recherche dichotomique d'un mot dans une liste de chaînes de caractères triée par ordre alphabétique
     Complexite :
        - Temps : O(log( |n_lst| ))
    param :
        w: le mot à chercher
        lst: la liste de chaînes de caractères triée par ordre alphabétique
    return:
        True si "w" est présente dans "lst" et False sinon
    """

    # Cas de base où la liste est vide 
    if len(lst) == 0:
        return False

    # Calcul de l'indice du milieu
    middle = len(lst)//2

    # Cas de base où le mot a été trouvé
    if lst[middle] == w:
        return True
    
    # Cas de base où le mot n'a pas été trouvé 
    # et le tableau n'a qu'un élément (milieu = 0)
    elif middle == 0:
        return False
    
    # Recherche dans les mots à gauche du milieu
    elif lst[middle] > w:
        return inside(w, lst[0 : middle])

    # Recherche dans les mots à droite du milieu
    elif lst[middle] < w:
        return inside(w, lst[middle+1 : len(lst)])

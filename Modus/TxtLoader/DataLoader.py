def loadDico(path : str) -> dict[int, list[str]]:
    """
    Charge un dictionnaire de mots à partir d'un fichier texte et les trie par longueur.
    Complexite :
        - Temps : O(n log n) où n est le nombre de mots dans le fichier
        - Espace : O(n)
    param :
        path: le chemin vers le fichier texte contenant les mots
    return:
        Un dictionnaire où les clés sont les longueurs des mots et les valeurs sont des listes de mots de cette longueur
    """
    
    dico_file = open(path, 'r')

    dico = {}
    for word in dico_file:
        if word.strip() is not None:

            l = len(word.strip())

            # Si le tableau des mots de longueur l n'existe pas
            # On le crée
            if l not in dico.keys():
                dico[l] = [word.strip()]

            else:
                dico[l].append(word.strip())

    dico_file.close()
    return dico
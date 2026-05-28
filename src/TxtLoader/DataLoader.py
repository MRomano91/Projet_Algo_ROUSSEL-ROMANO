"""
A completer
"""
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
    return
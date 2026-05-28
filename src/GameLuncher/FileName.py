"""
Fichier à renommer

Ecrire une fonction partie(n) qui lance une partie en n essais.
— Le programme choisit un mot x a faire deviner, et affiche sa longueur et sa
premiere lettre.
— Pour chaque proposition du joueur, le programme verifie que le mot est valide
(autrement il demande une nouvelle proposition sans incrementer le nombre
d'essais effectues), puis affiche les lettres bien et mal placees.
— Le programme s'arrete quand le joueur a trouve le mot, ou bien s'il a epuise ses
essais. Il termine en affichant le resultat de la partie.

"""

def partie(n : int) -> None:
    """
    Lance une partie en n essais.
    param :
        n: le nombre d'essais
    return: 
        None
    """
    return
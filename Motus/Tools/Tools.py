"""
Outils généraux
"""

def Liste1DtoString(l:list) -> str:
    s : str = "["
    for e in l :
        s += " " + str(e)
    s += " ]"
    return s

def Tableau2DtoString(t : list[list]) -> str:
    s : str = "["
    for l in t :
        s += "\n" + Liste1DtoString(l)
    s += "\n]"
    return s
"""
Devrait - on  le mettre dans Tools ? mail ?
"""

import colorama

colorama.init()
RED = colorama.Back.RED
GREEN = colorama.Back.GREEN
END = colorama.Back.RESET

def printRed(a):
    print(RED+a+END,end='')

def printGreen(a):
    print(GREEN+a+END,end='')

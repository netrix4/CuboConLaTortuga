"""
Codigo De: Mario De Jesus Arias Hernandez
Practica de la tortuga

Todo: usar la funcion de dot para hacer lineas y hacer lo mismo
"""

import turtle as t
from random import random

angle = 90
lineLenght = 250

def DrawSingleCube():
    for i in range(4):
        t.right(angle)
        t.fd(lineLenght)

def ConectTwoCubes():
    t.right(angle)
    t.fd(lineLenght)

    t.right(angle-45)
    t.fd(lineLenght*.66)

    t.right(angle-45)
    t.fd(lineLenght)

    t.right(angle+45)
    t.fd(lineLenght*.66)

    t.left(angle-45)
    t.fd(lineLenght)

    t.left(angle+45)
    t.fd(lineLenght*.66)


DrawSingleCube()

t.left(angle-45)
t.fd(lineLenght*.66)
t.right(angle-45)

DrawSingleCube()

ConectTwoCubes()

input("Presiona enter para salir...")


# DrawCube()
# 1.
# Derecha |90º|
# derecho |l|
# 2.
# Derecha |90º|
# derecho |l|
# 3.
# Derecha |90º|
# derecho |l|
# 4.
# Derecha |90º|
# derecho |l|


# DrawCube()
# 5.
# #           derecha(315)
# left |45º|
# derecho |l-10|

# drawcube()

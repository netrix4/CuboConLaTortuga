"""
Codigo De: Mario De Jesus Arias Hernandez
Practica de la tortuga con interpolacion

"""

from turtle import Turtle

t = Turtle()
angle = 90
lineLenght = 150

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

def calcslope()

def drawline(destination):
    origin = t.position()

    print('Orignen:',origin)
    print('Destino',destination)

    # m = (y2-y1)/(x2-x1)
    m = (destination[1]- origin[1]) / (destination[0]-origin[0])
    print('Pendiente: ',m)

    punto pendiente



t.screen.screensize(400,300)
t.screen.title('Interpolacion con la tortuga')
# t.screen.bgcolor('lightgray')
# t.screen.bgcolor(0,.5,.5)


# DrawSingleCube()

t.dot()
drawline((20,10))

t.screen.mainloop()





"""
Primero dibujar una recta con un punto destino (10,10)
    encontrar la pendiente
    punto-pendiente

"""
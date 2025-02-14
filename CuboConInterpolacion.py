"""
Codigo De: Mario De Jesus Arias Hernandez
Practica de la tortuga con interpolacion

"""

from turtle import Turtle
import math

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


def calcYForX(slope, x, point):
    # y-y1 = m (x-y1)
    # y = m (x-x1) + y1

    # y = (slope*point[0]-slope*point[0])+point[1]

    y = math.floor((slope * (x - point[0])) + point[1])
    # y = .28*(0+35) + 10
    print(f'm={slope} x={x} point={point}, y={y}')

    return (x, y)

def calcSlope(origin, destination):
    # m = (y2-y1)/(x2-x1)
    # m = abs((destination[1]- origin[1]) / (destination[0]- origin[0]))
    m = (destination[1]- origin[1]) / (destination[0]- origin[0])
    return m
        

def drawLine(destination):
    print('Dibujar una linea')
    origin = t.position()

    print('Origen:',origin)
    print('Destino: ',destination)

    if (destination[0] != origin[0]):
        slope = calcSlope(origin, destination)

        print('Pendiente: ',slope)

        isLeft2Right=(destination[0] > origin[0])
        stepsDirection = 1 if isLeft2Right else -1

        for x in range(int(origin[0]), int(destination[0]), stepsDirection):
            coordinateX = x+1
            # pointWithinLine = calcYForX(slope, coordinateX ,destination)
            pointWithinLine = calcYForX(slope, x ,origin)
            print(f'Nuevo punto -> {isLeft2Right}:  {pointWithinLine}')

            t.setx(pointWithinLine[0])
            t.sety(pointWithinLine[1])

            t.dot(3,'lightblue')

    else:
        isDown2Up=(destination[1] > origin[1])
        stepsDirection = 1 if isDown2Up else -1

        destAbsY = abs(destination[1])
        originAbsY = abs(origin[1])

        initialPoint = int(originAbsY) if destAbsY > originAbsY else int(destAbsY)
        finalPoint = int(originAbsY) if destAbsY < originAbsY else int(destAbsY)
        
        print(f'initial: {initialPoint} final:{finalPoint} steps: {stepsDirection}')

        for y in range(initialPoint, finalPoint, 1):
            
            pointWithinLine = (origin[0], (y+1)*stepsDirection)
            print(f'Nuevo punto \, {isDown2Up}:  {pointWithinLine}')

            t.setx(pointWithinLine[0])
            t.sety(pointWithinLine[1])

            t.dot(3,'lightblue')
        
    


t.screen.screensize(400,300)
t.screen.title('Interpolacion con la tortuga')
t.penup()
print(t.position())
t.dot(8,'red')

# drawLine((10,-10))

#aqui es 0,0
# drawLine((25,0))
# drawLine((24,-25))
# drawLine((0,-24))
# drawLine((-1,0))

t.setx(0)
t.sety(0)
# 1 CHECK 
drawLine((100,0))
t.setx(0)
t.sety(0)
# 2 Check
drawLine((-100,20))
t.setx(0)
t.sety(0)
# 3 check
drawLine((250,100))
t.setx(0)
t.sety(0)
# 4 
drawLine((0,200))
t.setx(0)
t.sety(0)
# 5 check
drawLine((0,-100))



t.screen.mainloop()




'''
La pendiente es 0 cuando Xdestino y Xinicio sin iguales (recta horizontal <-|->)

La pendiente es indefinida cuando Ydestino y Yinicio son iguales (Recta vertical |^  |  \|/)
cuando la recta es a la izquierda <- se itera el rango hacia atras
cuando la recta es a la derecha -> se itera el rango hacia adelante
'''



"""
Primero dibujar una recta con un punto destino (10,10)
    encontrar la pendiente
    punto-pendiente

"""
# p1= 2,4
# p2= 4,5


# 1.-
# m = (y2-y1)/(x2-x1)
# y-y1 = m (x-x1)
# y = mx + b


# m = (4-5)/4-2
# m = -1/2
# m = -0.5
# |m| = 0.5

# 2.-
# y -y2 = m (xnuevo - x2)
# y = m (xnuevo - x2) + y2

# y = .5(3-4)+5

# y = .5(-1)+5 = 4.5

































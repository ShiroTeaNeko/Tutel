import math

import numpy
import turtle
import random


def dessine_carre_colore(longueur, couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for compteur in range(0, 4):
        turtle.forward(longueur)
        turtle.left(90)
    turtle.end_fill()
    return None


def dessine_rectangle_colore(longueur, largeur, couleur):
    turtle.down()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for compteur in range(0, 2):
        turtle.forward(longueur)
        turtle.left(90)
        turtle.forward(largeur)
        turtle.left(90)
    turtle.end_fill()
    return None


def dessine_triangle_colore(base, hauteur):
    turtle.down()
    turtle.fillcolor('#000000')
    turtle.begin_fill()
    a = math.degrees(numpy.arctan(hauteur / (base / 2)))
    hyp = numpy.sqrt(math.pow(hauteur, 2) + math.pow(base / 2, 2))
    turtle.forward(base)
    turtle.left(180 - a)
    turtle.forward(hyp)
    turtle.left(a * 2)
    turtle.forward(hyp)
    turtle.setheading(0)
    turtle.end_fill()
    return None


def dessine_demidisque_colore(rayon, couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.forward(rayon * 2)
    turtle.left(90)
    turtle.circle(rayon, 180)
    turtle.end_fill()
    return None


def dessine_window():
    # color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    # turtle.fillcolor(color)
    turtle.up()
    turtle.speed(1)
    turtle.forward(12.5)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.begin_fill()
    turtle.down()
    dessine_carre_colore(30, '#ffffff')
    turtle.up()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

    return None


def dessine_door():
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    turtle.fillcolor(color)
    turtle.up()
    turtle.forward(12.5)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.circle(30 / 2, 180)
    turtle.forward(30)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(30)
    return None


def dessine_door_etage():
    turtle.fillcolor('#ffffff')
    turtle.up()
    turtle.forward(12.5)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(30)
    return None


def dessine_RDC_colore(couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    list = [dessine_window, dessine_door, dessine_window]
    random.shuffle(list)
    dessine_rectangle_colore(largeur, 60, couleur)
    for c in range(0, 3):
        list[c]()


def dessine_etage_colore(etage, couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    list = [dessine_window, dessine_door_etage]
    dessine_rectangle_colore(largeur, 60, couleur)
    for c in range(0, 3):
        random.choice(list)()


def dessine_immeuble_colore():
    turtle.down()
    turtle.forward(50)
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    turtle.fillcolor(color)
    turtle.begin_fill()

    dessine_RDC_colore(color)
    etage = random.randint(0, 4)
    for e in range(0, etage):
        turtle.goto(drawImmeublePos + offset, 60 + 60 * e)
        dessine_etage_colore(etage, color)

    turtle.goto(drawImmeublePos + offset, 60 + 60 * etage)
    dessine_triangle_colore(140, 50)
    turtle.up()

### MAIN PROGRAM ###
c = 0
drawImmeublePos = start = -1000
offset = 50
largeur = 140
turtle.speed(0.5)
turtle.up()
turtle.goto(start, 0)
turtle.setup(width=1920, height=1080, startx=None, starty=None)
while True:
    dessine_immeuble_colore()
    c += 1
    drawImmeublePos += largeur + offset
    turtle.goto(drawImmeublePos, 0)


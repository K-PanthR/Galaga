import pgzrun
import random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 500
HEIGHT = 400

ship = Actor("galaga")
bullet = Actor("bullet")
enemey = Actor("bug")

ship.x = WIDTH//2
ship.y = HEIGHT-50

speed = 4

bullets = []
enemies = []

def update():
    if keyboard.left:
        ship.x  -= 4
        if ship.x<0:
            ship.x = WIDTH//2
    if keyboard.right:
        ship.x += 4
        if ship.x>WIDTH:
            ship.x = WIDTH//2

    for bullet in bullets:
        if keyboard.space:
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    ship.draw()

pgzrun.go()
import pgzrun
import random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 500
HEIGHT = 400

ship = Actor("galaga")

ship.x = WIDTH//2
ship.y = HEIGHT-50

speed = 50

score=0

direction = 1

bullets = []
enemies = []

for i in range(8):
   enemies.append(Actor("bug1"))
   enemies[-1].x = 100 + 80 * x
   enemies[-1].y = -100 

def on_key_down(key):
    if key== keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50       

def update():
    global score
    global direction
    move_down = False  

    if keyboard.left:
        ship.x  -= 4
        if ship.x<0:
            ship.x = WIDTH//2
    if keyboard.right:
        ship.x += 4
        if ship.x>WIDTH:
            ship.x = WIDTH//2
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
        
    if len(enemies) > 0 and enemies[-1].x > WIDTH - 80 or enemies[0].x < 80:
        move_down = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x +=5*direction
        if move_down == True:
            enemy.y += 50
        
    for bullet in bullets:
        if bug.colliderect(bullet):
            bullets.remove(bullet)
            enemies.remove(bug)
            score  += 100

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for bug in enemies:
        bug.draw()
    ship.draw()


pgzrun.go()
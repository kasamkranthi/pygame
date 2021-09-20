import pygame
import math
import random
import time
from pygame.locals import *
from config import *


#from pygame.font import FontType
#from pygame.ftfont import Font


speed = 0
value = 0
value2 = 0
k = 1
round = 1
scorer1 = 0
scorer2 = 0
t2 = 0

def final1(points1, tim):
    score_val = score_font.render("Score of player1 :  " + str(points1), True, (255, 0, 0))
    screen.blit(score_val, (400, 100))
    score_vally = score_font.render("Time of player1 : " + str(tim//170), True, (255, 0, 0))
    screen.blit(score_vally, (400, 200))


def final2(points2, tim2):
    score_val = score_font.render("Score of player2 :  " + str(points2), True, (255, 0, 0))
    screen.blit(score_val, (400, 300))
    score_vally2 = score_font.render("Time of player1 : " + str(tim2//170), True, (255, 0, 0))
    screen.blit(score_vally2, (400, 400))



def show(score, round):
    score_val = score_font.render("Score of player1 in round" + str(round) + "  :  " + str(score), True, (255, 0, 0))
    screen.blit(score_val, (10, 800 - 60))


def show2(score10, round):
    score_val2 = score_font.render("Score of player2 in round" + str(round) + "  :  " + str(score10), True, (255, 0, 0))
    screen.blit(score_val2, (400, 10))

def printit(timeraa):
    score_val3 = score_font.render("Time is :  " + str(timeraa//170), True, (255, 0, 0))
    screen.blit(score_val3, (0, 0))

def showit(score2):
    score = score_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(score, (420, 300))
    score1 = score_font.render("Click Enter to continue", True, (255, 0, 0))
    screen.blit(score1, (280, 500))
    score_val = score_font.render("Score of player1 :  " + str(score2), True, (255, 0, 0))
    screen.blit(score_val, (350, 400))


def showit2(score10):
    score = score_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(score, (420, 300))
    score1 = score_font.render("Click Enter to continue", True, (255, 0, 0))
    screen.blit(score1, (280, 500))
    score_val = score_font.render("Score of player2 :  " + str(score10), True, (255, 0, 0))
    screen.blit(score_val, (350, 400))


a = 1
obs1 = random.randint(0, 1200)
obs2 = random.randint(0, 1200)
obs3 = random.randint(0, 1200)
obs4 = random.randint(0, 1200)
obsy1 = 85 + 80
obsy2 = 85 + 80 + 160
set1 = 0
set2 = 0
obsy3 = 85 + 80 + 160 + 160
obsy4 = 85 + 80 + 160 + 160 + 160
x11 = 0
x12 = 500
x13 = 1000
x21 = 250
x22 = 750
x31 = 0
x32 = 500
x33 = 1000
x41 = 250
x42 = 750
y11 = 85
y12 = 85
y13 = 85
y21 = 85 + 160
y22 = 85 + 160
y31 = 85 + 320
y32 = 85 + 320
y33 = 85 + 320
y41 = 85 + 480
y42 = 85 + 480

x = 550
y = 720
x2 = 550
y2 = 20

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Get Set Cross")
player = pygame.image.load('ship.png')
obstacle = pygame.image.load('cube.png')
player2 = pygame.image.load('ship.png')


def player1():
    screen.blit(player, (x, y))


def player3():
    screen.blit(player2, (x2, y2))


def obstacles():
    screen.blit(obstacle, (x11, y11))
    screen.blit(obstacle, (x12, y12))
    screen.blit(obstacle, (x13, y13))
    screen.blit(obstacle, (x21, y21))
    screen.blit(obstacle, (x22, y22))
    screen.blit(obstacle, (x31, y31))
    screen.blit(obstacle, (x32, y32))
    screen.blit(obstacle, (x33, y33))
    screen.blit(obstacle, (x41, y41))
    screen.blit(obstacle, (x42, y42))


def moving1():
    screen.blit(obstacle, (obs1, obsy1))


def moving2():
    screen.blit(obstacle, (obs2, obsy2))


def moving3():
    screen.blit(obstacle, (obs3, obsy3))


def moving4():
    screen.blit(obstacle, (obs4, obsy4))


def change1():
    obs1 = +1


def change2():
    obs2 = +1


def change3():
    obs2 = +1


t1 = 1
# game loop
running = True
while running:
    if round <= 3:
        if round == 1:
            speed = 1
        if round == 2:
            speed = 2
        if round == 3:
            speed = 3

        if a == 1 and k % 2 == 1:
            t1 += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 119, 190))
            pygame.draw.rect(screen, brown, [0, 0, 1200, 85])
            pygame.draw.rect(screen, brown, [0, 85, 1200, 70])

            pygame.draw.rect(screen, black, [0, 85 + 70, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 80, 1200, 10])
            pygame.draw.rect(screen, brown, [0, 85 + 70 + 80 + 10, 1200, 70])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 160, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 240, 1200, 10])
            pygame.draw.rect(screen, brown, [0, 85 + 70 + 240 +10, 1200, 70])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 320, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 320, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 400, 1200, 10])
            pygame.draw.rect(screen, brown, [0, 85 + 70 + 400 + 10, 1200, 70])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 480, 1200, 10])
            pygame.draw.rect(screen, brown, [0, 715, 1200, 85])
            if obs1 < 1200:
                obs1 += speed
            if obs2 < 1200:
                obs2 += speed
            if obs3 < 1200:
                obs3 += speed
            if obs4 < 1200:
                obs4 += speed

            obstacles()
            moving1()
            moving2()
            moving3()
            moving4()
            player1()
            player3()

            if obs1 >= 1200:
                obs1 -= 1200
            if obs2 >= 1200:
                obs2 -= 1200
            if obs3 >= 1200:
                obs3 -= 1200
            if obs4 >= 1200:
                obs4 -= 1200

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x <= 1200 - 64:
                    x += 1.5

                if event.key == pygame.K_LEFT and x > 0:
                    x -= 1.5

                if event.key == pygame.K_UP and y > 0:
                    y -= 1.5

                if event.key == pygame.K_DOWN and y <= 800 - 64:
                    y += 1.5
            if math.fabs(x - x31) <= 64 and math.fabs(y - y31) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x32) <= 64 and math.fabs(y - y32) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x33) <= 64 and math.fabs(y - y33) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x11) <= 64 and math.fabs(y - y11) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x12) <= 64 and math.fabs(y - y12) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x13) <= 64 and math.fabs(y - y13) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x21) <= 64 and math.fabs(y - y21) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x22) <= 64 and math.fabs(y - y22) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x41) <= 64 and math.fabs(y - y41) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - x42) <= 64 and math.fabs(y - y42) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(obs1 - x) <= 64 and math.fabs(y - obsy1) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - obs2) <= 64 and math.fabs(y - obsy2) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if math.fabs(x - obs3) <= 64 and math.fabs(y - obsy3) <= 64:
                x = 550
                y = 720
                a = 0
            if math.fabs(x - obs4) <= 64 and math.fabs(y - obsy4) <= 64:
                x = 550
                y = 720
                a = 0
                set2 = 1
            if value == 100:
                x = 550
                y = 720
                a = 0
                set2 = 1

            if y < 800 - 85 - 70 - 64:
                if value <= 10:
                    value = 10
            if y < 800 - 85 - 70 - 80 - 64:
                if value <= 25:
                    value = 25
            if y < 800 - 85 - 70 - 80 - 80 - 64:
                if value <= 35:
                    value = 35
            if y < 800 - 85 - 70 - 80 - 80 - 80 - 64:
                if value <= 50:
                    value = 50

            if y < 800 - 85 - 70 - 80 - 80 - 80 - 80 - 64:
                if value <= 60:
                    value = 60
            if y < 800 - 85 - 70 - 80 - 80 - 80 - 80 - 80 - 64:
                if value <= 75:
                    value = 75
            if y < 800 - 85 - 70 - 80 - 80 - 80 - 80 - 80 - 80 - 64:
                if value <= 85:
                    value = 85
            if y < 800 - 85 - 70 - 80 - 80 - 80 - 80 - 80 - 80 - 80 - 64:
                if value <= 100:
                    value = 100
            show(value, round)
            show2(value2, round)
            printit(t1)
        if a == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 119, 190))
            if k % 2 == 1:
                if set2 == 1:
                    scorer1 += value
                    set2 = 0
                    value = 0
                showit(scorer1)
            if k % 2 == 0:
                if set1 == 1:
                    scorer2 += value2
                    set1 = 0
                    value2 = 0
                showit2(scorer2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if a == 0 and k % 2 == 0:
                        round += 1
                    a = 1
                    k += 1
        if a == 1 and k % 2 == 0:
            t2 += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 119, 190))
            pygame.draw.rect(screen, brown, [0, 0, 1200, 85])
            pygame.draw.rect(screen, black, [0, 85 + 70, 1200, 10])
            pygame.draw.rect(screen, brown, [0, 85 + 70 + 10, 1200, 70])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 80, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 160, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 240, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 320, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 320, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 400, 1200, 10])
            pygame.draw.rect(screen, black, [0, 85 + 70 + 480, 1200, 10])

            pygame.draw.rect(screen, brown, [0, 715, 1200, 85])
            if obs1 < 1200:
                obs1 += speed
            if obs2 < 1200:
                obs2 += speed
            if obs3 < 1200:
                obs3 += speed
            if obs4 < 1200:
                obs4 += speed

            obstacles()
            moving1()
            moving2()
            moving3()
            moving4()
            player3()
            player1()

            if obs1 >= 1200:
                obs1 -= 1200
            if obs2 >= 1200:
                obs2 -= 1200
            if obs3 >= 1200:
                obs3 -= 1200
            if obs4 >= 1200:
                obs4 -= 1200

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x2 <= 1200 - 64:
                    x2 += 1

                if event.key == pygame.K_LEFT and x2 > 0:
                    x2 -= 1

                if event.key == pygame.K_UP and y2 > 0:
                    y2 -= 1

                if event.key == pygame.K_DOWN and y2 <= 800 - 64:
                    y2 += 1
            if math.fabs(x2 - x31) <= 64 and math.fabs(y2 - y31) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x32) <= 64 and math.fabs(y2 - y32) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x33) <= 64 and math.fabs(y2 - y33) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x11) <= 64 and math.fabs(y2 - y11) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x12) <= 64 and math.fabs(y2 - y12) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x13) <= 64 and math.fabs(y2 - y13) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x21) <= 64 and math.fabs(y2 - y21) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x22) <= 64 and math.fabs(y2 - y22) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x41) <= 64 and math.fabs(y2 - y41) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - x42) <= 64 and math.fabs(y2 - y42) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(obs1 - x2) <= 64 and math.fabs(y2 - obsy1) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - obs2) <= 64 and math.fabs(y2 - obsy2) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - obs3) <= 64 and math.fabs(y2 - obsy3) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if math.fabs(x2 - obs4) <= 64 and math.fabs(y2 - obsy4) <= 64:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if value2 == 100:
                x2 = 550
                y2 = 20
                a = 0
                set1 = 1
            if y2 < 85 - 64:
                if value2 < 0:
                    value2 = 0
            if y2 > 85:
                if value2 <= 0:
                    value2 = 0
            if y2 > 85 + 70:
                if value2 <= 15:
                    value2 = 15
            if y2 > 85 + 70 + 80:
                if value2 <= 25:
                    value2 = 25

            if y2 > 85 + 70 + 80 + 80:
                if value2 <= 40:
                    value2 = 40
            if y2 > 85 + 70 + 80 + 80 + 80:
                if value2 <= 50:
                    value2 = 50
            if y2 > 85 + 70 + 80 + 80 + 80 + 80:
                if value2 <= 65:
                    value2 = 65
            if y2 > 85 + 70 + 80 + 80 + 80 + 80 + 80:
                if value2 <= 75:
                    value2 = 75
            if y2 > 85 + 70 + 80 + 80 + 80 + 80 + 80 + 80:
                if value2 <= 90:
                    value2 = 90
            if y2 > 85 + 70 + 80 + 80 + 80 + 80 + 80 + 80 + 80:
                if value2 <= 100:
                    value2 = 100

            show2(value2, round)
            show(value, round)
            printit(t2)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 119, 190))
        final1(scorer1, t1)
        final2(scorer2, t2)
        if scorer1 > scorer2:
            score_val = score_font.render("PLAYER1 WON", True, (255, 0, 0))
            screen.blit(score_val, (400, 500))
        if scorer1 < scorer2:
            score_val = score_font.render("PLAYER2 WON", True, (255, 0, 0))
            screen.blit(score_val, (400, 500))
        if scorer1 == scorer2 and t1 == t2:
            score_val = score_font.render("DRAW", True, (255, 0, 0))
            screen.blit(score_val, (400, 500))
        score_val2 = score_font.render("click F1 to exit", True, (255, 0, 0))
        screen.blit(score_val2, (400, 600))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            running = False

    pygame.display.update()


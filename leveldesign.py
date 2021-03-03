#!/usr/bin/env python3
# coding:utf8
import pygame
import Classes

walls = []
traps = []
monsters = []
checkpoint = []
messages = []
objects1 = []
# TUTO
#checkpoints
checkpoint.append(Classes.ground(-10900, -2620, 100, 120))
checkpoint[-1].checkpoint = True
checkpoint.append(Classes.ground(-5300, -1320, 100, 120))
checkpoint[-1].checkpoint = True
checkpoint.append(Classes.ground(0, -1120, 100, 120))
checkpoint[-1].checkpoint = True
#messages
messages.append(Classes.message(-10900, -2600, 1))
messages.append(Classes.message(-10000, -1980, 2, 500, 180))
messages.append(Classes.message(-9500, -2500, 3))
#messages.append(Classes.message(-8900, -1980, 7))
messages.append(Classes.message(-7670, -1980, 4))
messages.append(Classes.message(-6200, -1980, 5))
messages.append(Classes.message(-4500, -960, 6))
messages.append(Classes.message(-50, 960, 8, 200, 60))
#contours
walls.append(Classes.ground(-12000, -1000, 10000, 1000))#mur du bas
walls.append(Classes.ground(-12000, -4000, 1000, 4000))# murs de gauche
#walls.append(Classes.ground(-12000, -4000, 12000, 1000))#mur du haut
#grands murs
walls.append(Classes.ground(-11000, -2500, 500, 2000))
walls.append(Classes.ground(-10500, -2000, 5000, 2000))
walls.append(Classes.ground(-9500, -2600, 500, 600))
walls.append(Classes.ground(-8900, -3000, 500, 500))
walls.append(Classes.ground(-8500, -2350, 200, 500))
walls.append(Classes.ground(-6200, -2150, 100, 200))
walls.append(Classes.ground(-5600, -2150, 100, 500))
walls.append(Classes.ground(-5950, -2450, 100, 250))
walls.append(Classes.ground(-5950, -2300, 200, 100))
walls.append(Classes.ground(-5500, -2550, 200, 1700))
walls.append(Classes.ground(-6050, -2300, 200, 60))
#petits murs
walls.append(Classes.ground(-10500, -2500, 61, 500))
walls.append(Classes.ground(-10450, -2450, 61, 500))
walls.append(Classes.ground(-10400, -2400, 61, 500))
walls.append(Classes.ground(-10350, -2350, 61, 500))
walls.append(Classes.ground(-10300, -2300, 61, 500))
walls.append(Classes.ground(-10250, -2250, 61, 500))
walls.append(Classes.ground(-10200, -2200, 61, 500))
walls.append(Classes.ground(-10150, -2150, 61, 500))
walls.append(Classes.ground(-10100, -2100, 61, 500))
walls.append(Classes.ground(-10050, -2050, 61, 500))
walls.append(Classes.ground(-9550, -2050))
walls.append(Classes.ground(-8550, -2100))
walls.append(Classes.ground(-5000, -1061))
walls.append(Classes.ground(-1960, -1061))
#plateformes horizontales
walls.append(Classes.ground(-9000, -2600, 100, 10))
walls.append(Classes.ground(-8200, -2450, 200, 10))
walls.append(Classes.ground(-6950, -2200, 100, 10))
walls.append(Classes.ground(-6500, -2450, 200, 10))
walls.append(Classes.ground(-6100, -2700, 400, 10))
walls.append(Classes.ground(-4000, -1150, 2000, 10))
walls.append(Classes.ground(-4000, -1300, 2000, 10))
walls.append(Classes.ground(-4000, -1450, 2000, 10))
walls.append(Classes.ground(-4000, -1600, 2000, 10))
walls.append(Classes.ground(-4000, -1750, 2010, 10))
walls.append(Classes.ground(-5300, -1200, 100, 10))
walls.append(Classes.ground(-5300, -1700, 100, 10))
walls.append(Classes.ground(-5300, -2100, 100, 10))
# plateformes verticales
walls.append(Classes.ground(-9650, -2200, 20, 100))
walls.append(Classes.ground(-9800, -2400, 20, 100))
walls.append(Classes.ground(-8650, -2100, 20, 100))
walls.append(Classes.ground(-7950, -2100, 20, 100))
walls.append(Classes.ground(-7250, -2100, 20, 100))
walls.append(Classes.ground(-6850, -2100, 20, 100))
walls.append(Classes.ground(-6050, -2350, 20, 100))
walls.append(Classes.ground(-6500, -2550, 20, 100))
walls.append(Classes.ground(-2300, -1350, 20, 50))
walls.append(Classes.ground(-2000, -1740, 20, 800))

#objets
objects1.append(Classes.objects(-10700, -2600, 100, 100, 0))
objects1.append(Classes.objects(-9800, -2100, 100, 100, 0))
objects1.append(Classes.objects(-9300, -2700, 100, 100, 0))
objects1.append(Classes.objects(-7470, -2100, 100, 100, 0))
objects1.append(Classes.objects(-6000, -2100, 100, 100, 0))
objects1.append(Classes.objects(-4300, -1100, 100, 100, 0))

# pièges
traps.append(Classes.spike(-9000, - 2020))
traps.append(Classes.spike(-8950, - 2020))
traps.append(Classes.spike(-8900, - 2020))
traps.append(Classes.spike(-8850, - 2020))
traps.append(Classes.spike(-7550, - 2020))
traps.append(Classes.spike(-7600, - 2020))
traps.append(Classes.spike(-7650, - 2020))
traps.append(Classes.spike(-7700, - 2020))
traps.append(Classes.spike(-7750, - 2020))
traps.append(Classes.spike(-7800, - 2020))
traps.append(Classes.spike(-7850, - 2020))
traps.append(Classes.spike(-7900, - 2020))
traps.append(Classes.spike(-7950, - 2020))
traps.append(Classes.spike(-8000, - 2020))
traps.append(Classes.spike(-8050, - 2020))
traps.append(Classes.spike(-8100, - 2020))
traps.append(Classes.spike(-8150, - 2020))
traps.append(Classes.spike(-8200, - 2020))
traps.append(Classes.spike(-7350, - 2020))
traps.append(Classes.spike(-7300, - 2020))
traps.append(Classes.spike(-7250, - 2020))
traps.append(Classes.spike(-7200, - 2020))
traps.append(Classes.spike(-7150, - 2020))
traps.append(Classes.spike(-7100, - 2020))
traps.append(Classes.spike(-7050, - 2020))
traps.append(Classes.spike(-7000, - 2020))
traps.append(Classes.spike(-6950, - 2020))
traps.append(Classes.spike(-6900, - 2020))
traps.append(Classes.spike(-6850, - 2020))
traps.append(Classes.spike(-6800, - 2020))
traps.append(Classes.spike(-6750, - 2020))
traps.append(Classes.spike(-6700, - 2020))
traps.append(Classes.spike(-6650, - 2020))
traps.append(Classes.spike(-6600, - 2020))
traps.append(Classes.spike(-6550, - 2020))
traps.append(Classes.spike(-6500, - 2020))
traps.append(Classes.spike(-6450, - 2020))
traps.append(Classes.spike(-6400, - 2020))


traps.append(Classes.spike(-1700, - 1020))
traps.append(Classes.spike(-1400, - 1020))
traps.append(Classes.spike(-1100, - 1020))
traps.append(Classes.spike(-800, - 1020))
traps.append(Classes.spike(-500, - 1020))

traps.append(Classes.spike(-4000, - 1170))
traps.append(Classes.spike(-4000, - 1320))
traps.append(Classes.spike(-4000, - 1470))
traps.append(Classes.spike(-4000, - 1620))
traps.append(Classes.spike(-4000, - 1770))

#monstres
monsters.append(Classes.monster(-4700, 1050, -4500, -5150))
monsters.append(Classes.monster(-4900, 1050, -4500, -5200))
monsters.append(Classes.monster(-5100, 1050, -4500, -5250))
monsters.append(Classes.monster(-5300, 1050, -4500, -5300))

monsters.append(Classes.monster(-4000, -1050, -2100, -4000))
monsters.append(Classes.monster(-3000, -1050, -2100, -4000))
monsters.append(Classes.monster(-3500, -1050, -2100, -4000, "right"))
monsters.append(Classes.monster(-2500, -1050, -2100, -4000, "right"))

monsters.append(Classes.monster(-3700, -1200, -2100, -4000))
monsters.append(Classes.monster(-2750, -1200, -2100, -4000))
monsters.append(Classes.monster(-3250, -1200, -2100, -4000, "right"))
monsters.append(Classes.monster(-2200, -1200, -2100, -4000, "right"))

monsters.append(Classes.monster(-3600, -1350, -2400, -4000))
monsters.append(Classes.monster(-3400, -1350, -2400, -4000))
monsters.append(Classes.monster(-3200, -1350, -2400, -4000))
monsters.append(Classes.monster(-3000, -1350, -2400, -4000))
monsters.append(Classes.monster(-2800, -1350, -2400, -4000))
monsters.append(Classes.monster(-2600, -1350, -2400, -4000))
monsters.append(Classes.monster(-3800, -1350, -2400, -4000, "right"))
monsters.append(Classes.monster(-3600, -1350, -2400, -4000, "right"))
monsters.append(Classes.monster(-3400, -1350, -2400, -4000, "right"))
monsters.append(Classes.monster(-3200, -1350, -2400, -4000, "right"))
monsters.append(Classes.monster(-3000, -1350, -2400, -4000, "right"))
monsters.append(Classes.monster(-2800, -1350, -2400, -4000, "right"))

monsters.append(Classes.monster(-3900, -1500, -2100, -4000))
monsters.append(Classes.monster(-3750, -1500, -2100, -4000))
monsters.append(Classes.monster(-3600, -1500, -2100, -4000))
monsters.append(Classes.monster(-3450, -1500, -2100, -4000))
monsters.append(Classes.monster(-3300, -1500, -2100, -4000))
monsters.append(Classes.monster(-3150, -1500, -2100, -4000))
monsters.append(Classes.monster(-3000, -1500, -2100, -4000))
monsters.append(Classes.monster(-2850, -1500, -2100, -4000))
monsters.append(Classes.monster(-2700, -1500, -2100, -4000))
monsters.append(Classes.monster(-2550, -1500, -2100, -4000))
monsters.append(Classes.monster(-2400, -1500, -2100, -4000))
monsters.append(Classes.monster(-2150, -1500, -2100, -4000))

monsters.append(Classes.monster(-4000, -1650, -2100, -4000))
monsters.append(Classes.monster(-3300, -1650, -2100, -4000))
monsters.append(Classes.monster(-2700, -1650, -2100, -4000))
monsters.append(Classes.monster(-3500, -1650, -2100, -4000, "right"))
monsters.append(Classes.monster(-3000, -1650, -2100, -4000, "right"))
monsters.append(Classes.monster(-2500, -1650, -2100, -4000, "right"))

monsters.append(Classes.monster(-3000, -1800, -2500, -4000))
monsters.append(Classes.monster(-3000, -1800, -2500, -4000, "right"))

monsters.append(Classes.monster(-1500, -1050, -500, -1900))
monsters.append(Classes.monster(-1000, -1050, -500, -1900))
monsters.append(Classes.monster(-1500, -1050, -500, -1900, "right"))
monsters.append(Classes.monster(-1000, -1050, -500, -1900, "right"))


# BOSS 1
#contours
walls.append(Classes.ground(-1000, 900, 17800, 1000))#mur du bas
walls.append(Classes.ground(-2000, -1000, 1000, 2000))# murs de gauche
walls.append(Classes.ground(0, -2580, 1700, 1000))#mur du haut
walls.append(Classes.ground(1000, -2580, 17800, 2700))#autre mur du haut
walls.append(Classes.ground(15780, 0, 1000, 800))#mur de droite
#grands murs
walls.append(Classes.ground(-1000, 0, 750, 1000))
walls[-1].invisible = 1
walls.append(Classes.ground(-1000, -1000, 1000, 1000))
walls.append(Classes.ground(0, -1000, 500, 1000))
walls.append(Classes.ground(4500, 620, 500, 500))
walls.append(Classes.ground(5300, 550, 300, 500))
walls.append(Classes.ground(6500, 550, 300, 500))
#petits murs
walls.append(Classes.ground(2775, 450))
walls.append(Classes.ground(3200, 800))
walls.append(Classes.ground(4239, 700))
walls.append(Classes.ground(4439, 849))
walls.append(Classes.ground(5000, 770, 61, 130))
walls.append(Classes.ground(6000, 849))
walls.append(Classes.ground(6000, 650))
walls.append(Classes.ground(6200, 750))
walls.append(Classes.ground(8410, 740))
walls.append(Classes.ground(8600, 840))
walls.append(Classes.ground(9700, 750))
#plateformes horizontales
walls.append(Classes.ground(1400, 750, 1000, 10))
walls.append(Classes.ground(2300, 600, 500, 10))
walls.append(Classes.ground(2900, 500, 500, 10))
walls.append(Classes.ground(4050, 500, 500, 10))
walls.append(Classes.ground(6000, 550, 500, 10))
walls.append(Classes.ground(6800, 780, 1610, 10))
walls.append(Classes.ground(7700, 680, 500, 10))
walls.append(Classes.ground(8600, 630, 500, 10))
walls.append(Classes.ground(10000, 630, 600, 10))
walls.append(Classes.ground(10500, 520, 200, 10))
walls.append(Classes.ground(10900, 420, 600, 10))
walls.append(Classes.ground(11700, 420, 200, 10))
walls.append(Classes.ground(12600, 420, 2000, 10))
walls.append(Classes.ground(12600, 580, 2000, 10))
walls.append(Classes.ground(12600, 740, 2000, 10))
#verticales
walls.append(Classes.ground(3400, 700, 20, 100))
walls.append(Classes.ground(3600, 490, 20, 500))
walls.append(Classes.ground(5300, 0, 20, 450))
walls.append(Classes.ground(7400, 580, 20, 200))
walls.append(Classes.ground(8400, 580, 20, 200))
walls.append(Classes.ground(8800, 630, 20, 300))
walls.append(Classes.ground(11000, 740, 20, 300))
walls.append(Classes.ground(11350, 595, 20, 300))
walls.append(Classes.ground(11950, 850, 20, 300))
walls.append(Classes.ground(12400, 750, 20, 300))

#bloqueur:
walls.append(Classes.ground(1000, -1080, 1780, 3000))


walls2 = []
traps2 = []
monsters2 = []
checkpoint2 = []
objects2 = []
messages2 = []

#messages
messages2.append(Classes.message(1900, 3680, 8, 200, 60))

#contours
walls2.append(Classes.ground(-1500, 3800, 3000, 1000))
walls2.append(Classes.ground(1500, 4600, 5026, 1000))
walls2.append(Classes.ground(-1500, -1000, 1000, 5800))
walls2.append(Classes.ground(500, -1050, 1000, 4710))
walls2.append(Classes.ground(1000, -2800, 500, 1750))
walls2.append(Classes.ground(2500, -1050, 1000, 5850))
walls2.append(Classes.ground(2500, -2800, 500, 1750))

#checkpoints
checkpoint2.append(Classes.ground(-30, 80, 100, 120))
checkpoint2[-1].checkpoint = True
checkpoint2.append(Classes.ground(-30, 1380, 100, 120))
checkpoint2[-1].checkpoint = True
checkpoint2.append(Classes.ground(-30, 2880, 100, 120))
checkpoint2[-1].checkpoint = True
checkpoint2.append(Classes.ground(900, 3680, 100, 120))
checkpoint2[-1].checkpoint = True

#murs
walls2.append(Classes.ground(-250, 500, 500, 50))
walls2.append(Classes.ground(-500, 700, 300, 50))
walls2.append(Classes.ground(200, 700, 300, 50))
walls2.append(Classes.ground(-250, 900, 500, 50))
walls2.append(Classes.ground(-500, 1100, 200, 50))
walls2.append(Classes.ground(300, 1100, 200, 50))
walls2.append(Classes.ground(-250, 1300, 500, 50))
walls2.append(Classes.ground(-250, 1500, 500, 50))
walls2.append(Classes.ground(-500, 1750, 400, 50))
walls2.append(Classes.ground(100, 1750, 400, 50))
walls2.append(Classes.ground(-250, 2000, 500, 50))
walls2.append(Classes.ground(-500, 2250, 400, 50))
walls2.append(Classes.ground(100, 2250, 400, 50))
walls2.append(Classes.ground(-200, 2500, 400, 50))
walls2.append(Classes.ground(-500, 2750, 400, 50))
walls2.append(Classes.ground(100, 2750, 400, 50))
walls2.append(Classes.ground(-400, 3000, 900, 50))
walls2.append(Classes.ground(-500, 3250, 900, 50))
walls2.append(Classes.ground(-400, 3500, 900, 50))

#plateformes
walls2.append(Classes.ground(-500, 200, 1000, 10))
walls2.append(Classes.ground(-500, 300, 1000, 10))
walls2.append(Classes.ground(-500, 400, 1000, 10))
walls2.append(Classes.ground(-500, 500, 1000, 10))
walls2.append(Classes.ground(-500, 700, 1000, 10))
walls2.append(Classes.ground(-500, 900, 1000, 10))
walls2.append(Classes.ground(-500, 1100, 1000, 10))
walls2.append(Classes.ground(-500, 1300, 1000, 10))
walls2.append(Classes.ground(-500, 1500, 1000, 10))
walls2.append(Classes.ground(-500, 1750, 1000, 10))
walls2.append(Classes.ground(-500, 2000, 1000, 10))
walls2.append(Classes.ground(-500, 2250, 1000, 10))
walls2.append(Classes.ground(-500, 2500, 1000, 10))
walls2.append(Classes.ground(-500, 2750, 1000, 10))
walls2.append(Classes.ground(-500, 3000, 1000, 10))
walls2.append(Classes.ground(-500, 3250, 1000, 10))
walls2.append(Classes.ground(-500, 3500, 1000, 10))

###monstres
#au fond de la fosse
monsters2.append(Classes.monster(1500, 4550, 2410, 1500, "right"))
monsters2.append(Classes.monster(1750, 4550, 2410, 1500, "right"))
monsters2.append(Classes.monster(2000, 4550, 2410, 1500, "right"))
monsters2.append(Classes.monster(2250, 4550, 2410, 1500, "right"))
monsters2.append(Classes.monster(2500, 4550, 2410, 1500))
monsters2.append(Classes.monster(2250, 4550, 2410, 1500))
monsters2.append(Classes.monster(2000, 4550, 2410, 1500))
monsters2.append(Classes.monster(1750, 4550, 2410, 1500))

#premier checkpoint
monsters2.append(Classes.monster(-500, 250, 410, -500, "right"))
monsters2.append(Classes.monster(-45, 250, 410, -500, "right"))
monsters2.append(Classes.monster(410, 250, 410, -500))
monsters2.append(Classes.monster(-45, 250, 410, -500))

monsters2.append(Classes.monster(205, 350, 410, -500, "right"))
monsters2.append(Classes.monster(-295, 350, 410, -500))

monsters2.append(Classes.monster(-500, 450, 410, -500, "right"))
monsters2.append(Classes.monster(-45, 450, 410, -500, "right"))
monsters2.append(Classes.monster(410, 450, 410, -500))
monsters2.append(Classes.monster(-45, 450, 410, -500))

monsters2.append(Classes.monster(-45, 650, 410, -500))

monsters2.append(Classes.monster(205, 850, 410, -500, "right"))
monsters2.append(Classes.monster(-295, 850, 410, -500))

monsters2.append(Classes.monster(-500, 1050, 410, -500, "right"))

monsters2.append(Classes.monster(205, 1250, 410, -500, "right"))
monsters2.append(Classes.monster(-295, 1250, 410, -500))

monsters2.append(Classes.monster(195, 650, 1160, 750, "up", 2))
monsters2[-1].speed = 3.6
monsters2.append(Classes.monster(-305, 650, 1160, 750, "up", 2))
monsters2[-1].speed = 3.6
#deuxième checkpoint
monsters2.append(Classes.monster(365, 2300, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(-475, 2300, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(365, 1500, 2370, 1500, "down", 2))
monsters2.append(Classes.monster(-475, 1500, 2370, 1500, "down", 2))
monsters2.append(Classes.monster(215, 2150, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(-325, 2150, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(215, 2000, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(-325, 2000, 2370, 1500, "up", 2))
monsters2.append(Classes.monster(65, 1750, 2370, 1500, "down", 2))
monsters2.append(Classes.monster(-175, 1750, 2370, 1500, "down", 2))
monsters2.append(Classes.monster(350, 2600, 350, -500, "left", 2))
monsters2.append(Classes.monster(-500, 2600, 350, -500, "right", 2))
#troisième checkpoint
monsters2.append(Classes.monster(-275, 3200, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(-275, 3200, 410, -500))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3200, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3200, 410, -500))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(-275, 3450, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(-275, 3450, 410, -500))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3450, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3450, 410, -500))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3750, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(185, 3750, 410, -500))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(-275, 3750, 410, -500, "right"))
monsters2[-1].speed = 5
monsters2.append(Classes.monster(-275, 3750, 410, -500))
monsters2[-1].speed = 5
#pièges
traps2.append(Classes.spike(-200, 680))
traps2.append(Classes.spike(200, 680))

#boss 2

#mur invisible
walls2.append(Classes.ground(1500, 3900,1000, 500))
walls2[-1].invisible = 1
#plateformes
walls2.append(Classes.ground(1500, 3800, 500, 20))
walls2.append(Classes.ground(1800, 3650, 400, 10))
walls2.append(Classes.ground(1650, 3500, 200, 10))
walls2.append(Classes.ground(2150, 3500, 200, 10))
walls2.append(Classes.ground(1500, 3350, 200, 10))
walls2.append(Classes.ground(2300, 3350, 200, 10))
walls2.append(Classes.ground(2150, 3200, 200, 10))
walls2.append(Classes.ground(1650, 3200, 200, 10))
walls2.append(Classes.ground(1800, 3050, 400, 10))
walls2.append(Classes.ground(1900, 2900, 200, 10))
walls2.append(Classes.ground(2200, 2750, 200, 10))
walls2.append(Classes.ground(1600, 2600, 500, 10))
walls2.append(Classes.ground(1500, 2450, 100, 10))
walls2.append(Classes.ground(1700, 2300, 100, 10))
walls2.append(Classes.ground(1800, 2150, 700, 10))
walls2.append(Classes.ground(2400, 2000, 100, 10))
walls2.append(Classes.ground(2300, 1850, 100, 10))
walls2.append(Classes.ground(1600, 1700, 700, 10))
walls2.append(Classes.ground(1500, 1550, 100, 10))
walls2.append(Classes.ground(1800, 1550, 100, 10))
walls2.append(Classes.ground(1500, 1400, 100, 10))
walls2.append(Classes.ground(1700, 1250, 700, 10))
walls2.append(Classes.ground(1980, 1100, 100, 10))
walls2.append(Classes.ground(2200, 1100, 100, 10))
walls2.append(Classes.ground(2400, 950, 100, 10))
walls2.append(Classes.ground(2100, 800, 100, 10))
walls2.append(Classes.ground(1800, 650, 100, 10))
walls2.append(Classes.ground(1500, 500, 100, 10))
walls2.append(Classes.ground(1500, 350, 100, 10))
walls2.append(Classes.ground(1750, 200, 100, 10))
walls2.append(Classes.ground(2000, 50, 100, 10))
walls2.append(Classes.ground(2250, -100, 100, 10))
walls2.append(Classes.ground(2250, -250, 100, 10))
walls2.append(Classes.ground(2250, -400, 100, 20))
walls2.append(Classes.ground(2250, -550, 100, 20))
walls2.append(Classes.ground(2200, -700, 300, 10))
walls2.append(Classes.ground(1950, -500, 200, 10))
walls2.append(Classes.ground(2000, -590, 20, 90))#pillier
walls2.append(Classes.ground(2100, -840, 400, 20))
walls2.append(Classes.ground(1700, -1000, 600, 10))
walls2.append(Classes.ground(1700, -1150, 600, 10))
walls2.append(Classes.ground(1700, -1300, 600, 10))
walls2.append(Classes.ground(1700, -1450, 600, 10))
walls2.append(Classes.ground(1700, -1600, 600, 10))
walls2.append(Classes.ground(1700, -1750, 600, 10))
walls2.append(Classes.ground(1700, -1900, 600, 10))
walls2.append(Classes.ground(1700, -2050, 600, 10))
walls2.append(Classes.ground(1700, -2200, 600, 10))
walls2.append(Classes.ground(1700, -2350, 600, 10))
walls2.append(Classes.ground(1700, -2500, 600, 10))
walls2.append(Classes.ground(1700, -2650, 600, 10))
walls2.append(Classes.ground(2100, -2800, 200, 10))

walls2.append(Classes.ground(1000, -2800, 1100, 80))
walls2.append(Classes.ground(2300, -2800, 400, 80))

#entreniveau
walls2.append(Classes.ground(3000, -2800, 750, 1000))
walls2.append(Classes.ground(3750, -2780, 250, 1000))
walls2.append(Classes.ground(3750, -2800, 250, 20))
walls2.append(Classes.ground(3700, -4800, 50, 1800))
walls2.append(Classes.ground(4000, -4800, 50, 3000))


#mur supprimé
walls2.append(Classes.ground(1500, 2200, 1000, 1000))



walls3 = []
traps3 = []
monsters3 = []
checkpoint3 = []
objects3 = []
messages3 = []


#!/usr/bin/env python3
# coding:utf8


#################### INITIATIONS ET IMPORTATIONS ########################

import pygame
pygame.init()
import math
from random import randrange
from pygame.locals import *
import Classes 
import leveldesign 

#################### VARIABLES ###########################



bearer = Classes.character() 
run = True
WINDOWWIDTH = 1400
WINDOWHEIGHT = 1000
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), DOUBLEBUF)
pygame.display.set_caption("CANDLE")
player_x = 700
player_y = 400
level = 1
menu = 1
#bearer.x = -5000
#bearer.y = -1200
#bearer.x = 0
#bearer.y = -1200
#bearer.x = 12000
#bearer.y = 100
#bearer.x = 61000
#bearer.y =  4000
#danger[0].x = 10000
#danger[0].x = 9500
#danger[0].alive = True
#bearer.cinematic = 10
buttons = []
buttons.append(Classes.buttons(WINDOWWIDTH - 80, 10))
buttons.append(Classes.buttons(buttons[0].backx + 50, buttons[0].backy + 50, 1, 50, 50, "QWERTY"))
buttons.append(Classes.buttons(buttons[0].backx + 50, buttons[0].backy + 100, 1, 50, 50, "AZERTY"))
buttons[-1].Activated = True
buttons.append(Classes.buttons(buttons[0].backx + 50, buttons[0].backy + 150, 1, 50, 50, "Directional keys"))
buttons.append(Classes.buttons(buttons[0].backx + 50, buttons[0].backy + 250, 1, 50, 50, "Easy mode"))
lasers = []
messages = []
walls = []
danger = []
traps = []
checkpoints = []
minions1 = []
objects = []
memory = 0
if level == 1:
	bearer.lifemax = 3
	danger.append(Classes.Boss1())
	for i in leveldesign.messages:
		messages.append(i)
	for i in leveldesign.monsters:
			danger.append(i)
	for i in leveldesign.walls:
			walls.append(i)
	for i in leveldesign.traps:
			traps.append(i)
	for i in leveldesign.checkpoint:
			checkpoints.append(i)
	for i in leveldesign.objects1:
			objects.append(i)
	minions1.append(Classes.MinionBoss(-1000, 740))
	minions1.append(Classes.MinionBoss(-1000, 540))
	minions1.append(Classes.MinionBoss(-1000, 340))
	for i in range(len(minions1)):
	        minions1[i].x = 9500
	        minions1[i].x = 10000
elif level == 2:
	bearer.lifemax = 2
	bearer.x = 0
	bearer.y = -2000
	danger.append(Classes.Boss2())
	for i in leveldesign.messages2:
		messages.append(i)
	for i in leveldesign.monsters2:
			danger.append(i)
	for i in leveldesign.walls2:
			walls.append(i)
	for i in leveldesign.traps2:
			traps.append(i)
	for i in leveldesign.checkpoint2:
			checkpoints.append(i)
	for i in leveldesign.objects2:
			objects.append(i)
################## FONCTIONS #######################

def LaserUp(time, boss, minion, X, lasers):
	if boss.timer > time-0.5 and boss.timer < time:
			minion.initialX = X
			minion.laser = 0
			if minion.initialX <= minion.x + 5 and minion.initialX >= minion.x - 5:
					minion.x = minion.initialX
			elif minion.initialX > minion.x:
					minion.x += 9
			elif minion.initialX < minion.x:
					minion.x -= 9
	elif boss.timer >= time and boss.timer <= time + 0.1 and minion.laser == 0:
			minion.x = minion.initialX
			lasers.append(Classes.laser(minion.x+ minion.width//2, minion.y - 3000, "up"))
			lasers[-1].durationmax = 2000
			minion.laser = 1
	return(lasers)

def LaserRight(location, boss, minion, Y, lasers, bearer):
	if bearer.x > location and bearer.x < location + 300:
			minion.initialY = Y
			minion.laser = 0
			if minion.initialY <= minion.y + 5 and minion.initialY >= minion.y - 5:
					minion.y = minion.initialY
			elif minion.initialY > minion.y:
					minion.y += 2
			elif minion.initialY < minion.y:
					minion.y -= 2
	elif bearer.x >= location + 300 and bearer.x <= location + 305 and minion.laser == 0:
			boss.laser += 1
			minion.y = minion.initialY
			lasers.append(Classes.laser(minion.x+ minion.width, minion.y + minion.height//2, "right"))
			lasers[-1].durationmax = 2800
			minion.laser = 1
	return(lasers)

def redrawGameWindow(window, x, y, bearer):
		window.fill((15,15,15))
		for wall in walls :
				wall.Draw(window, bearer.x - x, bearer.y -  y, bearer)
		for i in checkpoints:
				i.Draw(window, bearer.x-x, bearer.y-y, bearer)
		for i in traps:
				i.Draw(window, bearer.x - x, bearer.y - y, bearer)
		for i in objects:
				i.Draw(window, bearer.x - x, bearer.y - y, bearer)
		bearer.Draw(window, player_x, player_y)
		for i in danger:
				i.Draw(window, bearer.x - x, bearer.y -  y, bearer)
		for minion in minions1:
				minion.Draw(window, bearer.x-x, bearer.y-y, bearer)
		for laser in lasers:
				laser.Draw(window, bearer.x-x, bearer.y-y, bearer)
		for message in messages:
				message.Draw(window, bearer.x-x, bearer.y-y, bearer)
		for i in buttons:       
				i.Draw(window)
		bearer.Drawlife(window)
		
		pygame.display.update()
		
		
		
def redrawPauseWindow(window):
		for i in buttons:
				i.DrawBack(window)
				i.Draw(window)
				i.DrawPause(window)
		pygame.display.update()
		
def redrawMenuWindow(window):
	window.fill((30,30,30))
	font = pygame.font.SysFont("comicsans", 100, True)
	text = font.render("CANDLE", 1 , (255, 255, 255))
	window.blit(text, (300, 200))
	font = pygame.font.SysFont("comicsans", 20, True)
	text = font.render("press ESCAPE to start", 1 , (255, 255, 255))
	window.blit(text, (300, 330))
	pygame.display.update()
		

#################### BOUCLE ############################

while run:
		pygame.time.delay(10)
		if menu == 1:
			for event in pygame.event.get():
				redrawMenuWindow(window)
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT: 
						run = False
				if keys[pygame.K_ESCAPE]:
					menu = 0
		elif menu == 0:
			for event in pygame.event.get():
				###Boutons
					if event.type == pygame.MOUSEBUTTONUP:
						for i in range(len(buttons)):
							if pygame.mouse.get_pos()[0] <= buttons[i].x + buttons[i].width and pygame.mouse.get_pos()[0] >= buttons[i].x and pygame.mouse.get_pos()[1] <= buttons[i].y + buttons[i].height and pygame.mouse.get_pos()[1] >= buttons[i].y :
								if event.type == pygame.MOUSEBUTTONUP:
											if i == 0:
												buttons[i].clicked = True
												buttons[i].Activate()
											if buttons[0].Activated == True:
												if i > 0 and i < 4:
													if buttons[i].Activated == False:
															for j in range(1, 4):
																buttons[j].Activated = False
															buttons[i].clicked = True
															buttons[i].down = False
															buttons[i].Activate()
													else:
															buttons[i].clicked = True
															buttons[i].down = False
															buttons[i].Activate()
												if i == 4:
													if buttons[i].Activated == False:
															buttons[i].clicked = True
															buttons[i].down = False
															bearer.lifebonus = 2
															buttons[i].Activate()
													else:
															buttons[i].clicked = True
															buttons[i].down = False
															bearer.lifebonus = 0
															if bearer.life >= bearer.lifemax + bearer.lifebonus:
																bearer.life = bearer.lifemax + bearer.lifebonus
															buttons[i].Activate()
								if event.type == pygame.MOUSEBUTTONDOWN:
									buttons[i].down = True
									
					keys = pygame.key.get_pressed()
					if event.type == pygame.QUIT: 
							run = False
					if keys[pygame.K_ESCAPE]:
							buttons[0].clicked = True
							buttons[0].Activate()
			
			bearer.fasterfall = 0		
			if buttons[0].Activated == True:
					redrawPauseWindow(window)
			elif buttons[0].Activated == False:
					if buttons[1].Activated == True:
							if keys[pygame.K_a]:
									bearer.movement_left(walls)
							if keys[pygame.K_d]:
									bearer.movement_right(walls)
							if keys[pygame.K_s]:
									bearer.movement_down(walls)
							if keys[pygame.K_w]:
									bearer.movement_up(walls)
					if buttons[2].Activated == True:
							if keys[pygame.K_q]:
									bearer.movement_left(walls)
							if keys[pygame.K_d]:
									bearer.movement_right(walls)
							if keys[pygame.K_s]:
									bearer.movement_down(walls)
							if keys[pygame.K_z]:
									bearer.movement_up(walls)
					if buttons[3].Activated == True:
							if keys[pygame.K_LEFT]:
									bearer.movement_left(walls)
							if keys[pygame.K_RIGHT]:
									bearer.movement_right(walls)
							if keys[pygame.K_DOWN]:
									bearer.movement_down(walls)
							if keys[pygame.K_UP]:
									bearer.movement_up(walls)
					for i in checkpoints:
						if bearer.x < i.x + i.width and bearer.x + bearer.width > i.x -5:
							if bearer.y + bearer.height > i. y +5 and bearer.y < i.y + i.height -5:
								bearer.life = bearer.lifemax + bearer.lifebonus
					# fonction de chute et de saut
					bearer.Jump(walls, WINDOWHEIGHT, player_x, player_y)
					bearer.Fall(walls, WINDOWHEIGHT, player_x, player_y)
					#réinitialisation du jeu à la mort du joueur
					if bearer.life <= 0:
							bearer.standing = False
							i = len(checkpoints)-1
							while checkpoints[i].light == False:
									i -= 1
							bearer.x = checkpoints[i].x
							bearer.y = checkpoints[i].y
							bearer.fallingspeed = 2
							bearer.life = bearer.lifemax
							if level == 1:
									messages = []
									danger = []
									if bearer.boss < 1:
										danger.append(Classes.Boss1())
									for i in leveldesign.monsters:
											danger.append(i)
									walls = []
									for i in leveldesign.walls:
											walls.append(i)
									traps = []
									for i in leveldesign.traps:
											traps.append(i)
									checkpoints = []
									for i in leveldesign.checkpoint:
											checkpoints.append(i)
									objects = []
									for i in leveldesign.objects1:
											objects.append(i)
									for i in leveldesign.messages:
										messages.append(i)
									minions1 = []
									minions1.append(Classes.MinionBoss(-1000, 740))
									minions1.append(Classes.MinionBoss(-1000, 540))
									minions1.append(Classes.MinionBoss(-1000, 340))
							elif level == 2:
									messages = []
									minions1 = []
									danger = []
									if bearer.boss < 2:
										danger.append(Classes.Boss2())
									for i in leveldesign.messages2:
										messages.append(i)
									for i in leveldesign.monsters2:
											danger.append(i)
									walls = []
									for i in leveldesign.walls2:
											walls.append(i)
									traps = []
									for i in leveldesign.traps2:
											traps.append(i)
									checkpoints = []
									for i in leveldesign.checkpoint2:
											checkpoints.append(i)
									objects = []
									for i in leveldesign.objects2:
											objects.append(i)
					else :
							if bearer.knockback < 100 :
									if danger[0].timer > 0 and level == 1 and bearer.knockback == 0 and bearer.lifebonus == 2:
										danger[0].speed -= 0.2
									bearer.knockback += 1
							else:
									for i in range(len(danger)):
											if danger[i].exist == True and danger[i].alive == True:
												if danger[i] == danger[0]:
													bearer.oneshot(danger[i])
												if i == 49 or i == 50 or i == 51 or i == 52 or i == 53:
													if danger[0].x + danger[0].width > danger[i].x + danger[i].width and danger[0].alive == True:
														danger[i].exist = False
												else:
													bearer.hit(danger[i])
									for i in range(len(lasers)):
											if lasers[i].exist == True and lasers[i].duration > 1000:
													bearer.hit(lasers[i])
									for i in range(len(traps)):
											bearer.hit(traps[i])
					#pièges
					#ennemis
					for i in range(1,len(danger)):
							if danger[i].alive and danger[i].exist and danger[i].xmax:
									danger[i].movement()
					#boss1
					if level == 1:
							if danger[0].exist == True and bearer.y + bearer.height == 900 and bearer.x >= -220 and bearer.x <= 160:
									bearer.Cinematic2(window)
									if danger[0].cinematic == 0 and danger[0].alive == False:
											if keys[pygame.K_e]:
													bearer.cinematic = 2
													danger[0].cinematic = 1
													del walls[-1]
													del walls[55]
													messages[-1].exist = False
													bearer.Cinematic2(window)
							if danger[0].alive == True:
									danger[0].movement(bearer)
							if danger[0].x + 2500 < bearer.x:
									danger[0].speed = 4.5
							#### PHASE DES LASERS ####
							#aides du boss1
							for i in range(len(minions1)):
									if minions1[i].alive == True:
											if bearer.x <= 14600:
													minions1[i].movement(danger[0])
											elif bearer.x > 15000:
													if minions1[i].laser > 0:
															minions1[i].movement(danger[0])
													elif minions1[i].laser == 0 and bearer.x < 15500:
															pass
													else:
															minions1[i].alive = False
															minions1[i].exist = False
											if bearer.x < 12500:
												#invocations
												if bearer.x > 610 and bearer.x < 620 and danger[-1].xmax != 2000:
													danger.append(Classes.monster(1850, 850, 2000, 0))
												if bearer.x > 650 and bearer.x < 660 and danger[-1].xmax != 2050:
													danger.append(Classes.monster(2040, 850, 2050, 0))
												if bearer.x > 720 and bearer.x < 730 and danger[-1].xmax != 2300:
													danger.append(Classes.monster(2300, 700, 2300, 1400))
												#premier laser
												if bearer.x > 1700 and i == 1 and danger[0].laser <= 0:
													LaserRight(1700, danger[0], minions1[i], 640, lasers, bearer)
												#deuxième laser
												if bearer.x > 2150 and i == 1 and danger[0].laser <= 1:
													LaserRight(2150, danger[0], minions1[i], 500, lasers, bearer)
												#troisième laser
												if bearer.x > 2900 and i == 1 and danger[0].laser <= 2:
													LaserRight(2900, danger[0], minions1[i], 500, lasers, bearer)
												#4ème monstre
												if bearer.x > 4060 and bearer.x < 4070 and danger[-1].xmax != 4900:
													danger.append(Classes.monster(4900, 570, 4900, 4500))
												#5ème monstre
												if bearer.x > 4100 and bearer.x < 4110 and danger[-1].xmax != 6700:
													danger.append(Classes.monster(6800, 500, 6700, 6000))
												#quatrième laser
												if bearer.x > 7050 and i == 0 and danger[0].laser <= 5:
													LaserRight(7050, danger[0], minions1[i], 780, lasers, bearer)
												if bearer.x > 7050 and i == 1 and danger[0].laser <= 5:
													LaserRight(7050, danger[0], minions1[i], 540, lasers, bearer)
												if bearer.x > 7050 and i == 2 and danger[0].laser <= 5:
													LaserRight(7050, danger[0], minions1[i], 340, lasers, bearer)
												#cinquième laser
												if bearer.x > 8580 and i == 1 and danger[0].laser <= 7:
													LaserRight(8590, danger[0], minions1[i], 540, lasers, bearer)
												if bearer.x > 8580 and i == 2 and danger[0].laser <= 7:
													LaserRight(8590, danger[0], minions1[i], 340, lasers, bearer)
												#sixième laser
												if bearer.x > 9180 and i == 0 and danger[0].laser <= 9:
													LaserRight(9180, danger[0], minions1[i], 780, lasers, bearer)
												if bearer.x > 9180 and i == 2 and danger[0].laser <= 9:
													LaserRight(9180, danger[0], minions1[i], 340, lasers, bearer)
												#septième laser
												if bearer.x > 10030 and i == 1 and danger[0].laser <= 10:
													LaserRight(10030, danger[0], minions1[i], 540, lasers, bearer)
												#huitième laser
												if bearer.x > 10850 and i == 0 and danger[0].laser <= 12:
													LaserRight(10850, danger[0], minions1[i], 780, lasers, bearer)
												if bearer.x > 10850 and i == 1 and danger[0].laser <= 12:
													LaserRight(10850, danger[0], minions1[i], 540, lasers, bearer)
												#neuvième laser
												if bearer.x > 11350 and i == 2 and danger[0].laser <= 14:
													LaserRight(11350, danger[0], minions1[i], 340, lasers, bearer)
												#dixième laser
												if bearer.x > 11880 and i == 0 and bearer.x < 12185 and danger[0].laser <= 15:
													LaserRight(11880, danger[0], minions1[i], 780, lasers, bearer)
												if bearer.x > 11880 and i == 2 and bearer.x < 12185 and danger[0].laser <= 15:
													LaserRight(11880, danger[0], minions1[i], 340, lasers, bearer)
											#positionnement de la phase finale de lasers
											if bearer.x > 12185 and bearer.x < 12500:
													minions1[i].laser = 0
													minions1[0].initialY = 740
													minions1[1].initialY = 540
													minions1[2].initialY = 340
													if danger[0].speed < 4:
															danger[0].speed = 4.1
													if minions1[i].initialY == minions1[i].y + 1 or minions1[i].initialY == minions1[i].y - 1:
															minions1[i].y = minions1[i].initialY
													elif minions1[i].initialY > minions1[i].y:
															minions1[i].y += 2
													elif minions1[i].initialY < minions1[i].y:
															minions1[i].y -= 2
											#onzième laser
											if bearer.x >= 12600 and bearer.x < 12605 and minions1[i].laser == 0:
													if minions1[i].initialY == 740 :
															indice1 = len(lasers)
															lasers.append(Classes.laser(minions1[i].x+ minions1[i].width, minions1[i].y + 55, "right"))
															minions1[i].laser = 1
											if minions1[i].initialY == 740 and bearer.x > 12650 and minions1[i].y > 540 and lasers[indice1].duration >= 1000 and bearer.x <= 14000:
													minions1[i].y -= 4
											if minions1[i].initialY == 740 and bearer.x > 12650 and lasers[indice1].exist == True and lasers[indice1].duration >= 1000:
													lasers[indice1].y = minions1[i].y + 55 - lasers[indice1].height//2
											#douzième laser
											if bearer.x >= 13150 and bearer.x < 13154 and minions1[i].laser == 0:
													if minions1[i].initialY == 340 :
															indice3 = len(lasers)
															lasers.append(Classes.laser(minions1[i].x+ minions1[i].width, minions1[i].y + 55, "right"))
															minions1[i].laser = 1
											if minions1[i].initialY == 340 and bearer.x >= 13150 and minions1[i].y < 540 and lasers[indice3].duration >= 1000 and bearer.x <= 14000:
													minions1[i].y += 4
											if minions1[i].initialY == 340 and bearer.x >= 13150 and lasers[indice3].exist == True and lasers[indice3].duration >= 1000:
													lasers[indice3].y = minions1[i].y + 55 - lasers[indice3].height//2
											#treizième laser
											if bearer.x >= 13250 and bearer.x < 13254 and minions1[i].laser == 0:
													if minions1[i].initialY == 540 :
															indice2 = len(lasers)
															lasers.append(Classes.laser(minions1[i].x+ minions1[i].width, minions1[i].y + 55, "right"))
															minions1[i].laser = 1
											if minions1[i].initialY == 540 and bearer.x >= 13250 and minions1[i].y > 340 and lasers[indice2].duration >= 1000:
													minions1[i].y -= 4
											if minions1[i].initialY == 540 and bearer.x >= 13250 and minions1[i].y > 340 and lasers[indice2].exist == True:
													lasers[indice2].y = minions1[i].y + 55 - lasers[indice2].height//2
											#préparation au dernier laser
											if minions1[i].y > 550 and bearer.x >= 13350 and minions1[i].laser <= 1000:
												minions1[i].y -= 6
											elif minions1[i].y < 530 and bearer.x >= 13350 and minions1[i].laser <= 1000:
												minions1[i].y += 6
											elif minions1[i].y > 530 and minions1[i].y < 550 and bearer.x >= 13350 and minions1[i].laser <= 1000:
												minions1[i].y = 540
											#quatorzième laser
											if bearer.x >= 14100 and bearer.x < 14104 and minions1[i].laser == 0:
													indice4 = len(lasers) -1
													indice5 = len(lasers)
													lasers.append(Classes.laser(minions1[i].x+ minions1[i].width, minions1[i].y + 55, "right"))
													minions1[i].laser = 1
											if minions1[i].initialY == 340 and bearer.x >= 14200 and lasers[indice4].exist == True and minions1[i].y > 340:
													lasers[indice4].y = minions1[i].y + 55 - lasers[indice4].height//2
													minions1[i].y -= 4
											if minions1[i].initialY == 740 and bearer.x >= 14200 and lasers[indice5].exist == True and minions1[i].y < 740:
													lasers[indice5].y = minions1[i].y + 55 - lasers[indice5].height//2
													minions1[i].y += 4
											if danger[0].timer > 0 and danger[0].alive == False:
												bearer.boss = 1

											
													
									else:
											if danger[0].alive == True:
													minions1[i].alive = True
							for i in range(len(lasers)):
									if lasers[i].exist:
											lasers[i].fire(danger[0].speed)
					#boss2
					if level == 2:
							if danger[0].exist == True and bearer.y + bearer.height == 3800 and bearer.x >= 1900 and bearer.x <= 2000:
									bearer.Cinematic3(window)
									if danger[0].alive == False and danger[0].cinematic == 0:
											if keys[pygame.K_e]:
													bearer.cinematic = 3
													danger[0].cinematic = 1
													del walls[-1]
													del walls[43]
													messages[-1].exist = False
													danger.append(Classes.monster(3700, 3700, 4750, 0, "left", 2))
													danger.append(Classes.monster(3850, 3550, 4750, 0, "left", 2))
													danger.append(Classes.monster(4000, 3400, 4750, 0, "left", 2))
													danger.append(Classes.monster(4150, 3250, 4750, 0, "left", 2))
													danger.append(Classes.monster(4300, 3100, 4750, 0, "left", 2))
													danger.append(Classes.monster(4450, 2950, 4750, 0, "left", 2))
													
													danger.append(Classes.monster(190, 3700, 4750, -600, "right", 2))
													danger.append(Classes.monster(40, 3550, 4750, -600, "right", 2))
													danger.append(Classes.monster(-110, 3400, 4750, -600, "right", 2))
													danger.append(Classes.monster(-260, 3250, 4750, -600, "right", 2))
													danger.append(Classes.monster(-410, 3100, 4750, -600, "right", 2))
													danger.append(Classes.monster(-560, 2950, 4750, -600, "right", 2))
													bearer.Cinematic3(window)
													
							if danger[0].alive == True:
									danger[0].movement(bearer)
									if danger[0].timer == 0.01:
										minions1.append(Classes.MinionBoss(3200, 2650, "left", 0,2550, 2650))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(3150, 2500, "left", 0,2550, 2500))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(3100, 2350, "left", 0,2550, 2350))
										minions1[-1].alive = True
										#followers
										minions1.append(Classes.MinionBoss(1530, 5000, "up"))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(1945, 5000, "up"))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(2355, 5000, "up"))
										minions1[-1].alive = True
							#### PHASE DES LASERS ####
							for i in range(len(minions1)):
								if minions1[i].alive == True:
									if danger[0].timer <= 30.8 :
										minions1[i].movement(danger[0])
									elif danger[0].timer > 30.8 and i >= 3 and i <= 5:
										minions1[i].y += 2
										minions1[i].speed = -1
										if minions1[i].y > - 1000:
											minions1[i].exist = False
									if i < 3:
										if minions1[i].x == minions1[i].X:
											if minions1[i].firecount == 0:
												minions1[i].firecount += 1
												lasers.append(Classes.laser(minions1[i].x-3000, minions1[i].y + 60, "left", False))
												minions1[i].laser = 1
											elif minions1[i].laser == 0:
												minions1[i].X += 1000
												minions1[i].direction = "right"
									elif i >= 3 and i < 6:
										#PREMIER LASER
										if danger[0].timer > 5.5 and danger[0].timer < 6.1 and i == 3:
											LaserUp(6, danger[0], minions1[i], 1530, lasers)
										#DEUXIÈME LASER
										if danger[0].timer > 5.5 and danger[0].timer < 6.4 and i == 4:
												minions1[i].laser = 0
												minions1[i].initialX = 1730
												if minions1[i].initialX <= minions1[i].x + 5 and minions1[i].initialX >= minions1[i].x - 5:
														minions1[i].x = minions1[i].initialX
												elif minions1[i].initialX > minions1[i].x:
														minions1[i].x += 6
												elif minions1[i].initialX < minions1[i].x:
														minions1[i].x -= 6
										elif danger[0].timer >= 6.4 and danger[0].timer <= 6.5 and minions1[i].laser == 0 and i == 4:
												minions1[i].x = minions1[i].initialX
												lasers.append(Classes.laser(minions1[i].x+ minions1[i].width//2, minions1[i].y - 3000, "up"))
												minions1[i].laser = 1
												minions1[i].initialX = 1945
										#TROISIÈME LASER
										if danger[0].timer > 5.5 and danger[0].timer < 6.8 and i == 5:
												minions1[i].laser = 0
												minions1[i].initialX = 1930
												if minions1[i].initialX <= minions1[i].x + 5 and minions1[i].initialX >= minions1[i].x - 5:
														minions1[i].x = minions1[i].initialX
												elif minions1[i].initialX > minions1[i].x:
														minions1[i].x += 6
												elif minions1[i].initialX < minions1[i].x:
														minions1[i].x -= 6
										elif danger[0].timer >= 6.8 and danger[0].timer <= 6.9 and minions1[i].laser == 0 and i == 5:
												minions1[i].x = minions1[i].initialX
												lasers.append(Classes.laser(minions1[i].x+ minions1[i].width//2, minions1[i].y - 3000, "up"))
												minions1[i].laser = 1
												minions1[i].initialX = 2355
										#QUATRIÈME LASER
										if danger[0].timer > 6.7 and danger[0].timer < 7.3 and i == 3:
											LaserUp(7.2, danger[0], minions1[i], 2130, lasers)
										if danger[0].timer >= 7.2 and danger[0].timer <= 7.3 and i == 3:
												minions1[i].initialX = 1530
										#CINQUIÈME LASER, 7ÈME ÉVÈNNEMENT
										if danger[0].timer > 10 and danger[0].timer < 11 and i != 4:
												minions1[i].laser = 0
												if minions1[i].initialX <= minions1[i].x + 5 and minions1[i].initialX >= minions1[i].x - 5:
														minions1[i].x = minions1[i].initialX
												elif minions1[i].initialX > minions1[i].x:
														minions1[i].x += 6
												elif minions1[i].initialX < minions1[i].x:
														minions1[i].x -= 6
										if danger[0].timer > 11 and danger[0].timer < 11.5 and i != 4 and  minions1[i].laser == 0:
												indice1 = len(lasers) -1
												indice2 = len(lasers)
												lasers.append(Classes.laser(minions1[i].x+ (minions1[i].width)//2, minions1[i].y-3000, "up"))
												minions1[i].laser = 1
										elif danger[0].timer > 11.5 and danger[0].timer < 12.5 and i != 4:
											if i ==3 and lasers[indice1].exist == True :
													minions1[i].x += 3
													lasers[indice1].x = minions1[i].x + 40
											if i == 5 and lasers[indice2].exist == True :
													minions1[i].x -= 3
													lasers[indice2].x = minions1[i].x + 40
										#PHASE DE LASERS, 8ÈME ÉVENNEMENT
										#premier
										if danger[0].timer > 22 and danger[0].timer < 22.6 and i == 3:
											LaserUp(22.5, danger[0], minions1[i], 1745, lasers)
										if danger[0].timer > 22 and danger[0].timer < 22.6 and i == 4:
											LaserUp(22.5, danger[0], minions1[i], 1945, lasers)
										if danger[0].timer > 22 and danger[0].timer < 22.6 and i == 5:
											LaserUp(22.5, danger[0], minions1[i], 2145, lasers)
										#deuxième
										if danger[0].timer > 23 and danger[0].timer < 23.6 and i == 3:
											LaserUp(23.5, danger[0], minions1[i], 1845, lasers)
										if danger[0].timer > 23 and danger[0].timer < 23.6 and i == 4:
											LaserUp(23.5, danger[0], minions1[i], 1945, lasers)
										if danger[0].timer > 23 and danger[0].timer < 23.6 and i == 5:
											LaserUp(23.5, danger[0], minions1[i], 2045, lasers)
										#troisième
										if danger[0].timer > 24 and danger[0].timer < 24.6 and i == 3:
											LaserUp(24.5, danger[0], minions1[i], 2045, lasers)
										if danger[0].timer > 24 and danger[0].timer < 24.6 and i == 4:
											LaserUp(24.5, danger[0], minions1[i], 2145, lasers)
										if danger[0].timer > 24 and danger[0].timer < 24.6 and i == 5:
											LaserUp(24.5, danger[0], minions1[i], 2245, lasers)
										#quatrième
										if danger[0].timer > 25 and danger[0].timer < 25.6 and i == 3:
											LaserUp(25.5, danger[0], minions1[i], 1900, lasers)
										if danger[0].timer > 25 and danger[0].timer < 25.6 and i == 4:
											LaserUp(25.5, danger[0], minions1[i], 2000, lasers)
										if danger[0].timer > 25 and danger[0].timer < 25.6 and i == 5:
											LaserUp(25.5, danger[0], minions1[i], 2100, lasers)
										#cinquième
										if danger[0].timer > 26 and danger[0].timer < 26.6 and i == 3:
											LaserUp(26.5, danger[0], minions1[i], 1700, lasers)
										if danger[0].timer > 26 and danger[0].timer < 26.6 and i == 4:
											LaserUp(26.5, danger[0], minions1[i], 1800, lasers)
										if danger[0].timer > 26 and danger[0].timer < 26.6 and i == 5:
											LaserUp(26.5, danger[0], minions1[i], 1900, lasers)
										#phase finale
										#1
										if danger[0].timer > 27 and danger[0].timer < 27.6 and i == 5:
											LaserUp(27.5, danger[0], minions1[i], 2245, lasers)
										#2
										if danger[0].timer > 27.3 and danger[0].timer < 27.9 and i == 4:
											LaserUp(27.8, danger[0], minions1[i], 2145, lasers)
										#3
										if danger[0].timer > 27.6 and danger[0].timer < 28.2 and i == 3:
											LaserUp(28.1, danger[0], minions1[i], 2045, lasers)
										#4
										if danger[0].timer > 27.9 and danger[0].timer < 28.5 and i == 5:
											LaserUp(28.4, danger[0], minions1[i], 1945, lasers)
										#5
										if danger[0].timer > 28.2 and danger[0].timer < 28.8 and i == 4:
											LaserUp(28.7, danger[0], minions1[i], 1845, lasers)
										#6
										if danger[0].timer > 28.7 and danger[0].timer < 29.3 and i == 3:
											LaserUp(29.2, danger[0], minions1[i], 1645, lasers)
										#7
										if danger[0].timer > 29 and danger[0].timer < 29.6 and i == 4:
											LaserUp(29.5, danger[0], minions1[i], 1745, lasers)
										#8
										if danger[0].timer > 29.3 and danger[0].timer < 29.9 and i == 5:
											LaserUp(29.8, danger[0], minions1[i], 1845, lasers)
										#9
										if danger[0].timer > 29.6 and danger[0].timer < 30.2 and i == 3:
											LaserUp(30.1, danger[0], minions1[i], 1945, lasers)
										#10
										if danger[0].timer > 29.9 and danger[0].timer < 30.5 and i == 4:
											LaserUp(30.4, danger[0], minions1[i], 2045, lasers)
										#11
										if danger[0].timer > 30.2 and danger[0].timer < 30.8 and i == 5:
											LaserUp(30.7, danger[0], minions1[i], 2145, lasers)
											
									#LASER DE DROITE À GAUCHE
									if danger[0].timer > 5 and danger[0].timer < 5.1 and len(minions1) == 6:
										minions1.append(Classes.MinionBoss(3200, 2050, "left", 0,2550, 2050))
										minions1[-1].alive = True
									if i == 6:
										if minions1[i].x == minions1[i].X:
											if minions1[i].firecount == 0:
												minions1[i].firecount += 1
												lasers.append(Classes.laser(minions1[i].x-3000, minions1[i].y + 60, "left", False))
												minions1[i].laser = 1
											elif minions1[i].laser == 0:
												minions1[i].X += 1000
												minions1[i].direction = "right"
									#PASSAGE DE MONSTRES DE GAUCHE À DROITE
									if danger[0].timer > 7 and danger[0].timer < 7.1 :
										if danger[-1].xmax != 4500:
											danger.append(Classes.monster(1100, 1630, 4500, 1000, "right", 2))
									if danger[0].timer > 8 and danger[0].timer < 8.1 :
										if danger[-1].xmax != 4550:
											danger.append(Classes.monster(1100, 1630, 4550, 1000, "right", 2))
									#PASSAGE DE MONSTRE DE DROITE À GAUCHE
									if danger[0].timer > 9.5 and danger[0].timer < 9.6 :
										if danger[-1].xmax != 4000:
											danger.append(Classes.monster(3000, 1000, 4000, 0, "left", 2))
									#4 LASERS DE GAUCHE À DROITE
									if danger[0].timer > 12.7 and danger[0].timer < 12.8 and len(minions1) == 7:
										minions1.append(Classes.MinionBoss(350, 250, "right", 0,1350, 250))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(200, 100, "right", 0,1350, 100))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(50, -50, "right", 0,1350, -50))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(-120, -200, "right", 0,1350, -200))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(-340, -350, "right", 0,1350, -350))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(-570, -500, "right", 0,1350, -500))
										minions1[-1].alive = True
										minions1.append(Classes.MinionBoss(-700, -650, "right", 0,1350, -750))
										minions1[-1].alive = True
											
									if i >= 7 and i <= 13:
										if minions1[i].x == minions1[i].X:
											if minions1[i].firecount == 0:
												minions1[i].firecount += 1
												lasers.append(Classes.laser(minions1[i].x+minions1[i].width, minions1[i].y + 60, "right", False))
												minions1[i].laser = 1
											elif minions1[i].laser == 0:
												minions1[i].X -= 1000
												minions1[i].direction = "left"
									if danger[0].timer > 0 and danger[0].alive == False:
										bearer.boss = 2
											
											
											
							for i in range(len(lasers)):
									if lasers[i].exist:
											lasers[i].fire(danger[0].speed)
												
					if level == 3:
						if bearer.on == 4:
							if walls[4].y > -800:
								walls[4].y -= 2
								bearer.y -= 2
								print(walls[4].y)
							else:
								walls[4].y = -800
							
					
					
					if level == 2:
						if keys[pygame.K_i]:
							bearer.x = 3000
							bearer.y = -3000
					#### PASSAGE AU DEUXIEME NIVEAU
					if bearer.y > 5000:
							bearer.x = 0
							bearer.boss = 1
							bearer.y = -2000
							level = 2
							danger = []
							objects = []
							danger.append(Classes.Boss2())
							for i in leveldesign.monsters2:
									danger.append(i)
							walls = []
							for i in leveldesign.walls2:
									walls.append(i)
							traps = []
							for i in leveldesign.traps2:
									traps.append(i)
							checkpoints = []
							for i in leveldesign.checkpoint2:
									checkpoints.append(i)
							for i in leveldesign.objects2:
									objects.append(i)
							minions1 = []
					#### PASSAGE AU TROISIÈME NIVEAU
					if bearer.on == 100 and level == 2:
						if len(walls) == 104 and bearer.x > 3750:
							walls.append(Classes.ground(3700, -3000, 50, 200))
						walls[100].y -= 2
						bearer.y -= 2
						if bearer.y <= -4000:
							walls2 = []
							for i in range(-1,-6, -1):
								walls2.append(walls[i])
								walls2[-1].x -= 3875
								walls2[-1].y += 4000
							print(walls2)
							bearer.x -= 3875
							bearer.boss = 2
							bearer.y += 4000
							level = 3
							danger = []
							objects = []
							danger.append(Classes.Boss2())
							for i in leveldesign.monsters3:
									danger.append(i)
							walls = []
							for i in walls2:
								walls.append(i)
							for i in leveldesign.walls3:
									walls.append(i)
							traps = []
							for i in leveldesign.traps3:
									traps.append(i)
							checkpoints = []
							for i in leveldesign.checkpoint3:
									checkpoints.append(i)
							for i in leveldesign.objects3:
									objects.append(i)
							minions1 = []
							


			


					redrawGameWindow(window, player_x ,player_y, bearer)

#!/usr/bin/env python3
# coding:utf8
import pygame
import random
########## PERSO PRINCIPAL

class character(object):
		flame = [pygame.image.load('sprite/bearer/flame1.png'),pygame.image.load('sprite/bearer/flame2.png'),pygame.image.load('sprite/bearer/flame3.png'),pygame.image.load('sprite/bearer/flame4.png'), pygame.image.load('sprite/bearer/flame5.png')]
		flamegone = pygame.image.load('sprite/bearer/flameGone.png')
				 
		walkRight = [pygame.image.load('sprite/bearer/bearer_move1.png'), pygame.image.load('sprite/bearer/bearer_move2.png'), pygame.image.load('sprite/bearer/bearer_move3.png'), pygame.image.load('sprite/bearer/bearer_move4.png')]

		staticRight = [pygame.image.load('sprite/bearer/bearer_static.png'), pygame.image.load('sprite/bearer/bearer_static1.png'), pygame.image.load('sprite/bearer/bearer_static2.png'), pygame.image.load('sprite/bearer/bearer_static3.png'), pygame.image.load('sprite/bearer/bearer_static4.png')]
		
		standingRight = [pygame.image.load('sprite/bearer/bearer_standing.png'), pygame.image.load('sprite/bearer/bearer_standing1.png'), pygame.image.load('sprite/bearer/bearer_standing2.png'), pygame.image.load('sprite/bearer/bearer_standing3.png'), pygame.image.load('sprite/bearer/bearer_standing4.png')]
		
		jumpRight = [pygame.image.load('sprite/bearer/bearer_jump1.png'), pygame.image.load('sprite/bearer/bearer_jump2.png'), pygame.image.load('sprite/bearer/bearer_jump3.png'), pygame.image.load('sprite/bearer/bearer_jump4.png'), pygame.image.load('sprite/bearer/bearer_jump5.png'), pygame.image.load('sprite/bearer/bearer_jump6.png')]
		
		
		fire33 = [pygame.image.load('sprite/bearer/fire133.png'), pygame.image.load('sprite/bearer/fire233.png'), pygame.image.load('sprite/bearer/fire333.png'), pygame.image.load('sprite/bearer/fire433.png')]
		fire32 = [pygame.image.load('sprite/bearer/fire132.png'), pygame.image.load('sprite/bearer/fire232.png'), pygame.image.load('sprite/bearer/fire332.png'), pygame.image.load('sprite/bearer/fire432.png')]
		fire31 = [pygame.image.load('sprite/bearer/fire131.png'), pygame.image.load('sprite/bearer/fire231.png'), pygame.image.load('sprite/bearer/fire331.png'), pygame.image.load('sprite/bearer/fire431.png')]
		fire22 = [pygame.image.load('sprite/bearer/fire122.png'), pygame.image.load('sprite/bearer/fire222.png'), pygame.image.load('sprite/bearer/fire322.png'), pygame.image.load('sprite/bearer/fire422.png')]
		fire21 = [pygame.image.load('sprite/bearer/fire121.png'), pygame.image.load('sprite/bearer/fire221.png'), pygame.image.load('sprite/bearer/fire321.png'), pygame.image.load('sprite/bearer/fire421.png')]
		fire11 = [pygame.image.load('sprite/bearer/fire111.png'), pygame.image.load('sprite/bearer/fire211.png'), pygame.image.load('sprite/bearer/fire311.png'), pygame.image.load('sprite/bearer/fire411.png')]
		
		firejump33 = [pygame.image.load('sprite/bearer/firejump133.png'), pygame.image.load('sprite/bearer/firejump233.png'), pygame.image.load('sprite/bearer/firejump333.png'), pygame.image.load('sprite/bearer/firejump433.png'), pygame.image.load('sprite/bearer/firejump533.png'), pygame.image.load('sprite/bearer/firejump633.png'), pygame.image.load('sprite/bearer/firejump733.png'), pygame.image.load('sprite/bearer/firejump833.png'), pygame.image.load('sprite/bearer/firejump933.png'), pygame.image.load('sprite/bearer/firejump1033.png')]
		firejump32 = [pygame.image.load('sprite/bearer/firejump132.png'), pygame.image.load('sprite/bearer/firejump232.png'), pygame.image.load('sprite/bearer/firejump332.png'), pygame.image.load('sprite/bearer/firejump432.png'), pygame.image.load('sprite/bearer/firejump532.png'), pygame.image.load('sprite/bearer/firejump632.png'), pygame.image.load('sprite/bearer/firejump732.png'), pygame.image.load('sprite/bearer/firejump832.png'), pygame.image.load('sprite/bearer/firejump932.png'), pygame.image.load('sprite/bearer/firejump1032.png')]
		firejump31 = [pygame.image.load('sprite/bearer/firejump131.png'), pygame.image.load('sprite/bearer/firejump231.png'), pygame.image.load('sprite/bearer/firejump331.png'), pygame.image.load('sprite/bearer/firejump431.png'), pygame.image.load('sprite/bearer/firejump531.png'), pygame.image.load('sprite/bearer/firejump631.png'), pygame.image.load('sprite/bearer/firejump731.png'), pygame.image.load('sprite/bearer/firejump831.png'), pygame.image.load('sprite/bearer/firejump931.png'), pygame.image.load('sprite/bearer/firejump1031.png')]
		firejump22 = [pygame.image.load('sprite/bearer/firejump122.png'), pygame.image.load('sprite/bearer/firejump222.png'), pygame.image.load('sprite/bearer/firejump322.png'), pygame.image.load('sprite/bearer/firejump422.png'), pygame.image.load('sprite/bearer/firejump522.png'), pygame.image.load('sprite/bearer/firejump622.png'), pygame.image.load('sprite/bearer/firejump722.png'), pygame.image.load('sprite/bearer/firejump822.png'), pygame.image.load('sprite/bearer/firejump922.png'), pygame.image.load('sprite/bearer/firejump1022.png')]
		firejump21 = [pygame.image.load('sprite/bearer/firejump121.png'), pygame.image.load('sprite/bearer/firejump221.png'), pygame.image.load('sprite/bearer/firejump321.png'), pygame.image.load('sprite/bearer/firejump421.png'), pygame.image.load('sprite/bearer/firejump521.png'), pygame.image.load('sprite/bearer/firejump621.png'), pygame.image.load('sprite/bearer/firejump721.png'), pygame.image.load('sprite/bearer/firejump821.png'), pygame.image.load('sprite/bearer/firejump921.png'), pygame.image.load('sprite/bearer/firejump1021.png')]
		firejump11 = [pygame.image.load('sprite/bearer/firejump111.png'), pygame.image.load('sprite/bearer/firejump211.png'), pygame.image.load('sprite/bearer/firejump311.png'), pygame.image.load('sprite/bearer/firejump411.png'), pygame.image.load('sprite/bearer/firejump511.png'), pygame.image.load('sprite/bearer/firejump611.png'), pygame.image.load('sprite/bearer/firejump711.png'), pygame.image.load('sprite/bearer/firejump811.png'), pygame.image.load('sprite/bearer/firejump911.png'), pygame.image.load('sprite/bearer/firejump1011.png')]
		
		CinematicOne = [pygame.image.load('sprite/bearer/cinematic1/awake1.png'), pygame.image.load('sprite/bearer/cinematic1/awake2.png'), pygame.image.load('sprite/bearer/cinematic1/awake3.png'), pygame.image.load('sprite/bearer/cinematic1/awake4.png'), pygame.image.load('sprite/bearer/cinematic1/awake5.png'), pygame.image.load('sprite/bearer/cinematic1/awake6.png'), pygame.image.load('sprite/bearer/cinematic1/awake7.png'), pygame.image.load('sprite/bearer/cinematic1/awake8.png'), pygame.image.load('sprite/bearer/cinematic1/awake9.png'),
		pygame.image.load('sprite/bearer/cinematic1/awake10.png'),pygame.image.load('sprite/bearer/cinematic1/awake11.png'),pygame.image.load('sprite/bearer/cinematic1/awake12.png'),pygame.image.load('sprite/bearer/cinematic1/awake13.png'),pygame.image.load('sprite/bearer/cinematic1/awake14.png'),pygame.image.load('sprite/bearer/cinematic1/awake15.png'),pygame.image.load('sprite/bearer/cinematic1/awake16.png'),pygame.image.load('sprite/bearer/cinematic1/awake17.png'),pygame.image.load('sprite/bearer/cinematic1/awake18.png'),pygame.image.load('sprite/bearer/cinematic1/awake19.png'),
		]
		CinematicTwo = []
		for i in range(82): #fonction pour intégrer les 82 images parce que le faire manuellement c'est trop long
				imagelist = "sprite/bearer/cinematic1/bearer_standing/sprite_",str(i),".png"
				imagestr = ''.join(imagelist)
				CinematicOne.append(pygame.image.load(imagestr))
		for i in range(24): #fonction pour intégrer les 24 images parce que le faire manuellement c'est trop long
				imagelist = "sprite/bearer/cinematic2/sprite_",str(i),".png"
				imagestr = ''.join(imagelist)
				CinematicTwo.append(pygame.image.load(imagestr))
		
		
		# on met tout à la bonne échelle
		for i in range(len(walkRight)):
				walkRight[i] = pygame.transform.scale(walkRight[i], (int(100), int(100)))
		
		for i in range(len(walkRight)):
				staticRight[i] = pygame.transform.scale(staticRight[i], (int(100), int(100)))
				
		for i in range(len(standingRight)):
				standingRight[i] = pygame.transform.scale(standingRight[i], (int(100), int(100)))
				
		for i in range(len(fire33)):
				fire33[i] = pygame.transform.scale(fire33[i], (int(100), int(100)))
		for i in range(len(fire32)):
				fire32[i] = pygame.transform.scale(fire32[i], (int(100), int(100)))
		for i in range(len(fire31)):
				fire31[i] = pygame.transform.scale(fire31[i], (int(100), int(100)))
		for i in range(len(fire22)):
				fire22[i] = pygame.transform.scale(fire22[i], (int(100), int(100)))
		for i in range(len(fire21)):
				fire21[i] = pygame.transform.scale(fire21[i], (int(100), int(100)))
		for i in range(len(fire11)):
				fire11[i] = pygame.transform.scale(fire11[i], (int(100), int(100)))
				
		for i in range(len(firejump33)):
				firejump33[i] = pygame.transform.scale(firejump33[i], (int(100), int(100)))
		for i in range(len(firejump32)):
				firejump32[i] = pygame.transform.scale(firejump32[i], (int(100), int(100)))
		for i in range(len(firejump31)):
				firejump31[i] = pygame.transform.scale(firejump31[i], (int(100), int(100)))
		for i in range(len(firejump22)):
				firejump22[i] = pygame.transform.scale(firejump22[i], (int(100), int(100)))
		for i in range(len(firejump21)):
				firejump21[i] = pygame.transform.scale(firejump21[i], (int(100), int(100)))
		for i in range(len(firejump11)):
				firejump11[i] = pygame.transform.scale(firejump11[i], (int(100), int(100)))
				
		for i in range(len(jumpRight)):
				jumpRight[i] = pygame.transform.scale(jumpRight[i], (int(100), int(100)))
		
		for i in range(len(CinematicOne)):
				CinematicOne[i] = pygame.transform.scale(CinematicOne[i], (int(100), int(100)))
		
		for i in range(len(CinematicTwo)):
				CinematicTwo[i] = pygame.transform.scale(CinematicTwo[i], (int(100), int(100)))
		
		def __init__(self):
				#hauteur de saut environ 164, en 8/0.2 = 40 frames
				#disance parcourue en un saut : environ 384 mais il a une largeur de 50 en plus
				self.x = -10990
				self.y = -2595
				self.speed = 4
				self.jumping = False
				self.moving = False
				self.falling = False
				self.standing = False
				self.canmove = True
				self.jumpspeed = 8
				self.jumpspeedmax = 8
				self.fallingspeed = 2
				self.fallingspeedmax = 20
				self.width = 50
				self.height = 77
				self.on = 0
				self.direction = "right"
				self.walkcount = 0
				self.firecount = 0
				self.cinematiccount = 0
				self.cinematic = 0
				self.life = 3
				self.lifemax = 3
				self.knockback = 100 #le nombre de frames sans se prendre de dégats
				self.firecountbis = 0
				self.decalageY = 23
				self.decalageXright = 30
				self.decalageXleft = 20
				self.lifebonus = 0
				self.fasterfall = 0
				self.boss = 0

######## FONCTION DE DESSIN
		def Drawlife(self, window):#les vies en haut à gauche
				if self.firecountbis >= 49:
						self.firecountbis = 0
				else:
						self.firecountbis += 1

				for i in range(self.life):
						window.blit(self.flame[self.firecountbis//10], ( i*100, 0))
				for i in range(self.life, (self.lifemax+self.lifebonus)):
						window.blit(self.flamegone, ( i*100, 0))

		def Draw(self, window, x, y):
				#pygame.draw.rect(window, (240, 20, 20), (x, y, self.width, self.height)) #la hitbox
				if self.firecount >= 39:
						self.firecount = 0
				else:
						self.firecount += 1

				if self.cinematic == 0:
					if self.standing == True:
							if self.height == 67:
								self.y -= 10
								self.height = 77
							self.walkcount = 0
							if self.direction == "right":
									window.blit(self.standingRight[0], ( x-27, y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(self.fire33[self.firecount//10], ( x-27, y -self.decalageY))
										elif self.life == 2:
											window.blit(self.fire32[self.firecount//10], ( x-27, y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire31[self.firecount//10], ( x-27, y -self.decalageY))
									elif self.lifemax == 2:
										if self.life >= 2:
											window.blit(self.fire22[self.firecount//10], ( x-27, y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire21[self.firecount//10], ( x-27, y -self.decalageY))
									elif self.lifemax == 1:
										window.blit(self.fire11[self.firecount//10], ( x-27, y -self.decalageY))
							elif self.direction == "left":
									window.blit(pygame.transform.flip(self.standingRight[0], True, False ), ( x-15, y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(pygame.transform.flip(self.fire33[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
										elif self.life == 2:
											window.blit(pygame.transform.flip(self.fire32[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire31[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
									elif self.lifemax == 2:
										if self.life >= 2:
											window.blit(pygame.transform.flip(self.fire22[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire21[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
									elif self.lifemax == 1:
										window.blit(pygame.transform.flip(self.fire11[self.firecount//10], True, False ), ( x-15, y -self.decalageY))
									
									
					elif self.jumping == True:
							if self.height == 67:
								self.y -= 10
								self.height = 77
							if self.direction == "right":
									if self.jumpspeed > 5:
											window.blit(self.jumpRight[0], ( x-self.decalageXright,  y -self.decalageY))
											if self.jumpspeed > 6.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[0], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[0], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[0], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[0], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[0], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
														window.blit(self.firejump11[0], ( x-self.decalageXright,  y -self.decalageY-5))
											elif self.jumpspeed > 5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[1], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[1], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[1], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[1], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[1], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[1], ( x-self.decalageXright,  y -self.decalageY-5))
									elif self.jumpspeed > 2:
											window.blit(self.jumpRight[1], ( x-self.decalageXright,  y -self.decalageY))
											if self.jumpspeed > 3.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[2], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[2], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[2], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[2], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[2], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[2], ( x-self.decalageXright,  y -self.decalageY-5))
											elif self.jumpspeed > 2:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[3], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[3], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[3], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[3], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[3], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[3], ( x-self.decalageXright,  y -self.decalageY-5))
									elif self.jumpspeed <= 2:
											window.blit(self.jumpRight[2], ( x-self.decalageXright,  y -self.decalageY))
											if self.lifemax >= 3:
												if self.life >= 3:
													window.blit(self.firejump33[4], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 2:
													window.blit(self.firejump32[4], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(self.firejump31[4], ( x-self.decalageXright,  y -self.decalageY-5))
											if self.lifemax == 2:
												if self.life >= 2:
													window.blit(self.firejump22[4], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(self.firejump21[4], ( x-self.decalageXright,  y -self.decalageY-5))
											if self.lifemax == 1:
												window.blit(self.firejump11 [4], ( x-self.decalageXright,  y -self.decalageY-5))
							elif self.direction == "left":
									if self.jumpspeed > 5:
											window.blit(pygame.transform.flip(self.jumpRight[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.jumpspeed > 6.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											elif self.jumpspeed > 5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									elif self.jumpspeed > 2:
											window.blit(pygame.transform.flip(self.jumpRight[1], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.jumpspeed > 3.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											elif self.jumpspeed > 2:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									elif self.jumpspeed <= 2:
											window.blit(pygame.transform.flip(self.jumpRight[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.lifemax >= 3:
												if self.life >= 3:
													window.blit(pygame.transform.flip(self.firejump33[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 2:
													window.blit(pygame.transform.flip(self.firejump32[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(pygame.transform.flip(self.firejump31[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											if self.lifemax == 2:
												if self.life >= 2:
													window.blit(pygame.transform.flip(self.firejump22[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(pygame.transform.flip(self.firejump21[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											if self.lifemax == 1:
												window.blit(pygame.transform.flip(self.firejump11[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									
					elif self.falling == True:
							if self.direction == "right":
									if self.fallingspeed > 3:
											if self.fasterfall == 0:
												window.blit(self.jumpRight[4], ( x-self.decalageXright,  y -self.decalageY))
											if self.fasterfall == 1:
												window.blit(self.jumpRight[5], ( x-self.decalageXright,  y -self.decalageY))
											if self.jumpspeed > 4.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[9], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[9], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[9], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[9], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[9], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[9], ( x-self.decalageXright,  y -self.decalageY-5))
											elif self.jumpspeed > 3:
												self.height = 67
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[8], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[8], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[8], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[8], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[8], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[8], ( x-self.decalageXright,  y -self.decalageY-5))
									elif self.fallingspeed > 1:
											window.blit(self.jumpRight[3], ( x-self.decalageXright,  y -self.decalageY))
											if self.jumpspeed > 2:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[7], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[7], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[7], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[7], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[7], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[7], ( x-self.decalageXright,  y -self.decalageY-5))
											elif self.jumpspeed > 1:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(self.firejump33[6], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(self.firejump32[6], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump31[6], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(self.firejump22[6], ( x-self.decalageXright,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(self.firejump21[6], ( x-self.decalageXright,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(self.firejump11[6], ( x-self.decalageXright,  y -self.decalageY-5))
									elif self.fallingspeed <= 1:
											window.blit(self.jumpRight[2], ( x-self.decalageXright,  y -self.decalageY))
											if self.lifemax >= 3:
												if self.life >= 3:
													window.blit(self.firejump33[5], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 2:
													window.blit(self.firejump32[5], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(self.firejump31[5], ( x-self.decalageXright,  y -self.decalageY-5))
											if self.lifemax == 2:
												if self.life >= 2:
													window.blit(self.firejump22[5], ( x-self.decalageXright,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(self.firejump21[5], ( x-self.decalageXright,  y -self.decalageY-5))
											if self.lifemax == 1:
												window.blit(self.firejump11[5], ( x-self.decalageXright,  y -self.decalageY-5))
							elif self.direction == "left":
									if self.fallingspeed > 3:
											if self.fasterfall == 0:
												window.blit(pygame.transform.flip(self.jumpRight[4], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.fasterfall == 1:
												window.blit(pygame.transform.flip(self.jumpRight[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.jumpspeed > 6:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[9], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											elif self.jumpspeed > 4.5:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[8], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									elif self.fallingspeed > 1:
											window.blit(pygame.transform.flip(self.jumpRight[3], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.jumpspeed > 3:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[7], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											elif self.jumpspeed > 2:
												if self.lifemax >= 3:
													if self.life >= 3:
														window.blit(pygame.transform.flip(self.firejump33[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 2:
														window.blit(pygame.transform.flip(self.firejump32[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump31[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 2:
													if self.life >= 2:
														window.blit(pygame.transform.flip(self.firejump22[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
													elif self.life == 1:
														window.blit(pygame.transform.flip(self.firejump21[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												if self.lifemax == 1:
													window.blit(pygame.transform.flip(self.firejump11[6], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									elif self.fallingspeed <= 2:
											window.blit(pygame.transform.flip(self.jumpRight[2], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
											if self.lifemax >= 3:
												if self.life >= 3:
													window.blit(pygame.transform.flip(self.firejump33[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 2:
													window.blit(pygame.transform.flip(self.firejump32[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(pygame.transform.flip(self.firejump31[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											if self.lifemax == 2:
												if self.life >= 2:
													window.blit(pygame.transform.flip(self.firejump22[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
												elif self.life == 1:
													window.blit(pygame.transform.flip(self.firejump21[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
											if self.lifemax == 1:
												window.blit(pygame.transform.flip(self.firejump11[5], True, False ), ( x-self.decalageXleft,  y -self.decalageY-5))
									
									
					elif self.moving == False:
							if self.height == 67:
								self.y -= 10
								self.height = 77
							self.walkcount = 0
							if self.direction == "right":
									window.blit(self.staticRight[0], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(self.fire33[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 2:
											window.blit(self.fire32[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire31[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax == 2:
										if self.life >= 2:
											window.blit(self.fire22[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire21[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax == 1:
										window.blit(self.fire11[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
							elif self.direction == "left":
									window.blit(pygame.transform.flip(self.staticRight[0], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(pygame.transform.flip(self.fire33[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 2:
											window.blit(pygame.transform.flip(self.fire32[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire31[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax == 2:
										if self.life >= 2:
											window.blit(pygame.transform.flip(self.fire22[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire21[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax == 1:
										window.blit(pygame.transform.flip(self.fire11[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									
					elif self.moving == True:
							if self.height == 67:
								self.y -= 10
								self.height = 77
							if self.walkcount >= 39 :
									self.walkcount = 0
							else:
									self.walkcount += 1
							if self.direction == "right":
									window.blit(self.walkRight[self.walkcount//10], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(self.fire33[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 2:
											window.blit(self.fire32[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire31[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax == 2:
										if self.life >= 2:
											window.blit(self.fire22[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
										elif self.life == 1:
											window.blit(self.fire21[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
									if self.lifemax == 1:
										window.blit(self.fire11[self.firecount//10], ( x-self.decalageXright,  y -self.decalageY))
							elif self.direction == "left":
									window.blit(pygame.transform.flip(self.walkRight[self.walkcount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax >= 3:
										if self.life >= 3:
											window.blit(pygame.transform.flip(self.fire33[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 2:
											window.blit(pygame.transform.flip(self.fire32[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire31[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax == 2:
										if self.life >= 2:
											window.blit(pygame.transform.flip(self.fire22[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
										elif self.life == 1:
											window.blit(pygame.transform.flip(self.fire21[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
									if self.lifemax == 1:
										window.blit(pygame.transform.flip(self.fire11[self.firecount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
					self.moving = False
				elif self.cinematic == 2:
					window.blit(pygame.transform.flip(self.CinematicTwo[self.cinematiccount//10], True, False ), ( x-self.decalageXleft,  y -self.decalageY))
					if self.lifemax >= 3:
						if self.life >= 3:
							window.blit(pygame.transform.flip(self.fire33[self.firecount//10], True, False ), ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 2:
							window.blit(pygame.transform.flip(self.fire32[self.firecount//10], True, False ), ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 1:
							window.blit(pygame.transform.flip(self.fire31[self.firecount//10], True, False ), ( x-self.decalageXleft, y -self.decalageY))
					elif self.lifemax == 2:
						if self.life >= 2:
							window.blit(pygame.transform.flip(self.fire22[self.firecount//10], True, False ), ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 1:
							window.blit(pygame.transform.flip(self.fire21[self.firecount//10], True, False ), ( x-self.decalageXleft, y -self.decalageY))
				elif self.cinematic == 3:
					self.x = 1940
					window.blit(self.CinematicTwo[self.cinematiccount//10], ( x-self.decalageXleft,  y -self.decalageY))
					if self.lifemax >= 3:
						if self.life >= 3:
							window.blit(self.fire33[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 2:
							window.blit(self.fire32[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 1:
							window.blit(self.fire31[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
					elif self.lifemax == 2:
						if self.life >= 2:
							window.blit(self.fire22[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
						elif self.life == 1:
							window.blit(self.fire21[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
					elif self.lifemax == 1:
						window.blit(self.fire11[self.firecount//10], ( x-self.decalageXleft, y -self.decalageY))
		
		
		def Fall(self, walls, WINDOWHEIGHT, x, y):
				wallcount = 0
				onwall = False
				while wallcount < len(walls):
						if self.falling == True: #si on tombe, on augmente la vitesse mais une seule fois par frames donc on il le fait que pour wallcount = 0
								if wallcount == 0:
										self.y += self.fallingspeed
										if self.fallingspeed < self.fallingspeedmax:
												self.fallingspeed += 0.1
										else:
												self.fallingspeed = self.fallingspeedmax
						if walls[wallcount].y >= self.y + self.height and walls[wallcount].y <= self.y + self.height + self.fallingspeed:#fonction pour s'il est sur un mur
								if walls[wallcount].x < self.x and walls[wallcount].x + walls[wallcount].width > self.x or walls[wallcount].x < self.x + self.width and walls[wallcount].x + walls[wallcount].width > self.x + self.width : #or walls[wallcount].x < self.x and walls[wallcount].x + walls[wallcount].width > self.x :
										self.y = walls[wallcount].y - self.height
										onwall = True
										self.falling = False
										self.fallingspeed = 0
										self.on = wallcount
										if walls[wallcount].width < 50:
											self.jumpspeed = 10
											self.standing = True
											self.x = walls[wallcount].x - self.width//2 + 10
										wallcount = len(walls)
								elif walls[wallcount].x > self.x and walls[wallcount].x + walls[wallcount].width < self.x + self.width:
										self.y = walls[wallcount].y - self.height
										onwall = True
										self.falling = False
										self.fallingspeed = 0
										self.jumpspeed = 10
										self.on = wallcount
										x = walls[wallcount].x -self.width//2 + walls[wallcount].width//2   
										self.standing = True
										self.x = walls[wallcount].x - self.width//2 + 10
										wallcount = len(walls)

								else:
										wallcount += 1
						else :
								wallcount += 1

								
				if onwall == False and self.jumping == False:
						self.falling = True
						
						
						
						
		def movement_left(self, walls):
				if self.canmove == True:
						self.direction = "left"
						if self.standing == False:
								self.moving = True
								wallcount = 0
								cantmove = False
								while wallcount < len(walls):
										if walls[wallcount].x + walls[wallcount].width >= self.x - self.speed and walls[wallcount].x + walls[wallcount].width <= self.x :
												if walls[wallcount].y + walls[wallcount].height > self.y :
														if walls[wallcount].y < self.y + self.height and walls[wallcount].height > 10:
																self.x = walls[wallcount].x + walls[wallcount].width
																cantmove = True
										if self.x < walls[wallcount].x + walls[wallcount].width and self.x > walls[wallcount].x or self.x + self.width < walls[wallcount].x + walls[wallcount].width and self.x + self.width > walls[wallcount].x:
												if self.y + self.height < walls[wallcount].y + walls[wallcount].height and self.y + self.height  > walls[wallcount].y:
														if walls[wallcount].height > 10:
																self.y = walls[wallcount].y - self.height
																onwall = True
																self.falling = False
																self.fallingspeed = 0
																self.on = wallcount
																wallcount = len(walls)
										wallcount += 1
								if cantmove == False:
										self.x -= self.speed

		def movement_right(self, walls):
				if self.canmove == True:
						self.direction = "right"
						if self.standing == False:
								self.moving = True
								wallcount = 0
								cantmove = False
								while wallcount < len(walls):
										if walls[wallcount].x <= self.x + self.width + self.speed and walls[wallcount].x >= self.x + self.width:
												if walls[wallcount].y + walls[wallcount].height > self.y and walls[wallcount].height > 10:
														if walls[wallcount].y < self.y + self.height:
																self.x = walls[wallcount].x - self.width
																cantmove = True
										if self.x < walls[wallcount].x + walls[wallcount].width and self.x > walls[wallcount].x or self.x + self.width < walls[wallcount].x + walls[wallcount].width and self.x + self.width > walls[wallcount].x:
												if self.y + self.height < walls[wallcount].y + walls[wallcount].height and self.y + self.height  > walls[wallcount].y:
														if walls[wallcount].height > 10:
																self.y = walls[wallcount].y - self.height
																onwall = True
																self.falling = False
																self.fallingspeed = 0
																self.on = wallcount
																wallcount = len(walls)
										wallcount += 1
								if cantmove == False:
										self.x += self.speed


		def movement_down(self, walls):
				if self.canmove == True:
						if self.falling == False :
								if walls[self.on].height <= 10:
										self.y += 2
						elif self.falling == True:
								self.fasterfall = 1
								self.fallingspeed += 0.2
								
		def movement_up(self, walls):
				if self.canmove == True:
						if self.falling == False and self.jumping == False:
								self.jumping = True
								if self.standing == True:
										self.jumpspeed = 10
								self.standing = False
						elif self.jumping == True:
								self.jumpspeed += 0.2
						
		def Jump(self, walls, WINDOWHEIGHT, x, y):
				for wallcount in range(len(walls)):
						if walls[wallcount].y + walls[wallcount].height <= self.y and walls[wallcount].y + walls[wallcount].height >= self.y - self.jumpspeed and self.x <= walls[wallcount].x + walls[wallcount].width and self.x + self.width >= walls[wallcount].x and walls[wallcount].height > 10 or self.jumpspeed <= 0:
								self.falling = True
								self.jumping = False
								self.jumpspeed = self.jumpspeedmax

				if self.jumping == True:
						self.y -= self.jumpspeed
						self.jumpspeed -= 0.4
				#return x, y
						
		def Cinematic1(self, window, x, y):
				self.cinematiccount += 1
				
				if self.cinematiccount <= 700:
						window.blit(self.CinematicOne[0], (x, y))
				
				elif self.cinematiccount < 750 and self.cinematiccount > 700:#première flamme s'allume
						window.blit(self.CinematicOne[(self.cinematiccount-700)//10], (x, y))
						
				elif self.cinematiccount < 1400 and self.cinematiccount >= 750:#première flamme brule
						if self.cinematiccount % 20 < 10:
								window.blit(self.CinematicOne[5], (x, y))
						elif self.cinematiccount % 20 < 20:
								window.blit(self.CinematicOne[6], (x, y))
								
				elif self.cinematiccount < 1460 and self.cinematiccount >= 1400:#deuxième flamme s'allume
						window.blit(self.CinematicOne[(self.cinematiccount-1350)//10], (x, y))
						
				elif self.cinematiccount < 2100 and self.cinematiccount >= 1460:#deuxième flamme brule
						if self.cinematiccount % 20 < 10:
								window.blit(self.CinematicOne[11], (x, y))
						elif self.cinematiccount % 20 < 20:
								window.blit(self.CinematicOne[12], (x, y))

				elif self.cinematiccount < 2160 and self.cinematiccount >= 2100:#troisième flamme s'allume
						window.blit(self.CinematicOne[(self.cinematiccount-1980)//10], (x, y))
						
				elif self.cinematiccount < 2700 and self.cinematiccount >= 2160:#troisième flamme brule
						if self.cinematiccount % 20 < 10:
								window.blit(self.CinematicOne[17], (x, y))
						elif self.cinematiccount % 20 < 20:
								window.blit(self.CinematicOne[18], (x, y))
				
				elif self.cinematiccount < 3520 and self.cinematiccount >= 2700: #il se lève
						window.blit(self.CinematicOne[((self.cinematiccount-2700)//10) + 18], (x, y))
				
				else:
						self.y = 210
						self.cinematic = 0
						
		def Cinematic2(self, window):
				if self.cinematic == 2:
						self.canmove = False
						self.cinematiccount += 1
						if self.cinematiccount >= 60:
							if self.lifemax == 3:
									self.lifemax = 2
									self.life = 2 + self.lifebonus
						if self.cinematiccount >= 240:
								self.cinematiccount = 0
								self.cinematic = 0
								self.canmove = True
		def Cinematic3(self, window):
				if self.cinematic == 3:
						self.canmove = False
						self.cinematiccount += 1
						if self.cinematiccount >= 60:
							if self.lifemax == 2:
									self.lifemax = 1
									self.life = 1 +self.lifebonus
						if self.cinematiccount >= 240:
								self.cinematiccount = 0
								self.cinematic = 0
								self.canmove = True
				
		def hit(self, ennemy):
				if self.x +5 < ennemy.x + ennemy.width and self.x + self.width > ennemy.x -5:
						if self.y + self.height > ennemy. y +5 and self.y < ennemy.y + ennemy.height -5:
								if self.knockback == 100:
										self.life -= 1
										self.knockback = 0
		def oneshot(self, ennemy):
				if self.x +5 < ennemy.x + ennemy.width and self.x + self.width > ennemy.x -5:
						if self.y + self.height > ennemy. y +5 and self.y < ennemy.y + ennemy.height -5:
								if self.knockback == 100:
										self.life = 0
										self.knockback = 0
								
				
				
				########## BOSS 1


class Boss1(object):
		bossCinematic = []
		bossImg = []
		pygame.display.set_mode((1800,1000))
		for i in range(4):
				imagelist = "sprite/boss1/sprite_",str(i),".png"
				imagestr = ''.join(imagelist)
				image = pygame.image.load(imagestr).convert_alpha()
				bossImg.append(image)
		for i in range(7):
				imagelist = "sprite/boss1/cinematic/sprite_",str(i),".png"
				imagestr = ''.join(imagelist)
				image = pygame.image.load(imagestr).convert_alpha()
				bossCinematic.append(image)
		
		
		# on met tout à la bonne échelle
		for i in range(len(bossImg)):
				bossImg[i] = pygame.transform.scale(bossImg[i], (int(1400), int(800)))
		for i in range(len(bossCinematic)):
				bossCinematic[i] = pygame.transform.scale(bossCinematic[i], (int(1400), int(800)))


		def __init__(self):
				self.x = -1000
				self.y = 160#hauteur de l'image = 800px
				self.speed = 3.9
				self.width = 780
				self.height = 740
				self.walkcount = 0
				self.cinematiccount = 0
				self.cinematic = 0
				self.exist = True
				self.alive = False
				self.timer = 0
				self.laser = 0
				self.tfnf = 20 #time for new frame

		######## FONCTION DE DESSIN

		def Draw(self, window, x, y, player):
				if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :#histoire d'optimiser un peu
						if self.exist == True:
								if self.cinematic == 1:
										self.cinematiccount += 1
										if self.cinematiccount <=240:
												window.blit(self.bossCinematic[0], (self.x- x,  self.y-y - 60))
										elif self.cinematiccount <= 379:
												window.blit(self.bossCinematic[(self.cinematiccount-240)//20], (self.x- x,  self.y-y - 60))
										elif self.cinematiccount >= 379:
												self.cinematic = 0
												self.alive = True
								elif self.alive == True:
										#pygame.draw.rect(window, (240, 20, 20), (self.x- x,  self.y-y, self.width, self.height)) #la hitbox
										if self.walkcount >= 79 :
												self.walkcount = 0
										else:
												self.walkcount += 1
										window.blit(self.bossImg[self.walkcount//20], (self.x- x,  self.y-y - 60))
								else:
										window.blit(self.bossCinematic[0], (self.x- x,  self.y-y - 60))
								
		def movement(self, player):
				if self.timer < 45:
					self.timer += 0.01
				if self.x + self.width >= 14600 :
						self.speed = 3
				if self.x + self.width >= 15000 :
						self.speed = 2
				if self.x + self.width >= 15400 :
						self.speed = 1
				if self.x + self.width >= 15600 :
						self.speed = 0.5
				if self.x + self.width >= 15780 :
						self.alive = False
						cinematic = 2
				elif player.x + 5< self.x + self.width :
						self.walkcount = 0
						if self.speed > 3:
								self.speed -= 0.1
				else:
						self.x += self.speed
								
								
class Boss2(object):
		bossCinematic = []
		bossImg = []
		pygame.display.set_mode((1800,1000))
		for i in range(6):
				imagelist = "sprite/boss2/sprite_",str(i),".png"
				imagestr = ''.join(imagelist)
				image = pygame.image.load(imagestr).convert_alpha()
				bossImg.append(image)
		for i in range(7):
				imagelist = "sprite/boss2/cinematic/sprite_",str(0),".png"
				imagestr = ''.join(imagelist)
				image = pygame.image.load(imagestr).convert_alpha()
				bossCinematic.append(image)
		
		# on met tout à la bonne échelle
		for i in range(len(bossImg)):
				bossImg[i] = pygame.transform.scale(bossImg[i], (int(1000), int(1100)))
		for i in range(len(bossCinematic)):
				bossCinematic[i] = pygame.transform.scale(bossCinematic[i], (int(1000), int(1100)))


		def __init__(self):
				self.x = 1500
				self.y = 3870
				self.speed = 2
				self.width = 1000
				self.height = 950
				self.walkcount = 0
				self.cinematiccount = 0
				self.cinematic = 0
				self.exist = True
				self.alive = False
				self.timer = 0
				self.tfnf = 20 #time for new frame

		######## FONCTION DE DESSIN

		def Draw(self, window, x, y, player):
				if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :#histoire d'optimiser un peu
						if self.exist == True:
								if self.cinematic == 1:
										self.cinematiccount += 1
										if self.cinematiccount <=240:
												window.blit(self.bossCinematic[0], (self.x- x,  self.y-y - 150))
										elif self.cinematiccount <= 379:
												window.blit(self.bossCinematic[(self.cinematiccount-240)//20], (self.x- x,  self.y-y - 150))
										elif self.cinematiccount >= 379:
												self.cinematic = 0
												self.alive = True
								elif self.alive == True:
										#pygame.draw.rect(window, (240, 20, 20), (self.x- x,  self.y-y, self.width, self.height)) #la hitbox
										if self.walkcount >= self.tfnf*5-1 :
												self.walkcount = 0
										else:
												self.walkcount += 1
										window.blit(self.bossImg[int(self.walkcount//self.tfnf)], (self.x- x,  self.y-y - 150))
								else:
										window.blit(self.bossCinematic[0], (self.x- x,  self.y-y - 150))
								
		def movement(self, player):
				if self.timer < 32.65 :
					self.timer += 0.01
					#if player.y + 5 > self.y :
					#		self.walkcount = 0
					#		if self.speed > 1.7:
					#				self.speed -= 0.1
					#else:
					self.y -= self.speed
				elif self.timer < 36:
					self.timer += 0.01
					self.tfnf += 0.03
				else:
					self.alive = False
								
class MinionBoss(object):
		pygame.display.set_mode((1800,1000))
		flyframeright = []
		flyframeleft = []
		flyframeup = []
		flyframedown = []
		for i in range(5):
			flyframeright.append(pygame.image.load("sprite/BossMinions/Minion1_right/sprite_"+str(i)+".png").convert_alpha())
		for i in range(5):
			flyframeleft.append(pygame.transform.flip(pygame.image.load("sprite/BossMinions/Minion1_right/sprite_"+str(i)+".png").convert_alpha(), True, False))
		for i in range(5):
			flyframeup.append(pygame.image.load("sprite/BossMinions/Minion1_up/sprite_"+str(i)+".png").convert_alpha())
		for i in range(5):
			flyframedown.append(pygame.image.load("sprite/BossMinions/Minion1_down/sprite_"+str(i)+".png").convert_alpha())

		def __init__(self,x, y, direction = "right", follow = 1,X = None,Y = None):
				self.x = x
				self.y = y 
				if X == None:
					if direction == "right" or direction == "left":
						self.y += random.randrange(-30,31)
				if Y == None:
					if direction == "up" or direction == "down":
						self.x += random.randrange(-30,31)
				self.X = X
				self.Y = Y
				self.initialY = y
				self.initialX = x
				if X == None:
					self.speed = 10
				else:
					self.speed = 3
				self.width = 110
				self.height = 110
				if direction == "right" or direction == "left":
					self.floating = "down"
				if direction == "up" or direction == "down":
					self.floating = "left"
				self.direction = direction
				self.exist = True
				self.alive = False
				self.laser = 0
				self.firecount = 0
				self.walkcount = 0
				self.follow = follow
				
		def Draw(self, window, x, y, player):
			if self.exist == True:
				#pygame.draw.rect(window, (240, 20, 20), (self.x- x,  self.y-y, self.width, self.height)) #la hitbox
				if self.walkcount == 49:
					self.walkcount = 0
				else:
					self.walkcount += 1
				if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :
						if self.exist == True:  
							if self.direction == "left":
									window.blit(self.flyframeleft[self.walkcount//10], (self.x-x-20, self.y-y-20))
							elif self.direction == "right":
									window.blit(self.flyframeright[self.walkcount//10], (self.x-x-20, self.y-y-20))
							elif self.direction == "up":
									window.blit(self.flyframeup[self.walkcount//10], (self.x-x-20, self.y-y-20))
							elif self.direction == "down":
									window.blit(self.flyframedown[self.walkcount//10], (self.x-x-20, self.y-y-20))
		
		def movement(self, boss):
			if self.exist == True:
				if self.follow == 1:
					if self.laser == 0:
							if self.y < self.initialY - 30 and self.floating == "up":
									self.floating = "down"
							elif self.y > self.initialY + 30 and self.floating == "down":
									self.floating = "up"
							if self.floating == "down":
									self.y += 1
							elif self.floating == "up":
									self.y -= 1
							if self.x < self.initialX - 30 and self.floating == "left":
									self.floating = "right"
							elif self.x > self.initialX + 30 and self.floating == "right":
									self.floating = "left"
							if self.floating == "right":
									self.x += 1
							elif self.floating == "left":
									self.x -= 1
					elif self.laser >= 1 and self.laser < 3000:
							self.laser += 20
					elif self.laser >= 3000:
							self.laser = 0
					if self.direction == "right":
						if boss.x + boss.width -10 > self.x + self.width :
								self.x += self.speed
						else:
								self.x = boss.x + boss.width - self.width
					if self.direction == "up":
						if boss.y +10 < self.y :
								self.y -= self.speed
						else:
								self.y = boss.y 
				else:
					if self.laser >= 1 and self.laser < 3000:
							self.laser += 20
					elif self.laser >= 3000:
							self.laser = 0
					if self.direction == "right" or self.direction == "left":
						if self.X + 3 >= self.x and self.X - 3 <= self.x:
								self.x = self.X
						elif self.X > self.x :
								self.x += self.speed
						elif self.X < self.x :
							self.x -= self.speed
					if self.direction == "up" or self.direction == "down":
						if self.Y + 3 >= self.y and self.Y - 3 <= self.y:
								self.y = self.Y
						elif self.Y > self.y :
								self.y += self.speed
						elif self.Y < self.y :
							self.y -= self.speed

class laser(object):
		intro = ["sprite/BossMinions/lasercharger1.png", "sprite/BossMinions/lasercharger2.png", "sprite/BossMinions/lasercharger3.png", "sprite/BossMinions/lasercharger4.png", "sprite/BossMinions/lasercharger5.png", "sprite/BossMinions/lasercharger6.png", "sprite/BossMinions/lasercharger7.png", "sprite/BossMinions/lasercharger8.png"]
		for i in range(len(intro)):
				intro[i] = pygame.image.load(intro[i]).convert_alpha()
		def __init__(self, x, y, direction, moving = True):
				self.x = x
				self.y = y
				self.direction = direction
				self.width = 0
				self.height = 30
				self.duration = 1
				self.exist = True
				self.display = 0
				self.moving = moving
				self.durationmax = 3000


		def fire(self, speed = 0):
				if self.moving == True:
					if self.direction == "right":
						self.x += speed
					if self.direction == "up":
						self.y -= speed
				if self.duration <= 1000:
					if self.direction == "right" or self.direction == "left":
							self.height = 2
							self.width = 3000
					elif self.direction == "up" or self.direction == "down":
							self.width = 2
							self.height = 3000
				if self.duration <= 700:
						self.duration += 20
						self.display = self.duration//100
				if self.duration > 700 and self.duration <= 1000:
						self.duration += 20
						self.display = 7
				if self.duration > 1000 and self.duration <= self.durationmax:
						self.display = 8
						self.duration += 20
						if self.direction == "right" or self.direction == "left":
							if self.height < 30:
								self.y -= 2
								self.height += 4
						elif self.direction == "up" or self.direction == "down":
							if self.width < 30:
								self.x -= 2
								self.width += 4
						
				if self.duration > self.durationmax:
						self.exist = False


		def Draw(self, window, x, y, player):
				if self.exist == True:
						if self.direction == "right":
							if self.display <= 7:
									window.blit(self.intro[self.display], (self.x- x-30,  self.y-y-23))
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
							else:
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
						elif self.direction == "left":
							if self.display <= 7:
									window.blit(self.intro[self.display], (self.x- x-30+3000,  self.y-y-23))
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
							else:
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
						elif self.direction == "up":
							if self.display <= 7:
									window.blit(self.intro[self.display], (self.x- x-30,  self.y-y-23+3000))
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
							else:
									pygame.draw.rect(window, (255, 0, 0), (self.x - x, self.y - y , self.width, self.height))
						
########## BOUTONS
class buttons():
		menu = pygame.image.load('sprite/other/Menu.png').convert_alpha()
		menu =  pygame.transform.scale(menu, (800, 600))
		pause = [pygame.image.load('sprite/other/Pause1.png'),pygame.image.load('sprite/other/Pause2.png')]
		options = [pygame.image.load('sprite/other/validate.png'), pygame.image.load('sprite/other/validate2.png')]
		for i in range(len(pause)):
				pause[i] =  pygame.transform.scale(pause[i], (70, 70))
		def __init__(self, x, y, Type = 0, width = 70, height = 70, text= ""):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.clicked = False
				self.Type = Type
				self.Activated = False
				self.down = False
				self.backx = 300
				self.backy = 100
				self.text = text
				self.timer = 0#le timer sert au bouton pause sinon il bug

		def Activate(self):
			if self.Type == 0:
				if self.timer == 0 :
					if self.clicked == True:
							if self.Activated == False:
									self.Activated = True
							elif self.Activated == True:
									self.Activated = False
							self.timer = 10
			else:
				if self.clicked == True:
						if self.Activated == False:
								self.Activated = True
						elif self.Activated == True:
								self.Activated = False

		def Draw(self, window):
			if self.timer > 0:
				self.timer -= 1
			if self.Type == 0:
					if self.down == True:
							window.blit(self.pause[1], (self.x, self.y))
					elif self.down == False:
							window.blit(self.pause[0], ( self.x, self.y))
								
		def DrawPause(self, window):
				if self.Type == 1:
						if self.Activated == True:
								window.blit(self.options[1], (self.x, self.y))
						elif self.Activated == False:
								window.blit(self.options[0], (self.x, self.y))
								


				
		def DrawBack(self, window):
				if self.Type == 0:
						window.blit(self.menu, (self.backx, self.backy))
				font = pygame.font.SysFont("comicsans", 40, True)
				text = font.render(self.text, 1 , (255, 255, 255))
				window.blit(text, (self.x + 60, self.y + 10))

########## MURS ET POINTS DE SAUVERGARDE
				
class ground(object):
		flame = [pygame.image.load('sprite/other/flame_save1.png'),pygame.image.load('sprite/other/flame_save2.png'),pygame.image.load('sprite/other/flame_save3.png'),pygame.image.load('sprite/other/flame_save4.png'), pygame.image.load('sprite/other/flame_save5.png')]
		flamegone = pygame.image.load('sprite/other/flame_saveGone.png')
		dust = []
		for i in range(7):
			imagelist = "sprite/other/dust_",str(i),".png"
			imagestr = ''.join(imagelist)
			dust.append(pygame.image.load(imagestr))
			dust[-1] =  pygame.transform.scale(dust[-1], (120, 120))
		for i in range(len(flame)):
				flame[i] =  pygame.transform.scale(flame[i], (105, 120))
		flamegone =  pygame.transform.scale(flamegone, (105, 120))
		def __init__(self, x , y, width = 61, height = 61):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.checkpoint = False
				self.flamecount = 0
				self.light = False
				self.active = 0
				self.invisible = 0

		def Draw(self, window, x, y, player):
				if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 and self.invisible == 0:
						if self.checkpoint == False:
								pygame.draw.rect(window, (50, 50, 50), (self.x - x, self.y - y, self.width, self.height))
						elif self.checkpoint == True:
								if self.x < player.x + player.width and self.x + self.width > player.x:
									if self.y + self.height > player. y and self.y < player.y + player. height:
																					self.light = True
								if self.flamecount >= 49:
										self.flamecount = 0
								else:
										self.flamecount += 1
								if self.light == True:
										if self.active > 15:
											window.blit(self.flame[self.flamecount//10], (self.x- x-50 +self.width//2,  self.y-y))
										else:
											window.blit(self.flamegone, (self.x- x-50 +self.width//2 ,  self.y-y ))
										if self.active < 35:
											window.blit(self.dust[self.active//5], (self.x- x-50 +self.width//2-20,  self.y-y))
											self.active += 1
											
								else:
										window.blit(self.flamegone, (self.x- x-50 +self.width//2 ,  self.y-y ))
										
########## SPIKE
				
				
class spike(object):
		spike = "sprite/traps/spike.png"
		image = pygame.image.load(spike).convert_alpha()
		image = pygame.transform.scale(image, (52, 20))
		def __init__(self, x = 0, y = 0, width = 52, height = 20):
				self.x = x
				self.y = y
				self.width = width
				self.height = height

		def Draw(self, window, x, y, player):
				if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :
					window.blit(self.image, (self.x- x,  self.y-y))

class message():
	messages = [pygame.image.load('sprite/messages/message1.png').convert_alpha(), pygame.image.load('sprite/messages/message2.png').convert_alpha(), pygame.image.load('sprite/messages/message3.png').convert_alpha(),pygame.image.load('sprite/messages/message4.png').convert_alpha(),
					pygame.image.load('sprite/messages/message5.png').convert_alpha(), pygame.image.load('sprite/messages/message6.png').convert_alpha(), pygame.image.load('sprite/messages/message7.png').convert_alpha(),  pygame.image.load('sprite/messages/PressBossE.png').convert_alpha()]
	def __init__(self, x = 0, y = 0,number = 1, width = 500, height = 130):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.number = number
		self.seen = False
		self.progression = 0
		self.display = None
		self.exist = True
		
	def Draw(self, window, x, y, player):
		if self.display != None and self.exist == True:
			window.blit(self.display, (int(player.x + player.width//2 - (self.width * self.progression)//2 - x), int(player.y - (self.height*self.progression)//2 - y - 120)))
		if player.x +player.width//2 < self.x + self.width//2 + 50 and player.x +player.width//2 > self.x + self.width//2 - 50 and player.y + player.height//2 < self.y + self.height//2 + 300 and player.y + player.height > self.y + self.height//2 - 300 and player.cinematic == 0:
			self.seen = True
			if self.progression < 1:
				self.display = pygame.transform.scale(self.messages[self.number-1], (int(self.width*self.progression), int(self.height*self.progression)))
				self.progression += 0.05
			else:
				self.progression = 1
				self.display = pygame.transform.scale(self.messages[self.number-1], (int(self.width*self.progression), int(self.height*self.progression)))
		else:
			if self.seen == True:
				if self.progression > 0:
					self.progression -= 0.05
				else:
					self.seen = False
					self.progression = 0
			if int(self.width*self.progression) >= 0 and int(self.height*self.progression) >= 0 and self.exist == True:
				self.display = pygame.transform.scale(self.messages[self.number-1], (int(self.width*self.progression), int(self.height*self.progression)))

class objects():
	sprite = [pygame.image.load('sprite/other/Stone1.png').convert_alpha()]
	def __init__(self, x, y, width, height, appearance):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.appearance = appearance
		
	def Draw(self, window, x, y, player):
			if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :
				window.blit(self.sprite[self.appearance], (self.x- x,  self.y-y))

class monster():
		walkframeright = ["sprite/ennemy/crowler1.png", "sprite/ennemy/crowler2.png", "sprite/ennemy/crowler3.png", "sprite/ennemy/crowler4.png", "sprite/ennemy/crowler5.png"]
		walkframeleft = []
		for i in range(len(walkframeright)):
				walkframeright[i] = pygame.image.load(walkframeright[i]).convert_alpha()
				walkframeleft.append(pygame.transform.flip(walkframeright[i], True, False))
		flyframeright = []
		flyframeleft = []
		flyframeup = []
		flyframedown = []
		for i in range(5):
			flyframeright.append(pygame.image.load("sprite/BossMinions/Minion1_right/sprite_"+str(i)+".png").convert_alpha())
		for i in range(5):
			flyframeleft.append(pygame.transform.flip(pygame.image.load("sprite/BossMinions/Minion1_right/sprite_"+str(i)+".png").convert_alpha(), True, False))
		for i in range(5):
			flyframeup.append(pygame.image.load("sprite/BossMinions/Minion1_up/sprite_"+str(i)+".png").convert_alpha())
		for i in range(5):
			flyframedown.append(pygame.image.load("sprite/BossMinions/Minion1_down/sprite_"+str(i)+".png").convert_alpha())
				
		def __init__(self, x, y, xmax, xmin, direction = "left", monstertype = 1, width= 80, height = 45):
				self.x = x 
				self.y = y +5
				self.width = width
				self.height = height
				self.speed = 4
				self.walkcount = 0
				self.exist = True
				self.alive = True
				self.direction = direction
				self.xmax = xmax
				self.xmin = xmin
				self.ymax = xmax
				self.ymin = xmin
				self.walkcountmax = 50
				self.monstertype = monstertype
				if self.monstertype == 2:
						self.width = 110
						self.height = 110

		def movement(self):
				if self.exist:
						self.walkcount += 1
						if self.walkcount >= self.walkcountmax:
								self.walkcount = 0
						if self.monstertype == 1:
								if self.x + self.speed > self.xmax:
										self.x = self.xmax
										self.direction = "left"
								if self.x - self.speed < self.xmin:
										self.direction = "right"
										self.x = self.xmin
								if self.direction == "right":
										self.x += self.speed
								elif self.direction == "left":
										self.x -= self.speed
						elif self.monstertype == 2:
								if self.x + self.speed > self.xmax and self.direction == "right":
										self.x = self.xmax
										self.direction = "left"
								if self.x - self.speed < self.xmin and self.direction == "left":
										self.direction = "right"
										self.x = self.xmin
								if self.direction == "right":
										self.x += self.speed
								elif self.direction == "left":
										self.x -= self.speed
								if self.y + self.speed > self.ymax and self.direction == "down":
										self.direction = "up"
										self.y = self.ymax
								if self.y - self.speed < self.ymin and self.direction == "up":
										self.direction = "down"
										self.y = self.ymin
								if self.direction == "down":
										self.y += self.speed
								elif self.direction == "up":
										self.y -= self.speed

		def Draw(self, window, x, y, player):
			if self.exist == True:
				#pygame.draw.rect(window, (240, 20, 20), (self.x- x,  self.y-y, self.width, self.height)) #la hitbox
				if self.monstertype == 1:
						if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :
								if self.direction == "left":
										window.blit(self.walkframeright[self.walkcount//(self.walkcountmax//len(self.walkframeright))], (self.x- x-5,  self.y-y-20))
								elif self.direction == "right":
										window.blit(self.walkframeleft[self.walkcount//(self.walkcountmax//len(self.walkframeright))], (self.x- x-5,  self.y-y-20))
				if self.monstertype == 2:
						if player.x < self.x + self.width + 2000 and player.x > self.x - 2000 and player.y < self.y + self.height + 1000 and player.y > self.y - 1000 :
								if self.direction == "left":
										window.blit(self.flyframeleft[self.walkcount//10], (self.x-x-20, self.y-y-20))
								elif self.direction == "right":
										window.blit(self.flyframeright[self.walkcount//10], (self.x-x-20, self.y-y-20))
								elif self.direction == "up":
										window.blit(self.flyframeup[self.walkcount//10], (self.x-x-20, self.y-y-20))
								elif self.direction == "down":
										window.blit(self.flyframedown[self.walkcount//10], (self.x-x-20, self.y-y-20))
						

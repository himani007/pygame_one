
#we are making an oop approach today cz its very scattered...
#and now we can have a multiplayer game!

import pygame
pygame.init()

win = pygame.display.set_mode((852,480))

pygame.display.set_caption("Hola Gameos")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#WALKLEFT LIST
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
standChar = pygame.image.load('standing.png')

#This is class that will help us to track amount of time or to manage framerate
clock = pygame.time.Clock()

class player():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.right = False
		self.left = False
		self.walkCount = 0

	def draw(self,win):
		if self.walkCount +1 >= 27:
			self.walkCount = 0 
		if self.left:
			win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount +=1
		elif self.right:
			win.blit(walkRight[self.walkCount//3], (self.x,self.y))
			self.walkCount +=1
		else:
			win.blit(standChar, (self.x,self.y))


def redrawGameWindow():
	
	win.blit(bg, (0,0)) 
	gameChar.draw(win)
	pygame.display.update()

#mainloop:
#instance of our player class:
gameChar = player(200, 420, 64, 64)
run = True
while run:
	clock.tick(27)#how many frames or images we see in a sec.

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and gameChar.x > gameChar.vel:
		gameChar.x -= gameChar.vel
		gameChar.left = True
		gameChar.right = False
	elif keys[pygame.K_RIGHT] and gameChar.x < 852-gameChar.width:
		gameChar.x += gameChar.vel
		gameChar.left = False
		gameChar.right = True
	
	else:
		gameChar.right = False
		gameChar.left = False
		gameChar.walkCount = 0

	if not(gameChar.isJump):	
		if keys[pygame.K_SPACE]:
			gameChar.isJump = True
	else:
		if gameChar.jumpCount >= -10:
			neg = 1
			if gameChar.jumpCount<0:
				neg = -1	
			gameChar.y -= (gameChar.jumpCount ** 2) * 0.5 * neg
			gameChar.jumpCount -=1
		else:
			gameChar.isJump = False
			gameChar.jumpCount = 10

#we took our drawing char outside main loop so we have to call the funxtion!
	redrawGameWindow()



pygame.quit()
		

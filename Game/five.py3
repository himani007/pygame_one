
##-----------projectile...............
# adding bullets.... multiple bullets and their velocities

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
		self.standing = True
		

	def draw(self,win):
		if self.walkCount +1 >= 27:
			self.walkCount = 0 
		if not(self.standing):
			if self.right:
				win.blit(walkRight[0], (self.x,self.y))
			else:
				win.blit(walkLeft[0], (self.x,self.y))
				
		if self.left:
			win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount +=1
		elif self.right:
			win.blit(walkRight[self.walkCount//3], (self.x,self.y))
			self.walkCount +=1
		else:
			if self.right:
				win.blit(walkRight[0], (self.x,self.y))
			else:
				win.blit(walkLeft[0], (self.x,self.y))



class projectile():
	def __init__(self, x, y,radius,color, facing):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.facing = facing
		self.vel = 10 * facing
	
	def draw_bullet(self,win):
		pygame.draw.circle(win , self.color,(self.x, self.y), self.radius)

def redrawGameWindow():
	global walkCount
	win.blit(bg, (0,0)) 
	gameChar.draw(win)

	for bullet in bullets:
		bullet.draw_bullet(win)

	pygame.display.update()
	
	
#mainloop:
#instance of our player class:
gameChar = player(200, 420, 64, 64)
run = True
bullets = []
while run:
	clock.tick(27)#how many frames or images we see in a sec.

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False

	for bullet in bullets: 
		if bullet.x <852 and bullet.x>0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and gameChar.x > gameChar.vel:
		gameChar.x -= gameChar.vel
		gameChar.left = True
		gameChar.right = False
		gameChar.standing = False

	elif keys[pygame.K_RIGHT] and gameChar.x < 852-gameChar.width:
		gameChar.x += gameChar.vel
		gameChar.left = False
		gameChar.right = True
		gameChar.standing = False
	
	else:
		gameChar.standing = True
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
#shooting from a
	if keys[pygame.K_a]:
		if gameChar.left:
			gameChar.facing = -1
		else:
			gameChar.facing = 1
		if len(bullets) <5:
			bullets.append(projectile(int(round(gameChar.x + gameChar.width//2)), int(round(gameChar.y + gameChar.height//2)), 6, (102, 0, 102), gameChar.facing))


	redrawGameWindow()



pygame.quit()
		

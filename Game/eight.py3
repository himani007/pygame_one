
#adding a score...

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
		self.hitbox = (self.x +20, self.y, 20,52)

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
		self.hitbox = (self.x +20, self.y, 20,52)
		#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

#this entire class for bullets!
class projectile():
	def __init__(self, x, y,radius,color, facing):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.facing = facing
		self.vel = 7 * facing
	
	def draw_bullet(self,win):
		pygame.draw.circle(win , self.color,(self.x, self.y), self.radius)


class enemy():
	walkRight =[pygame.image.load('R1E.png'), pygame.image.load('R2E.png'),  pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
	walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'),  pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

	def __init__(self,x,y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end 
		self.path = [self.x, self.end]
		self.walkCount = 0
		self.vel = 3
		self.hitbox = (self.x +17, self.y, 31,52)
		#keeping a track of health
		self.health =10 
		self.visible = True

	def draw(self,win):
		self.move()
		if self.visible:
			if self.walkCount +1 >= 33:
				self.walkCount = 0

			if self.vel>0:
				win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount +=1
			else:
				win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount +=1
			self.hitbox = (self.x +17, self.y, 31,52)
			#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
			pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]-20,50,10))
			pygame.draw.rect(win, (0,120,0), (self.hitbox[0], self.hitbox[1]-20,(50-5*(10-self.health)),10))
			#we r not drawing hitbox now. but its positions are where ther health bar will stay. 	

	def move(self):   #we will be changing velocity... to +ve and -ve:
		if self.vel>0:
			if self.x+self.vel < self.path[1]:
				self.x += self.vel
			else:
				self.vel = self.vel *-1
				self.walkCount = 0
		else:
			if self.x-self.vel>self.path[0]:
				self.x += self.vel
			else :
				self.vel = self.vel*-1
				self.walkCount = 0		
			
	def hit(self):
		if self.health>1:
			self.health -=1
		else:
			self.visible = False

#KEEPING A TRACK OF SCORE OF HITTING THE GOBLIN
score = 0
#we will check for collision in our main loop below.

def redrawGameWindow():
	global walkCount
	win.blit(bg, (0,0)) 

	gameChar.draw(win)

	for bullet in bullets:
		bullet.draw_bullet(win)

	enemy_1.draw(win)
	text = font_variable.render('Score: '+ str(score), 1, (0,0,0))
	win.blit(text, (32, 10))
	pygame.display.update()
	
	
#mainloop:
font_variable = pygame.font.SysFont('comicsans', 35, True)

enemy_1 = enemy(100, 420, 64, 64, 450)
gameChar = player(200, 420, 64, 64)
run = True
bullets = []

shootLoop = 0

while run:
	clock.tick(27)#how many frames or images we see in a sec.

	if shootLoop > 0:
		shootLoop +=1
	if shootLoop > 3:
		shootLoop = 0	
	
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False

	for bullet in bullets: 
		if (bullet.y-bullet.radius < enemy_1.hitbox[1]+enemy_1.hitbox[3]) and  (bullet.y+bullet.radius > enemy_1.hitbox[1]):
			if bullet.x + bullet.radius > enemy_1.hitbox[0] and (bullet.x - bullet.radius < enemy_1.hitbox[0] + enemy_1.hitbox[2]):
				enemy_1.hit()
				bullets.pop(bullets.index(bullet))
				score +=1
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

	if keys[pygame.K_a] and shootLoop ==0:
		if gameChar.left:
			gameChar.facing = -1
		else:
			gameChar.facing = 1
		if len(bullets) <5:
			bullets.append(projectile(int(round(gameChar.x + gameChar.width//2)), int(round(gameChar.y + gameChar.height//2)), 6, (102, 0, 102), gameChar.facing))
		shootLoop = 1


	redrawGameWindow()



pygame.quit()
		


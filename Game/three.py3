
#----------------CHARACTER ANIMATION:AND sprites.....(9 images)


import pygame
pygame.init()

win = pygame.display.set_mode((852,480))

pygame.display.set_caption("Hola Gameos")
#to load our image.. we need to make sure that all images are in same folder..OTHERWISE we need to mention path!
#WALKRIGHT LIST!!
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#WALKLEFT LIST
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
standChar = pygame.image.load('standing.png')


clock = pygame.time.Clock()
#This is class that will help us to track amount of time or to manage framerate

x = 250
y = 420
width = 64 #we can see from properties of image..(sprite)
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
	global walkCount
	win.blit(bg, (0,0)) #bg and then the tuple with where we wanna place background
	
	if walkCount +1 >= 27:
		walkCount = 0 # this is because we have 9 sprite images.
	if left:
		win.blit(walkLeft[walkCount//3], (x,y))#this is integer division!!
		walkCount +=1
	elif right:
		win.blit(walkRight[walkCount//3], (x,y))
		walkCount +=1
	else:
		win.blit(standChar, (x,y))

	pygame.display.update()

#mainloop:
run = True
while run:
	clock.tick(27)#how many frames or images we see in a sec.

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < 852-width:
		x += vel
		left = False
		right = True
	
	else:
		right = False
		left = False
		walkCount = 0

	if not(isJump):	
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount<0:
				neg = -1	
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -=1
		else:
			isJump = False
			jumpCount = 10

#we took our drawing char outside main loop so we have to call the funxtion!
	redrawGameWindow()



pygame.quit()
		

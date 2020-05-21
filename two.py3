
#----------------- ADDING JUMPING OPTION!

import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Hola Gameos")

x = 250
y = 450
width = 40
height = 60
vel = 5

isJump = False #.....		
jumpCount = 10

#mainloop:
run = True
while run:
	pygame.time.delay(100)#this is miniseconds!
	#checking events.....

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
	if keys[pygame.K_RIGHT] and x < 500-width:
		x += vel

	if not(isJump):	
		if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN] and y < 500-height:
			y += vel
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount<0:
				neg = -1	
			y -= (jumpcount ** 2) * 0.5 * neg
			jumpCount -=1
		else:
			isJump = False
			jumpCount = 10

	win.fill((0, 255, 0, 128)) #this is colour of whole screen...

	pygame.draw.rect(win, (255, 0, 0),(x, y, width, height))
	pygame.display.update()



pygame.quit()
		

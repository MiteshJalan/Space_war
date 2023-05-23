import pygame
#initialize pygame
pygame.init()

#screen making width and height
screen=pygame.display.set_mode((800,600))

#caption n icon
pygame.display.set_caption("Space Wars")
icon= pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change=0
playerY_change=0

def player(x,y):#sending coordiate of img
    screen.blit(playerImg, (x,y))#blit means draw on screen


#game loop
running=True

while running:
    #RGB
    screen.fill((0,0,0))

    #dont close until quit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        
        #press on key is event check if its left or right
        if event.type==pygame.KEYDOWN:#IF KEY PRESSED
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key== pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key== pygame.K_UP:
                playerY_change= -0.2
            if event.key== pygame.K_DOWN:
                playerY_change= 0.2
        if event.type==pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT or event.key== pygame.K_UP or event.key== pygame.K_DOWN :
                playerX_change = 0
                playerY_change = 0



    playerX += playerX_change
    playerY+=playerY_change
    player(playerX,playerY) #call after fill to avaoid overlap screen above player
    pygame.display.update()#to update screen every milisec as everything is moving
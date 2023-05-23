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
    

    playerX+=0.1
    player(playerX,playerY) #call after fill to avaoid overlap screen above player
    pygame.display.update()#to update screen every milisec as everything is moving
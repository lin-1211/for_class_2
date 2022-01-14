import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

done = False
clock = pygame.time.Clock

background_position = [0,0]

player_image = pygame.image.load("playerShip1_orange.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    screen.fill(BLACK)
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    screen.blit(player_image,[x,y])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
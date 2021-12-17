import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

done = False
clock = pygame.time.Clock

while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

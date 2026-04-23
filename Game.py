import pygame
from Player import player

# pygame setup

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0 # delta time
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

P1 = player(100,player_pos)

# pygame.QUIT event occurs when user clicks escape
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    # Keep reseting screen
    screen.fill((0, 0, 0))
    
    

    # draw a red circle on the screen imma test it
    pygame.draw.circle(screen, "red", player_pos, 20)


    # keys used to move

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        P1.pos.y -= P1.speed * dt
    if keys[pygame.K_s]:
        P1.pos.y += P1.speed * dt
    if keys[pygame.K_a]:
        P1.pos.x -= P1.speed * dt
    if keys[pygame.K_d]:
        P1.pos.x += P1.speed * dt

    

    # close game
    if keys[pygame.K_ESCAPE]:
       pygame.quit()
            

    # flip() the display to screen
    pygame.display.flip()

    # limit fps to 60
    dt = clock.tick(60) / 1000 

    

pygame.quit()



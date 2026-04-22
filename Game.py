import pygame


# pygame setup

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0 # delta time
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


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
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt

    

    # close game
    if keys[pygame.K_ESCAPE]:
       pygame.quit()
            

    # flip() the display to screen
    pygame.display.flip()

    # limit fps to 60
    dt = clock.tick(60) / 1000 

    

pygame.quit()



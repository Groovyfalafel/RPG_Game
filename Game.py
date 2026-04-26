import pygame
from Player import *
from Camera import *
from Settings import *


# pygame setup

pygame.init()
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
running = True
dt = 0 # delta time
player_pos = pygame.Vector2(Width / 2, Height / 2)
map_data = open("TestTiles/MapTest.txt", "r")
map = []
P1 = player(100,player_pos, 300)
cam =  camera(P1)
water = pygame.image.load("TestTiles/water.png")
grass = pygame.image.load("TestTiles/grass.png")

#load map data into the map
for i in map_data:
        i = i.strip()
        if i != "":
            map.append(i)

# pygame.QUIT event occurs when user clicks escape
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Keep reseting screen
    screen.fill((0, 0, 0))
    
    # display map
    cam.custom_draw()
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '0':
                screen.blit(grass, (col * Tile_Size - cam.offset.x, row * Tile_Size - cam.offset.y))
            elif map[row][col] == '1':
                screen.blit(water, (col * Tile_Size - cam.offset.x, row * Tile_Size - cam.offset.y))
    

    # draw a red circle on the screen imma test it
    pygame.draw.circle(screen, "red", (P1.pos.x - cam.offset.x, P1.pos.y - cam.offset.y), 20)


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
    dt = clock.tick(Fps) / 1000 

    

pygame.quit()



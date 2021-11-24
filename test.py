# import the pygame module, so you can use it
import pygame
green=(0,255,0)
white=(255,255,255)
balck=(0,0,0)
color=green
setter=1
clock = pygame.time.Clock()
# define a main function

# initialize the pygame module
pygame.init()
# load and set the logo
logo = pygame.image.load("python.png")
pygame.display.set_icon(logo)

pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((800, 600))


    # define a variable to control the main loop
running = True

    # main loop
posy = 200
posx = 200
while running:


        # event handling, gets all event from the event queue
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
            running = False

    pygame.draw.rect(screen, (255, 255, 255), [10, 20, 20, 200])
    pygame.draw.rect(screen, (255, 255, 255), [760, 10, 20, 200])
    pygame.draw.rect(screen,color, [posy, posx, 20, 20])

    #posy = posy+4
    if setter == 1:
        posy = posy+4
        color=green
        if posy == 600:
            setter = 0

    if setter==0:
        posy=posy-4
        color=white
        if posy==100:
            setter=1

    pygame.display.flip()
    screen.fill(balck)
    clock.tick(60)
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)

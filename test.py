import pygame
import time

pygame.init()
screen = pygame.display.set_mode((900, 900))
done = False

happy = pygame.image.load('home.png') # our happy blue protagonist

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)

while not done:
        start = time.time()
        # pump those events!
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        done = True

        # here comes the protagonist
        screen.fill((0,255,0))
        blit_alpha(screen, happy, (100,100), 128)

        pygame.display.flip()

        # yeah, I know there's a pygame clock method
        # I just like the standard threading sleep
        end = time.time()
        diff = end - start
        framerate = 30
        delay = 1.0 / framerate - diff
        if delay > 0:
                time.sleep(delay)

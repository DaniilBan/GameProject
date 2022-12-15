import pygame
from random import randint

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    running = True
    w = False
    x_pos = 0
    clock = pygame.time.Clock()
    screen.fill((0, 0, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m = [randint(100, 400) for i in range(2)]
                r, g, b = randint(0, 255), randint(0, 254), randint(0, 255)
                y = randint(10, 400)
                pygame.draw.circle(screen, (r, g, b), m, y, 4)

        pygame.display.flip()

    pygame.quit()
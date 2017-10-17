try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame
from lib import gui
from lib import event

# import os


def main():
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=4096)

    screen = pygame.display.set_mode((720, 1280))

    handler = event.Handler()

    while handler.appOn:
        handler.process(pygame.event.get())
        screen.blit(gui.screen, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()



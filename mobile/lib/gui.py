try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame

pygame.init()

screen = pygame.Surface((720, 1280))


LIGHT_YELLOW = (255, 250, 202)
titleFont = pygame.font.Font("fnt/iron.ttf", 100)
iconFont = pygame.font.Font("fnt/prime.ttf", 48)
line1 = "Renesas IoT Sandbox"
titleSurface = titleFont.render(line1, True, LIGHT_YELLOW)
titleRect = titleSurface.get_rect(y=20, centerx=360)
line2 = "IBM Watson API"
titleSurface2 = titleFont.render(line2, True, LIGHT_YELLOW)
titleRect2 = titleSurface2.get_rect(y=120, centerx=360)

micIcon = pygame.image.load("img/microphone.png")
micRect = micIcon.get_rect(x=300, y=700)
tempIcon = pygame.image.load("img/temp.png")

watsonIcon = pygame.image.load("img/watson_icon.png")
watsonRect = watsonIcon.get_rect(x=500, y=300)

getIoT = pygame.image.load("img/getiot.png")
getIoTRect = getIoT.get_rect(x=50, y=300)

convertData = pygame.image.load("img/convert.png")
convertDataRect = convertData.get_rect(x=280, y=300)

screen.blit(titleSurface, titleRect)
screen.blit(titleSurface2, titleRect2)

screen.blit(micIcon, micRect)

screen.blit(getIoT, getIoTRect)
screen.blit(convertData, convertDataRect)
screen.blit(watsonIcon, watsonRect)

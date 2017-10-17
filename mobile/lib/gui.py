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
tempIcon = pygame.image.load("img/temp.png")

watsonIcon = pygame.image.load("img/watson.png")
watsonRect = watsonIcon.get_rect(x=200, y=700)

getIoT = iconFont.render("Get IoT Data", True, LIGHT_YELLOW)
getIoTRect = getIoT.get_rect(x=200, y=500)

convertData = iconFont.render("Convert IoT Data", True, LIGHT_YELLOW)
convertDataRect = convertData.get_rect(x=200, y=600)

screen.blit(titleSurface, titleRect)
screen.blit(titleSurface2, titleRect2)

screen.blit(micIcon, (100, 300))
screen.blit(tempIcon, (300, 300))

screen.blit(getIoT, getIoTRect)
screen.blit(convertData, convertDataRect)
screen.blit(watsonIcon, watsonRect)

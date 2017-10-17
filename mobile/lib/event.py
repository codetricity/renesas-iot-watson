import pygame
import gui


class Handler():
    def __init__(self):
        self.appOn = True
    
    def process(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.appOn = False
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gui.getIoTRect.collidepoint(mouse_pos):
                    print("Received IoT JSON data")
                if gui.convertDataRect.collidepoint(mouse_pos):
                    print("Converted data to human text")
                

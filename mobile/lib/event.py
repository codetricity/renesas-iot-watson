try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame
import gui


class Handler():
    def __init__(self):
        self.appOn = True
        self.voiceAlert = pygame.mixer.Sound("snd/iot-mod.wav")

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
                if gui.watsonRect.collidepoint(mouse_pos):
                    print("Sent data to Watson")
                if gui.micRect.collidepoint(mouse_pos):
                    print("play sound")
                    self.voiceAlert.play()
                

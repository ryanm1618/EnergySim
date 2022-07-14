import pygame
import pygame_gui
from GUI import GUI


pygame.init()

pygame.display.set_caption('EnergySim v0.0.0')
window_surface = pygame.display.set_mode((800,600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

user_interface = GUI(800, 600)


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        user_interface.check_event(event)
               
    user_interface.update(time_delta)
        
    window_surface.blit(background, (0,0))
    user_interface.draw(window_surface)
    
    pygame.display.update()

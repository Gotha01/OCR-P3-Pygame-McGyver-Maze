import pygame

pygame.init()
window_resolution = (363,363)
font_color = (12,12,95)

pygame.display.set_caption("Mac Gyver Survivor")
window_surface = pygame.display.set_mode(window_resolution)


image_démarrage = pygame.image.load("imgstart.jpg")
image_démarrage.convert()


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False 
    
    #Corps du programme
    window_surface.fill(font_color)
    window_surface.blit(image_démarrage, (20,20))
    pygame.display.flip()
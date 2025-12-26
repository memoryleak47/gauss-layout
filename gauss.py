import pygame

def run():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    # Define Rects
    red_rect = pygame.Rect(100, 50, 200, 200)
    blue_rect = pygame.Rect(150, 150, 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        
        # Draw Rects
        pygame.draw.rect(screen, (255, 0, 0), red_rect)
        pygame.draw.rect(screen, (0, 0, 255), blue_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

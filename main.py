import pygame
import os

WIDTH = 800
HEIGHT = 650
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

RIGHT_PLANE = pygame.image.load(os.path.join('assets', 'right_fighter.png'))
RIGHT_PLANE = pygame.transform.scale(RIGHT_PLANE, (95, 70))
LEFT_PLANE = pygame.image.load(os.path.join('assets', 'left_fighter.png'))
LEFT_PLANE = pygame.transform.scale(LEFT_PLANE, (95, 70))
SKY = pygame.image.load(os.path.join('assets', 'sky.png'))

pygame.display.set_caption("Planes")

def drawWimdow(red, blue):
    WIN.blit(SKY, (0, 0))
    
    WIN.blit(RIGHT_PLANE, (blue.x, blue.y))
    WIN.blit(LEFT_PLANE, (red.x, red.y))
    
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    red = pygame.Rect(600, 325, 95, 70)
    blue = pygame.Rect(100, 325, 95, 70)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawWimdow(red, blue)
                
                
    pygame.quit()
    
if __name__ == "__main__":
    main()
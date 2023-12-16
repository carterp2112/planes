import pygame
import os
pygame.font.init()

WIDTH = 800
HEIGHT = 650
FPS = 60
RELOAD = 4
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect((WIDTH // 2) + 5, 0, 10, HEIGHT)
FONT = pygame.font.SysFont('arial', 40)

REDHIT = pygame.USEREVENT + 1
BLUEHIT = pygame.USEREVENT + 2

RIGHT_PLANE = pygame.image.load(os.path.join('assets', 'right_fighter.png'))
RIGHT_PLANE = pygame.transform.rotate(pygame.transform.scale(RIGHT_PLANE, (95, 70)), 180)
LEFT_PLANE = pygame.image.load(os.path.join('assets', 'left_fighter.png'))
LEFT_PLANE = pygame.transform.rotate(pygame.transform.scale(LEFT_PLANE, (95, 70)), 180)
SKY = pygame.image.load(os.path.join('assets', 'sky.png'))

pygame.display.set_caption("Planes")
    
def handleRedMovement(red, keysPressed):
    if keysPressed[pygame.K_a] and not red.x == (WIDTH / 2): # Left
        red.x -= 2
    elif keysPressed[pygame.K_d] and not red.x == 705: # Right
        red.x += 2
    elif keysPressed[pygame.K_w] and not red.y <= 0: # Up
        red.y -= 2
    elif keysPressed[pygame.K_s] and not red.y >= 580: # Down
        red.y += 2
    
def handleBlueMovement(blue, keysPressed):
    if keysPressed[pygame.K_LEFT] and not blue.x == 0: # Left
        blue.x -= 2
    elif keysPressed[pygame.K_RIGHT] and not blue.x == (WIDTH / 2) - 70: # Right
        blue.x += 2
    elif keysPressed[pygame.K_UP] and not blue.y <= 0: # Up
        blue.y -= 2
    elif keysPressed[pygame.K_DOWN] and not blue.y >= 580: # Down
        blue.y += 2

def handleRockets(redRockets, blueRockets, red, blue):
    for rocket in redRockets:
        rocket.x -= 8
        
        if blue.colliderect(rocket):
            pygame.event.post(pygame.event.Event(BLUEHIT))
            redRockets.remove(rocket)
        elif rocket.x <= 0:
            redRockets.remove(rocket)
    
    for rocket in blueRockets:
        rocket.x += 8
        
        if red.colliderect(rocket):
            pygame.event.post(pygame.event.Event(REDHIT))
            blueRockets.remove(rocket)
        elif rocket.x >= WIDTH:
            blueRockets.remove(rocket)
            
def drawWimdow(red, blue, redRockets, blueRockets, redHealth, blueHealth):
    WIN.blit(SKY, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    
    redHealthText = FONT.render(f'Red Health: {str(redHealth)}', 0.5, (0, 0, 0))
    blueHealthText = FONT.render(f'Blue Health: {str(blueHealth)}', 0.5, (0, 0, 0))
    WIN.blit(redHealthText, (10, 10))
    WIN.blit(blueHealthText, ((WIDTH - blueHealthText.get_width()) -10, 10))
    
    WIN.blit(RIGHT_PLANE, (blue.x, blue.y))
    WIN.blit(LEFT_PLANE, (red.x, red.y))
    
    for rocket in redRockets:
        pygame.draw.rect(WIN, (0, 0, 0), rocket)
        
    for rocket in blueRockets:
        pygame.draw.rect(WIN, (0, 0, 0), rocket)
    
    pygame.display.update()

def drawWinner(text):
    winner = FONT.render(text, 1, (0, 0, 0))
    WIN.blit(winner, ((WIDTH/2 - winner.get_width() / 2), (HEIGHT/2 - winner.get_height() / 2)))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    run = True
    clock = pygame.time.Clock()
    red = pygame.Rect(600, 325, 95, 70)
    blue = pygame.Rect(100, 325, 95, 70)
    redRockets = []
    blueRockets = []
    redHealth = 10
    blueHealth = 10
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(redRockets) <= RELOAD:
                    rocket = pygame.Rect(red.x + red.width, (red.y + red.height // 2) - 2, 10, 5)
                    redRockets.append(rocket)
                if event.key == pygame.K_RCTRL and len(blueRockets) <= RELOAD:
                    rocket = pygame.Rect(blue.x, (blue.y + blue.height // 2) - 2, 10, 5)
                    blueRockets.append(rocket)
            
            if event.type == REDHIT:
                redHealth -= 1
            if event.type == BLUEHIT:
                blueHealth -= 1
               
        winner = "" 
        if redHealth == 0:
            winner = "RED WINS"
        
        if blueHealth == 0:
            winner = "BLUE WINS"
        
        if winner != "":
            drawWinner(winner)
        
        keysPressed = pygame.key.get_pressed()
        handleRedMovement(red, keysPressed)
        handleBlueMovement(blue, keysPressed)
        
        handleRockets(redRockets, blueRockets, red, blue)
        
        drawWimdow(red, blue, redRockets, blueRockets, redHealth, blueHealth)
                
                
    pygame.quit()
    
if __name__ == "__main__":
    main()
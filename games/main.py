import pygame

pygame.init()

WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

def main(): 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    

    pygame.display.flip() 
    pygame.quit()
    clock.tick(60) # Limits the fps to 60 

if __name__ == "__main__": # main loop
    main() 
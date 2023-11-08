import pygame

pygame.init()

WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT) ,
                                 pygame.RESIZABLE)
img = pygame.image.load("D:\code\python-practice\games\Vector.png")
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(img)
clock = pygame.time.Clock()


def main(): 
    global color
    color = "red"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(color)
        pygame.display.flip() 
        if color == "red":
            color = "blue"
        else:
            color = "red"
        
        clock.tick(60) # Limits the fps to 60 
    pygame.quit()

if __name__ == "__main__": # main loop
    main() 
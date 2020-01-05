import pygame, sys
pygame.init()
dimensions = (500, 500)
canvas = pygame.display.set_mode(dimensions)
running=True
fps = int(input("FPS\n"))

clock = pygame.time.Clock()

def draw():
    canvas.fill((255,255,255))
    drawEllipse(250, 250, 200, 150, (0,0,0))
    drawDot(xE, 50)
    pygame.display.flip()
def drawEllipse(top, left, width, height, color):
    eRect=pygame.Rect(top, left, width, height)
    pygame.draw.ellipse(canvas, color, eRect)
def drawDot(x, y):
    pygame.draw.circle(canvas, (0,0,0), (x,y), 2)

xE = 0

while running:
    #yada, yada, yada...
    xE += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
    draw()
    clock.tick(fps)

pygame.quit()
sys.exit()

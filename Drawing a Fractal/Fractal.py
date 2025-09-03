import pygame


def draw(x, y):
    k = 80 # A higher value results in a more precise fractal.
  
    x = (x-250)/125
    y = (y-250)/125

    c = x + y*1j
    z = x + y*1j

    for i in range(1,k):
        z = z*z + c
    if abs(z)<= 2:
        return (0,255,0)
    
    return (0,0,0)



pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for x in range(500):
        for y in range(500):
            color = draw(x, y)
            window.set_at((x, y), color)
    
    pygame.display.flip()

pygame.quit()
exit()

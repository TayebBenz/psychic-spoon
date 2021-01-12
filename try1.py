import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = 255,255,255
case = 100,100
circle = True
p1 = (105,105)
p2 = (105,95)
p3 = (95,100)
poly_points = [p1,p2,p3]
i = 0
j = 0

d_point = [(98,100),(124,100),(150,100)]

class Square:
    def __init__(self,center):
        self.occupied = "free"
        self.center = center
tableau = [[Square((98,100)),Square((124,100)),Square((150,100))],
            [Square((98,125)),Square((124,125)),Square((150,125))],
            [Square((98,150)),Square((124,150)),Square((150,150))]
]



show = True
screen = pygame.display.set_mode(size)
circle = True
count = 0

while 1:
    screen.fill(black)
    pygame.draw.line(screen,white,(111,90),(111,165),3)
    pygame.draw.line(screen,white,(136,90),(136,165),3)
    pygame.draw.line(screen,white,(90,115),(156,115),3)
    pygame.draw.line(screen,white,(90,145),(156,145),3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                if circle:
                    tableau[j][i].occupied = "circle"
                else:
                    tableau[j][i].occupied = "cross"
                circle = not circle
                drawn_position = tableau[j][i]
                count+=1
            if event.key == K_UP:
                if(j == 0):
                    j = 2
                else:
                    j-=1
                j = j % 3
            if event.key == K_DOWN:
                j += 1
                j = j % 3
            if event.key == K_RIGHT:
                i+=1
                i = i % 3
            if event.key == K_LEFT:
                if(i == 0):
                    i = 2
                else:
                    i-=1
                i = i % 3
    position = tableau[j][i]

    for line in tableau:
        for case in line:
            if case.occupied == "circle":
                pygame.draw.circle(screen,white,case.center,10,2)
            elif case.occupied == "cross":
                pygame.draw.line(screen,white,(case.center[0]+5,case.center[1]+5),(case.center[0]-5,case.center[1]-5),2)
                pygame.draw.line(screen,white,(case.center[0]+5,case.center[1]-5),(case.center[0]-5,case.center[1]+5),2)


    if show and position.occupied == "free":
        if circle:
            pygame.draw.circle(screen,white,position.center,10,2)
        else:
            pygame.draw.line(screen,white,(position.center[0]+5,position.center[1]+5),(position.center[0]-5,position.center[1]-5),2)
            pygame.draw.line(screen,white,(position.center[0]+5,position.center[1]-5),(position.center[0]-5,position.center[1]+5),2)
    show = not show


    if count >= 5:
        if drawn_position.occupied == tableau[j][(i+1)%3].occupied:
            if drawn_position.occupied == tableau[j][(i+2)%3].occupied:
                screen.fill(white)
                sys.exit()
        if drawn_position.occupied == tableau[(j+1)%3][i].occupied:
            if drawn_position.occupied == tableau[(j+2)%3][i].occupied:
                screen.fill(white)
                sys.exit()
        if i == j:
            if drawn_position.occupied == tableau[(i+1)%3][(i+1)%3].occupied:
                if drawn_position.occupied == tableau[(i+2)%3][(i+2)%3].occupied:
                    screen.fill(white)
                    sys.exit()

    pygame.display.flip()




# ball = pygame.image.load("ball.gif")
# ballrect = ball.get_rect()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()

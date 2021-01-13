import sys, pygame
from pygame.locals import *



pygame.init()

black = 0,0,0
white = 255,255,255

size = width, height = 320, 240


class Square:
    def __init__(self,center):
        self.occupied = "free"
        self.center = center


tableau = [[Square((98,100)),Square((124,100)),Square((150,100))],
            [Square((98,125)),Square((124,125)),Square((150,125))],
            [Square((98,150)),Square((124,150)),Square((150,150))]
]

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 20)
won_message = font.render('the circles won!',True,white)
replay_message = font.render('Press Enter to replay!',True,white)


i=0
j=0
counter = 0
turns = 1
position = tableau[i][j]
circle = True
won = False

def init():
    global i
    global j
    global counter
    global turns
    global position
    global tableau
    global circle
    global won

    i=0
    j=0
    counter = 0
    turns = 1
    position = tableau[i][j]
    circle = True
    won = False


while 1:
    screen.fill(black)
    pygame.draw.line(screen,white,(111,90),(111,165),3)
    pygame.draw.line(screen,white,(136,90),(136,165),3)
    pygame.draw.line(screen,white,(90,115),(156,115),3)
    pygame.draw.line(screen,white,(90,145),(156,145),3)

    if won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    init()
                    for lines in tableau:
                        for case in lines:
                            case.occupied = "free"

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    if circle:
                        position.occupied = "circle"
                    else:
                        position.occupied = "cross"
                    circle = not circle
                    turns+=1

                if event.key == K_UP:
                    if(i == 0):
                        i = 2
                    else:
                        i-=1
                    i = i % 3
                    position = tableau[i][j]
                if event.key == K_DOWN:
                    i += 1
                    i = i % 3
                    position = tableau[i][j]
                if event.key == K_RIGHT:
                    j+=1
                    j = j % 3
                    position = tableau[i][j]
                if event.key == K_LEFT:
                    if(j == 0):
                        j = 2
                    else:
                        j-=1
                    j = j % 3
                    position = tableau[i][j]


        if counter < 1900 and position.occupied == "free":
            if circle:
                pygame.draw.circle(screen,white,position.center,10,2)
            else:
                pygame.draw.line(screen,white,(position.center[0]+5,position.center[1]+5),(position.center[0]-5,position.center[1]-5),2)
                pygame.draw.line(screen,white,(position.center[0]+5,position.center[1]-5),(position.center[0]-5,position.center[1]+5),2)
        if turns >5:
            if position.occupied == tableau[((i+1)%3)][j].occupied and position.occupied == tableau[((i+2)%3)][j].occupied:
                won = True
            if position.occupied == tableau[i][((j+1)%3)].occupied and position.occupied == tableau[i][((j+2)%3)].occupied:
                won = True
            if i == j:
                if position.occupied == tableau[((j+1)%3)][((j+1)%3)].occupied and position.occupied == tableau[((j+2)%3)][((j+2)%3)].occupied:
                    won = True

    for line in tableau:
        for case in line:
            if case.occupied == "circle":
                pygame.draw.circle(screen,white,case.center,10,2)
            elif case.occupied == "cross":
                pygame.draw.line(screen,white,(case.center[0]+5,case.center[1]+5),(case.center[0]-5,case.center[1]-5),2)
                pygame.draw.line(screen,white,(case.center[0]+5,case.center[1]-5),(case.center[0]-5,case.center[1]+5),2)








    counter +=1
    counter = counter % 5000

    if won:
        screen.blit(won_message, (180,100))
        screen.blit(replay_message, (180,125))
    pygame.display.flip()

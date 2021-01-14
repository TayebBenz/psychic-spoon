import sys, pygame
from pygame.locals import *



pygame.init()

black = 0,0,0
white = 255,255,255

size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 20)
won_message = font.render('the circles won!',True,white)
replay_message = font.render('Press Enter to replay!',True,white)

darkSquare = pygame.image.load("dark.png")


whiteSquare = pygame.image.load("white.png")

ball = pygame.image.load("ball.gif")

class Piece:
    def __init__(self,square,color,type):
        self.square = square
        square.piece = self
        self.color = color
        self.type = type


class Square:
    def __init__(self,center,color):
        self.center = center
        self.color = color
        self.piece = "free"
        self.line = 0
        self.collum = 0
        self.visibility = True

class Board:
    def __init__(self,squares):
        self.squares = squares
        self.whiteScore = 0
        self.whiteCaptures ={}
        self.darkScore = 0
        self.darkCaptures = {}

class Mouse:
    def __init__(self,mouse_position):
        self.mouse_position = mouse_position
        self.piece = "free"

class Rook:
    points = 5
    ame = "rook"
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum
        for line in range(orig_line+1,8):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == self.color):
                self.moves.append(matrix[line][orig_collum])
            else:
                break
        for line in range(orig_line-1,-1,-1):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == self.color):
                self.moves.append(matrix[line][orig_collum])
            else:
                break
        for collum in range(orig_collum+1,8):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == self.color):
                self.moves.append(matrix[orig_line][collum])
            else:
                break
        for collum in range(orig_collum-1,-1,-1):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == self.color):
                self.moves.append(matrix[orig_line][orig_collum])
            else:
                break
        return self.moves

class Knight:
    points = 3
    name = "knight"
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves =[]
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        line = orig_line + 2
        if line < 8:
            collum = orig_collum+1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])



            collum = orig_collum-1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])

        line = orig_line - 2
        if line < 8:
            collum = orig_collum+1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])


            collum = orig_collum-1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])


        collum = orig_collum + 2
        if collum < 8:
            line = orig_line+1
            if line < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])

            line = orig_line-1
            if line > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])

        collum = orig_collum - 2
        if collum < 8:
            line = orig_line+1
            if line < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])
            line = orig_line-1
            if line > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == self.color):
                    self.moves.append(matrix[line][collum])
        return self.moves

class King:
    points = "kekw"
    name = "king"
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        line = orig_line
        collum = orig_collum+1
        if (collum)<8:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])

        collum = orig_collum-1
        if (collum)>-1:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif matrix[line][collum].piece.color == self.color:
                self.moves.append(matrix[line][collum])

        line = orig_line +1
        if (line)<8:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif matrix[line][collum].piece.color == self.color:
                self.moves.append(matrix[line][orig_collum])


            collum = orig_collum+1
            if (collum)<8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif matrix[line][collum].piece.color == self.color:
                    self.moves.append(matrix[line][collum])

            collum = orig_collum-1
            if (collum)>-1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif matrix[line][collum].piece.color == self.color:
                    self.moves.append(matrix[line][collum])


        line = orig_line -1
        if (line)<8:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif matrix[line][collum].piece.color == self.color:
                self.moves.append(matrix[line][orig_collum])


            collum = orig_collum+1
            if (collum)<8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif matrix[line][collum].piece.color == self.color:
                    self.moves.append(matrix[line][collum])

            collum = orig_collum-1
            if (collum)>-1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif matrix[line][collum].piece.color == self.color:
                    self.moves.append(matrix[line][collum])


        return self.moves

class Queen:
    points = 9
    name = "queen"
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum
        for line in range(orig_line+1,8):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == self.color):
                self.moves.append(matrix[line][orig_collum])
            else:
                break
        for line in range(orig_line-1,-1,-1):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == self.color):
                self.moves.append(matrix[line][orig_collum])
            else:
                break
        for collum in range(orig_collum+1,8):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == self.color):
                self.moves.append(matrix[orig_line][collum])
            else:
                break

        for collum in range(orig_collum-1,-1,-1):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == self.color):
                self.moves.append(matrix[orig_line][collum])
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break
        return self.moves


class Pawn:
    points = 1
    name = "pawn"
    first_move = True
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves =[]
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        if orig_line == 7 or orig_line == 0:
            return self.moves

        if self.first_move:
            if self.color == "white":
                for line in range(orig_line-1,orig_line-3,-1):

                    self.moves.append(matrix[line][orig_collum])
                    self.first_move = False
            else:
                for line in range(orig_line+1,orig_line+3):
                    self.moves.append(matrix[line][orig_collum])
                    self.first_move = False

        if self.color == "white":
            for line in range(orig_line-1,orig_line-2,-1):
                self.moves.append(matrix[line][orig_collum])
        else:
            for line in range(orig_line+1,orig_line+2):
                self.moves.append(matrix[line][orig_collum])

        return self.moves

class Bishop:
    points = 3
    name = "bishop"
    moves = []

    def __init__(self,color):
        self.color = color

    def legal_sq(self,square,matrix):
        self.moves =[]
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        for line,collum in zip(range(orig_line+1,8),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == self.color):
                self.moves.append(matrix[line][collum])
            else:
                break
        #
        #
        # diog1 = True
        # diog2 = True
        # for line,collum1,collum2 in zip(range(orig_line+1,8),range(orig_collum+1,8),range(orig_collum-1,-1,-1)):
        #     print(line," ",collum1," ",collum2)
        #     if matrix[line][collum1].piece == "free" and diog1:
        #         self.moves.append(matrix[line][collum1])
        #     else:
        #         diog1 = False
        #     if matrix[line][collum2].piece == "free" and diog2:
        #         self.moves.append(matrix[line][collum2])
        #     else:
        #         diog2 = False
        #
        #
        # diog1 = True
        # diog2 = True
        # for line,collum1,collum2 in zip(range(orig_line-1,-1,-1),range(orig_collum-1,-1,-1),range(orig_collum+1,8)):
        #     print(line," ",collum1," ",collum2)
        #     if matrix[line][collum1].piece == "free" and diog1:
        #         self.moves.append(matrix[line][collum1])
        #     else:
        #         diog1 = False
        #
        #     if matrix[line][collum2].piece == "free" and diog2:
        #         self.moves.append(matrix[line][collum2])
        #     else:
        #         diog2 = False

        return self.moves


def legal_move(square,legal_sq):
    for sq in legal_sq:
        if square == sq:
            return True
    return False



matrix = [[Square((100,100),"white"),Square((200,100),"dark"),Square((300,100),"white"),Square((400,100),"dark")
        ,Square((500,100),"white"),Square((600,100),"dark"),Square((700,100),"white"),Square((800,100),"dark")]

        ,[Square((100,200),"dark"),Square((200,200),"white"),Square((300,200),"dark"),Square((400,200),"white")
        ,Square((500,200),"dark"),Square((600,200),"white"),Square((700,200),"dark"),Square((800,200),"white")]

        ,[Square((100,300),"white"),Square((200,300),"dark"),Square((300,300),"white"),Square((400,300),"dark")
        ,Square((500,300),"white"),Square((600,300),"dark"),Square((700,300),"white"),Square((800,300),"dark")]

        ,[Square((100,400),"dark"),Square((200,400),"white"),Square((300,400),"dark"),Square((400,400),"white")
        ,Square((500,400),"dark"),Square((600,400),"white"),Square((700,400),"dark"),Square((800,400),"white")]

        ,[Square((100,500),"white"),Square((200,500),"dark"),Square((300,500),"white"),Square((400,500),"dark")
        ,Square((500,500),"white"),Square((600,500),"dark"),Square((700,500),"white"),Square((800,500),"dark")]

        ,[Square((100,600),"dark"),Square((200,600),"white"),Square((300,600),"dark"),Square((400,600),"white")
        ,Square((500,600),"dark"),Square((600,600),"white"),Square((700,600),"dark"),Square((800,600),"white")]

        ,[Square((100,700),"white"),Square((200,700),"dark"),Square((300,700),"white"),Square((400,700),"dark")
        ,Square((500,700),"white"),Square((600,700),"dark"),Square((700,700),"white"),Square((800,700),"dark")]

        ,[Square((100,800),"dark"),Square((200,800),"white"),Square((300,800),"dark"),Square((400,800),"white")
        ,Square((500,800),"dark"),Square((600,800),"white"),Square((700,800),"dark"),Square((800,800),"white")]
        ]
for line in range(0,8):
    for collum in range(0,8):
        matrix[line][collum].line = line
        matrix[line][collum].collum = collum

board = Board(matrix)

mouse = Mouse(pygame.mouse.get_pos())

P_ball= Piece(matrix[7][0],"white",Rook("white"))
B_ball= Piece(matrix[7][1],"white",Bishop("white"))
K_ball = Piece(matrix[7][2],"white",Knight("white"))
Pwn_ball = Piece(matrix[6][3],"white",Pawn("white"))
Q_ball = Piece(matrix[7][3],"white",Queen("white"))
K_ball = Piece(matrix[7][4],"white",King("white"))








max_x = 150
max_y = 150
min_x = 50
min_y = 50


while 1:
    screen.fill(black)
    mouse.mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for button in pygame.mouse.get_pressed(num_buttons=3):
                if button == True:
                    for line in matrix:
                        for square in line:
                            if whiteSquare.get_rect(center=square.center).collidepoint(mouse.mouse_position) and not(square.piece=="free"):
                                mouse.piece = square.piece
                                square.visibility = False
        if event.type == MOUSEBUTTONUP:
            if not(mouse.piece == "free"):
                for line in matrix:
                    for square in line:
                        if whiteSquare.get_rect(center=square.center).collidepoint(mouse.mouse_position):
                            if not(square.piece == "free"):
                                mouse.piece.square.visibility = True
                                mouse.piece = "free"
                                break
                            else:
                                if legal_move(square,mouse.piece.type.legal_sq(mouse.piece.square,matrix)):
                                    mouse.piece.square.visibility = True
                                    mouse.piece.square.piece = "free"
                                    mouse.piece.square = square
                                    square.piece = mouse.piece
                                    mouse.piece = "free"
                                    break
                                else:
                                    mouse.piece.square.visibility = True
                                    mouse.piece = "free"
                                    break



    for line in matrix:
        for square in line:
            if square.color == "white":
                whiteS_rect = whiteSquare.get_rect(center=square.center)
                screen.blit(whiteSquare, whiteS_rect)
            else:
                darkS_rect = darkSquare.get_rect(center=square.center)
                screen.blit(darkSquare, darkS_rect)
            if not(square.piece == "free") and square.visibility == True:
                ball_rect = ball.get_rect(center=square.center)
                screen.blit(ball,ball_rect)



    if not(mouse.piece=="free"):
        if mouse.mouse_position[0] < 850 and mouse.mouse_position[0] > 50:
            if mouse.mouse_position[1] > 50 and mouse.mouse_position[1] < 850:
                ball_rect = ball.get_rect(center=(mouse.mouse_position))
                screen.blit(ball,ball_rect)


    pygame.display.flip()

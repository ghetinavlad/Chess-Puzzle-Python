import pygame
import time

from minigameChessPuzzle import *

class chess_puzzle_GUI:
    def __init__(self):
        self.Window_Size = [800,600]
        self.Screen = 0
        self.Green_ID = (0, 255, 0)
        self.White_ID = (255, 255, 255)
        self.Grey_ID = (160, 190, 220)
        self.Blue_ID = (0, 128, 255)
        self.Black_ID = (0, 0, 0)
        self.Chess_Board = {}
        self.Mini_Game_Chess_Puzzle_Object = Chess_Puzzle()
        self.Width_Board = 64
        self.Height_Board = 64
        self.Margin_Board = 10
        self.Clock = pygame.time.Clock()
        self.Square_Size = 74
        self.Chess_Board_Initial_State = {}
        self.Chess_Board_First_Move = {}
        self.Chess_Board_Second_Move = {}
        self.Chess_Board_Final_State = {}
        self.Solution = []
        self.NrMoves = 3
        self.SleepBefore = 0.3
        self.SleepAfter = 0.7

    def Init_Game(self):
        pygame.init()
        self.Screen = pygame.display.set_mode(self.Window_Size)
        pygame.display.set_caption("Chess")
        self.Set_Background()

    def Refresh_Screen(self):
        pygame.display.flip()

    def Set_Background(self):
        self.Screen.fill(self.Grey_ID)

    def Place_Piece(self,X_Coordinate,Y_Coordinate,Image):
        Image = pygame.image.load(Image)
        self.Screen.blit(Image, (X_Coordinate,Y_Coordinate))

    def Filter_Piece(self,X_Coordinate,Y_Coordinate,Piece_Type):
        self.Place_Piece(X_Coordinate,Y_Coordinate,str(Piece_Type)+".png")

    def Get_Position_On_Board_By_Click_Coordinates(self,Click_Coordinates):
        X_Coordinate = Click_Coordinates[0]
        Y_Coordinate = Click_Coordinates[1]
        return [Y_Coordinate/self.Square_Size,X_Coordinate/self.Square_Size]

    def Correct_Answer_Tick(self):
        self.Place_Piece(670,300,"tick.png")
        pygame.display.flip()

    def Checkmate_Message(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render("Checkmate! ", False, self.Black_ID)
        self.Screen.blit(textsurface, (636, 360))
        pygame.display.flip()


    def Mark_Selected_Piece(self,row,column,piece_type):
        pygame.draw.rect(self.Screen, self.Blue_ID,
                         [(self.Margin_Board + self.Width_Board) * column + self.Margin_Board,
                          (self.Margin_Board + self.Height_Board) * row + self.Margin_Board,
                          self.Width_Board,
                          self.Height_Board])
        #pygame.display.flip()
        piece_name = str(piece_type)+".png"
        self.Place_Piece(column*self.Square_Size+self.Margin_Board,row*self.Square_Size+self.Margin_Board,piece_name)
        pygame.display.flip()

    def Display_Color_Text_To_Move(self,Color):

        if Color == 0:
            ColorToString = "White"
        else:
            ColorToString = "Black"

        if Color == 0:
          self.Place_Piece(604, 45, "white-circle.png")
        else:
            self.Place_Piece(604, 45, "black-circle.png")

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render(ColorToString + " to move", False, self.Black_ID)
        self.Screen.blit(textsurface, (636, 43))
        pygame.display.flip()

    def Get_Piece_Color(self,Piece_Type):
        if "white" in Piece_Type:
            return 0
        return 1

    def Init_Chess_Board(self):
        self.Chess_Board = self.Mini_Game_Chess_Puzzle_Object.Generate_Board_Mate_In_2_Database()
        self.Chess_Board_Initial_State = self.Chess_Board[0]
        self.Chess_Board_First_Move = self.Chess_Board[1]
        self.Chess_Board_Second_Move = self.Chess_Board[2]
        self.Chess_Board_Final_State = self.Chess_Board[3]
        self.Solution = self.Chess_Board[4]
        self.AllBoards = {}
        self.AllBoards[0] = self.Chess_Board_Initial_State
        self.AllBoards[1] = self.Chess_Board_First_Move
        self.AllBoards[2] = self.Chess_Board_Second_Move
        self.AllBoards[3] = self.Chess_Board_Final_State

        self.Display_New_Board(self.AllBoards[0])

    def Display_New_Board(self,Board):
        Y_Coordinate = 10
        for row in range(8):
            X_Coordinate = 21
            for column in range(8):
                if (row+column)&1:
                    color = self.Green_ID
                else:
                    color = self.White_ID


                pygame.draw.rect(self.Screen,color,
                [(self.Margin_Board + self.Width_Board) * column + self.Margin_Board,
                 (self.Margin_Board + self.Height_Board) * row + self.Margin_Board,
                 self.Width_Board,
                 self.Height_Board])

                if Board[row][column] != None:
                  self.Filter_Piece(X_Coordinate, Y_Coordinate, Board[row][column])

                X_Coordinate += 71

            Y_Coordinate += 74


        self.Refresh_Screen()

    def Run_Main(self):
        stop_first_click = 1
        self.Chess_Board = self.AllBoards[0]
        solution_index = 0
        group_index = 0
        boards_index = 0

        First_Piece_X_Coordinates = self.Solution[0][0][0]
        First_Piece_Y_Coordinates = self.Solution[0][0][0]
        self.Display_Color_Text_To_Move(self.Get_Piece_Color(self.Chess_Board[First_Piece_X_Coordinates][First_Piece_Y_Coordinates]))

        while stop_first_click:
            for click in pygame.event.get():
                if click.type == pygame.MOUSEBUTTONDOWN:
                    click_coordinates = pygame.mouse.get_pos()
                    first_piece_move = self.Get_Position_On_Board_By_Click_Coordinates(click_coordinates)
                    First_Piece_Coordinates_X = first_piece_move[0]
                    First_Piece_Coordinates_Y = first_piece_move[1]

                    if first_piece_move == self.Solution[solution_index][group_index]:
                      self.Mark_Selected_Piece(First_Piece_Coordinates_X,First_Piece_Coordinates_Y,self.Chess_Board[First_Piece_Coordinates_X][First_Piece_Coordinates_Y])
                      group_index += 1
                      stop_second_click = 1
                      while stop_second_click:
                        for second_click in pygame.event.get():
                            if second_click.type == pygame.MOUSEBUTTONDOWN:

                                second_click_coordinates = pygame.mouse.get_pos()
                                secon_piece_move = self.Get_Position_On_Board_By_Click_Coordinates(second_click_coordinates)

                                if secon_piece_move == self.Solution[solution_index][group_index]:
                                    solution_index += 1
                                    group_index = 0
                                    boards_index +=1
                                    self.Chess_Board = self.AllBoards[boards_index]
                                    time.sleep(self.SleepBefore)

                                    self.Display_New_Board(self.Chess_Board)
                                    time.sleep(self.SleepAfter)

                                    if boards_index == self.NrMoves:
                                        self.Correct_Answer_Tick()
                                        self.Checkmate_Message()
                                        stop_second_click = 0
                                        break

                                    boards_index +=1
                                    self.Chess_Board = self.AllBoards[boards_index]
                                    self.Display_New_Board(self.Chess_Board)
                                    stop_second_click = 0
                                    break





                            elif second_click.type == pygame.QUIT:
                                pygame.quit()

                elif click.type == pygame.QUIT:
                    pygame.quit()

test = chess_puzzle_GUI()
test.Init_Game()
test.Refresh_Screen()
i = 0
test.Init_Chess_Board()
test.Run_Main()
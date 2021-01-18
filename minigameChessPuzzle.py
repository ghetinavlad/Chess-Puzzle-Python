import random

class Chess_Puzzle:
    def __init__(self):
        self.Board_Number_1_Mate_In_2_Initial_State = {}
        self.Board_Number_1_Mate_In_2_FirstMove = {}
        self.Board_Number_1_Mate_In_2_SecondMove = {}
        self.Board_Number_1_Mate_In_2_Final_State = {}
        self.SolutionMoves = []
        self.ChooseRandom = []


        for Line in range(8):
            self.Board_Number_1_Mate_In_2_Initial_State[Line] = {}
            self.Board_Number_1_Mate_In_2_FirstMove[Line] = {}
            self.Board_Number_1_Mate_In_2_SecondMove[Line] = {}
            self.Board_Number_1_Mate_In_2_Final_State[Line] = {}

        for line in range(8):
            for column in range(8):
                self.Board_Number_1_Mate_In_2_Initial_State[line][column] = None
                self.Board_Number_1_Mate_In_2_FirstMove[line][column] = None
                self.Board_Number_1_Mate_In_2_SecondMove[line][column] = None
                self.Board_Number_1_Mate_In_2_Final_State[line][column] = None

    def Generate_Board_Mate_In_2_Database(self):

        Random_Value = random.randint(0,10)
        #first step-initial state
        #White pieces on the board
        self.Board_Number_1_Mate_In_2_Initial_State[0][3] = "white-rook"
        self.Board_Number_1_Mate_In_2_Initial_State[0][4] = "white-rook"
        self.Board_Number_1_Mate_In_2_Initial_State[0][5] = "white-king"
        self.Board_Number_1_Mate_In_2_Initial_State[1][1] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[1][2] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[1][3] = "white-queen"
        self.Board_Number_1_Mate_In_2_Initial_State[1][4] = "white-knight"
        self.Board_Number_1_Mate_In_2_Initial_State[1][6] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[1][7] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[2][0] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[2][3] = "white-bishop"
        self.Board_Number_1_Mate_In_2_Initial_State[2][5] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[2][6] = "white-bishop"
        self.Board_Number_1_Mate_In_2_Initial_State[3][4] = "white-pawn"

        #Black pieces on the board
        self.Board_Number_1_Mate_In_2_Initial_State[7][0] = "black-rook"
        self.Board_Number_1_Mate_In_2_Initial_State[6][0] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[6][1] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[6][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[5][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[4][2] = "black-bishop"
        self.Board_Number_1_Mate_In_2_Initial_State[4][4] = "black-knight"
        self.Board_Number_1_Mate_In_2_Initial_State[5][5] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[7][5] = "black-king"
        self.Board_Number_1_Mate_In_2_Initial_State[4][4] = "black-knight"
        self.Board_Number_1_Mate_In_2_Initial_State[6][4] = "black-queen"
        self.Board_Number_1_Mate_In_2_Initial_State[7][4] = "black-rook"
        self.Board_Number_1_Mate_In_2_Initial_State[6][6] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[6][7] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Initial_State[3][6] = "black-bishop"


        #second step-first move
        # White pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_SecondMove[0][3] = "white-rook"
        self.Board_Number_1_Mate_In_2_SecondMove[0][4] = "white-rook"
        self.Board_Number_1_Mate_In_2_SecondMove[0][5] = "white-king"
        self.Board_Number_1_Mate_In_2_SecondMove[1][1] = "white-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[1][2] = "white-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[1][3] = "white-queen"
        self.Board_Number_1_Mate_In_2_SecondMove[1][4] = "white-knight"
        self.Board_Number_1_Mate_In_2_SecondMove[1][6] = None
        self.Board_Number_1_Mate_In_2_SecondMove[1][7] = "white-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[2][0] = "white-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[2][3] = "white-bishop"
        self.Board_Number_1_Mate_In_2_SecondMove[2][5] = "white-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[2][6] = "white-bishop"
        self.Board_Number_1_Mate_In_2_SecondMove[3][4] = "white-pawn"

        # Black pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_SecondMove[7][0] = "black-rook"
        self.Board_Number_1_Mate_In_2_SecondMove[6][0] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[6][1] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[6][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[5][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[4][2] = "black-bishop"
        self.Board_Number_1_Mate_In_2_SecondMove[4][4] = "black-knight"
        self.Board_Number_1_Mate_In_2_SecondMove[5][5] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[7][5] = "black-king"
        self.Board_Number_1_Mate_In_2_SecondMove[4][4] = None
        self.Board_Number_1_Mate_In_2_SecondMove[6][4] = "black-queen"
        self.Board_Number_1_Mate_In_2_SecondMove[7][4] = "black-rook"
        self.Board_Number_1_Mate_In_2_SecondMove[6][6] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[6][7] = "black-pawn"
        self.Board_Number_1_Mate_In_2_SecondMove[3][6] = "black-bishop"

        # third step-second move
        # White pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_FirstMove[0][3] = "white-rook"
        self.Board_Number_1_Mate_In_2_FirstMove[0][4] = "white-rook"
        self.Board_Number_1_Mate_In_2_FirstMove[0][5] = "white-king"
        self.Board_Number_1_Mate_In_2_FirstMove[1][1] = "white-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[1][2] = "white-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[1][3] = "white-queen"
        self.Board_Number_1_Mate_In_2_FirstMove[1][4] = "white-knight"
        self.Board_Number_1_Mate_In_2_FirstMove[1][6] = "white-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[1][7] = "white-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[2][0] = "white-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[2][3] = "white-bishop"
        self.Board_Number_1_Mate_In_2_FirstMove[2][5] = "black-knight"
        self.Board_Number_1_Mate_In_2_FirstMove[2][6] = "white-bishop"
        self.Board_Number_1_Mate_In_2_FirstMove[3][4] = "white-pawn"

        # Black pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_FirstMove[7][0] = "black-rook"
        self.Board_Number_1_Mate_In_2_FirstMove[6][0] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[6][1] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[6][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[5][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[4][2] = "black-bishop"
        self.Board_Number_1_Mate_In_2_FirstMove[4][4] = None
        self.Board_Number_1_Mate_In_2_FirstMove[5][5] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[7][5] = "black-king"
        self.Board_Number_1_Mate_In_2_FirstMove[4][4] = None
        self.Board_Number_1_Mate_In_2_FirstMove[6][4] = "black-queen"
        self.Board_Number_1_Mate_In_2_FirstMove[7][4] = "black-rook"
        self.Board_Number_1_Mate_In_2_FirstMove[6][6] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[6][7] = "black-pawn"
        self.Board_Number_1_Mate_In_2_FirstMove[3][6] = "black-bishop"

        #fourth step-last move
        # White pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_Final_State[0][3] = "white-rook"
        self.Board_Number_1_Mate_In_2_Final_State[0][4] = "white-rook"
        self.Board_Number_1_Mate_In_2_Final_State[0][5] = "white-king"
        self.Board_Number_1_Mate_In_2_Final_State[1][1] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[1][2] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[1][3] = "white-queen"
        self.Board_Number_1_Mate_In_2_Final_State[1][4] = "white-knight"
        self.Board_Number_1_Mate_In_2_Final_State[1][6] = None
        self.Board_Number_1_Mate_In_2_Final_State[1][7] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[2][0] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[2][3] = "white-bishop"
        self.Board_Number_1_Mate_In_2_Final_State[2][5] = "white-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[2][6] = "white-bishop"
        self.Board_Number_1_Mate_In_2_Final_State[3][4] = "white-pawn"

        # Black pieces on the board order with respect to the value
        self.Board_Number_1_Mate_In_2_Final_State[7][0] = "black-rook"
        self.Board_Number_1_Mate_In_2_Final_State[6][0] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[6][1] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[6][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[5][2] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[4][2] = "black-bishop"
        self.Board_Number_1_Mate_In_2_Final_State[4][4] = "black-knight"
        self.Board_Number_1_Mate_In_2_Final_State[5][5] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[7][5] = "black-king"
        self.Board_Number_1_Mate_In_2_Final_State[4][4] = None
        self.Board_Number_1_Mate_In_2_Final_State[6][4] = "black-queen"
        self.Board_Number_1_Mate_In_2_Final_State[7][4] = "black-rook"
        self.Board_Number_1_Mate_In_2_Final_State[6][6] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[6][7] = "black-pawn"
        self.Board_Number_1_Mate_In_2_Final_State[3][6] = None
        self.Board_Number_1_Mate_In_2_Final_State[2][7] = "black-bishop"

        self.SolutionMoves.append([[4,4],[2,5]])
        self.SolutionMoves.append([[3,6],[2,7]])

        self.ChooseRandom.append([self.Board_Number_1_Mate_In_2_Initial_State,self.Board_Number_1_Mate_In_2_FirstMove,self.Board_Number_1_Mate_In_2_SecondMove,self.Board_Number_1_Mate_In_2_Final_State,self.SolutionMoves])

        return self.ChooseRandom[0]


#4.6.2.1 PROJECT: Tic-Tac-Toe
"""
Scenario assumptions:
1. the computer (i.e., your program) should play the game using 'X's;
2. the user (e.g., you) should play the game using 'O's;
3. the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
4. all the squares are numbered row by row starting with 1 (see the example session below for reference)
5. the user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
6. the program checks if the game is over - there are four possible verdicts: the game should continue, or the game ends with a tie, your win, or the computer's win;
7. the computer responds with its move and the check is repeated;
8. don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.

Requirements
Implement the following features:
1. the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) 
so that all of the squares may be accessed using the following syntax: 'board[row][column]'
2. each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
3. implement the functions defined for you in the editor.
"""


#FUNCTIONS
import random


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in board:
        for j in i:
            print(j, end =" ")
        print()


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    from random import choice
    move_human = -1
    posible_moves = []
    for i in board:
        for j in i:
            if j != "X" or j != "0":
                posible_moves.append(j)
    while move_human < 0 :
        print("Your move: ", end="")
        answer = input()
        if answer.isnumeric():
            if (int(answer) in posible_moves):
                move_human = int(answer)
            else:
                print("Human, choose one of the available positions\n")
        else:
            print("Human, choose one of the available positions\n")

    for i in board_tuple:
        if board[i[0]][i[1]] == move_human:
            board[i[0]][i[1]] = "0"
            del board_tuple[board_tuple.index(i)]
            print("Human choosed ", move_human)
    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list_free_positions = []
    for i in board:
        for j in i:
                if j == "X" or j =="0":
                    continue
                else:
                    tuple_free_position = (board.index(i),i.index(j))
                    list_free_positions.append(tuple_free_position)
    return list_free_positions


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #horizontal check
    if (board[0][0] == sign and board[0][1] == sign and board[0][2]== sign) or \
       (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or \
       (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign):
        return sign
    #verical check
    elif (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
        (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
        (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        return sign    
    #diagonal check
    elif (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
        (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return sign
    else:
        sign = " "
        return sign


def draw_move(board):
    # The function draws the computer's move and updates the board.
    move_HAL = ()
    from random import choice
    if moves_left == 9:
        del board[4]
        print("HAL stars with position", board_int[1][1])
        board_int[1][1] = "X"
        return board
    else:
        move_HAL = random.choice(board)
        for i in board:
            if i == move_HAL:
                del board[board.index(i)]
        print("HAL chooses ", board_int[move_HAL[0]][move_HAL[1]])
        board_int[move_HAL[0]][move_HAL[1]] = "X"
        return board


# START
print("######################")
print("# TIC_TAC_TOE_vs.0.1 #")
print("######################")
print()
go_nogo = True


while go_nogo:
    user_option = input("Shall we play a game?(Type 'yes' if you want too.)")
    if user_option == "yes":
        victory = " "                                       # Fresh start
        board_int = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        moves_left = 9
        board_tuple = make_list_of_free_fields(board_int)
        display_board(board_int)
        while moves_left > 0 and victory == " ":            # The game
            draw_move(board_tuple)
            moves_left -= 1
            victory = victory_for(board_int, "X")
            display_board(board_int)
            print()
            if moves_left == 0 or victory == "X":
                print("Game finished!\n")
                break
            else:
                enter_move(board_int)
                moves_left -= 1
                victory = victory_for(board_int, "0")
                display_board(board_int)
                print()
        if victory == "X":
            print("HAL WON!!")
        elif victory == "0":
            print("HAL DIDN'T PREVAIL!")
        else:
            print("Human manage to survive!")
        
    else:
        print("You may go now! The pod bay doors are open!")
        go_nogo = False
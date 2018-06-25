#Tic Tac Toe game against the computer for HolidayCheck
#import
import os
import random 
import time

#Creation steps
#Create game board
#User input
#Winning capability
#Computer as input
#Tie scenario
#Computer AI

#Initialise board (first space empty in order to allow for the is_board_full function to work)
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#Drawing of the board to contain the board list
def draw_board():
    print("   |   |  ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |  ")

#Function to determine winner
def is_winner(board, player):
    if (board[1]== player and board[2] == player  and board[3] == player ) or \
     (board[4]== player and board[5] == player  and board[6] == player ) or \
     (board[7]== player and board[8] == player  and board[9] == player ) or \
     (board[1]== player and board[4] == player  and board[7] == player ) or \
     (board[2]== player and board[5] == player  and board[8] == player ) or \
     (board[3]== player and board[6] == player  and board[9] == player ) or \
     (board[1]== player and board[5] == player  and board[9] == player ) or \
     (board[3]== player and board[5] == player  and board[7] == player ):   
        return True
    else:
        return False

#Function to determine Tie
def is_board_full(board):
    if " " in board:
        return False
    else: 
        return True

#computer game strategy
def get_computer_move(board, player):
    if board[5] == " ":
        return 5
    else:
        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                return move
                
#Game loop
while True:
    os.system('cls')
    draw_board()
    
    #user input of 'cross' at desired gridspace
    user_input = input("Please select which grid space you would like to place the x?  ")
    user_input = int(user_input)

    #No double space useage
    if board[user_input]== " ":
        board[user_input]= "x"
    else: 
        print("This space is already taken, please choose another available space")
        time.sleep(1)

    #Check x win
    if is_winner(board, "x"):   
        os.system("cls")
        draw_board()
        print("Congratulations you are the winner!")
        break
    os.system('cls')
    draw_board()
    
    #Tie scenario        
    if is_board_full(board) == True:
        os.system("cls")
        draw_board()
        print("It's a Tie!")
        break

    #computer input of 'circle' at desired gridspace
    computer_input = get_computer_move(board, "o")

    #No double space usage
    if board[computer_input]== " ":
        board[computer_input]= "o"
    else: 
        print("This space is already taken, please choose another available space")
        time.sleep(1)

    #check o win
    if is_winner(board,"o"):   
        os.system("cls")
        draw_board()
        print("The computer won. The machines are taking over...")
        break

    #Tie scenario        
    if is_board_full(board) == True:
        os.system("cls")
        draw_board()
        print("It's a Tie!")
        break
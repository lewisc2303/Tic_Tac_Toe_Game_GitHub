#Tic Tac Toe game against the computer for HolidayCheck

#import
import os
import random 
import time
import sys

#Creation steps
#Create game board
#User input
#Winning capability
#Computer as input
#Tie scenario
#AI player
#Play again function
#create game loop function
#create user_input function
#Simplify functions
#Add O.S statement

#Initialise board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#Initialise winner function category variables
row = 1
column = 3
left_diag = 4
right_diag = 2

def clear_screen():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

def intro_screen():
    while True:
        clear_screen() 
        print("Welcome to Tic Tac Toe")
        intro_answer = input("Press any key to continue"  )
        play_game()
        break

#Drawing of the board to contain the board list
def draw_board():
    print("   |   |  ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |  ")

#Functions to determine row/column/diagonal win
def win_check(board, start_index, category, player):
    if board[start_index] == player and board[start_index + category] == player and board[start_index + (category*2)] == player:
        return True 

def check_rows(player):
    if win_check(board, 0, row, player) or win_check(board, 3, row, player) or win_check(board, 6, row, player):
        return True

def check_column(player):
    if win_check(board, 0, column, player) or win_check(board, 1, column, player) or win_check(board, 2, column, player):
        return True

def check_diagonal(player):
    if win_check(board, 0, left_diag, player) or win_check(board, 2, right_diag, player):
        return True

#Function to determine winner
def is_winner(player):
    if (check_rows(player) == True) or (check_column(player) == True) or (check_diagonal(player) == True):
        clear_screen()
        draw_board()
        if player == "x":
            print("Congratulations you are the winner!")
            play_again()
        else:
            print("The computer won. The machines are taking over...")
            play_again()
    else:
        return False
        
#Function to determine Tie
def is_board_full(board):
    if " " in board:
        return False
    else: 
        clear_screen()
        draw_board()
        print("It's a Tie!")
        play_again()

#computer game strategy
def get_computer_move(board, player):
    if board[4] == " ":
       board[4] = player
    else:
        while True:
           move = random.randint(0, 8)
           if board[move] == " ":
            board[move] = player
            break    

def get_user_input(board, player):

    #Loop to account for skipping player go when space is taken
    while True:
  
    #user input of 'cross' at desired gridspace
        while True:
            user_input = int(input("Please select which grid space you would like to place the x?  "))
            if  0 < user_input < 9 :
                user_input = user_input -1
                break
            else:
                print("Invalid entry, please enter a number between 1 and 9")

    #No double space useage
        if board[user_input]== " ":
            board[user_input]= player
            break 
        else: 
            print("This space is already taken, please choose another available space")
            time.sleep(1)
            clear_screen()
            draw_board()

#Play again function
def play_again():
    while True: 
        answer=input("Would you like to play again? yes or no ")
        clear_screen()
        draw_board()
        if answer == "yes":
            board[0:8] = [" ", " ", " ", " ", " ", " ", " ", " ", " "] 
            play_game()
            break
        elif answer == "no":
            board[0:8] = [" ", " ", " ", " ", " ", " ", " ", " ", " "] 
            intro_screen()
            break
        else:
            print("Invalid entry. Please enter 'yes' or 'no'")
        
#Game loop
def play_game():
    while True:

        #Refresh the board
        clear_screen()
        draw_board()
    
        #User input
        get_user_input(board, "x")

        #Check x win 
        is_winner("x")

        #Tie scenario        
        is_board_full(board)

        #Computer input of 'circle' at desired gridspace    
        get_computer_move(board, "o") 
    
        #Check o win
        is_winner("o")

        #Tie scenario        
        is_board_full(board)

#Play game execution
intro_screen()

     #improvement notes
        #make stuff more flexible
            #make board into function so 4x4 of 5x5 grid can be done
        #clean up code further
            #userinput +1 instead of leaving the space
            #create repeating function for print board to save lines
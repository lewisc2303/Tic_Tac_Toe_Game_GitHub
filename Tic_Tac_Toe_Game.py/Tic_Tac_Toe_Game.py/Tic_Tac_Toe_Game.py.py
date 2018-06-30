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
#AI player
#Play again function
#create game loop function
#create user_input function

#Initialise board (first space empty in order to allow for the is_board_full function to work)
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def intro_screen():
    while True:
        os.system('cls') 
        print("Welcome to Tic Tac Toe")
        intro_answer = input("Press any key to continue"  )
        play_game()
        break

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
        os.system("cls")
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
        os.system("cls")
        draw_board()
        print("It's a Tie!")
        play_again()

#computer game strategy
def get_computer_move(board, player):
    if board[5] == " ":
       board[5] = player
    else:
        while True:
           move = random.randint(1, 9)
           if board[move] == " ":
            board[move] = player
            break    

def get_user_input(board, player):
        
    #Loop to account for skipping player go when space is taken
    while True:
  
    #user input of 'cross' at desired gridspace
        user_input = input("Please select which grid space you would like to place the x?  ")
        user_input = int(user_input)

    #No double space useage
        if board[user_input]== " ":
            board[user_input]= player
            break 
        else: 
            print("This space is already taken, please choose another available space")
            time.sleep(1)
            os.system('cls')
            draw_board()

#Play again function
def play_again():
    while True: 
        answer=input("Would you like to play again? yes or no ")
        os.system('cls') 
        draw_board()
        if answer == "yes":   
            board[0:9] = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "] 
            play_game()
            break
        elif answer == "no":
            intro_screen()
            break
        
#Game loop
def play_game():
    while True:

        #Refresh the board
        os.system('cls')
        draw_board()
    
        #User input
        get_user_input(board, "x")

        #Check x win 
        is_winner(board, "x")

        #Tie scenario        
        is_board_full(board)

        #Computer input of 'circle' at desired gridspace    
        get_computer_move(board, "o") 
    
        #Check o win
        is_winner(board,"o")

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
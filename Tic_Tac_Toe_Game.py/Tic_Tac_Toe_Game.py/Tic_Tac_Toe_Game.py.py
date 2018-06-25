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

#Initialise board (first space empty in order to allow for the is_board_full function to work)
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
answer = "no"

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
    if answer == "no":
        if board[5] == " ":
            return 5
        else:
            while True:
                move = random.randint(1, 9)
                if board[move] == " ":
                    return move

#Play again function
def play_again():
    while True: 
        answer=input("Would you like to play again? yes or no ")
        os.system('cls') 
        draw_board()
        if answer == "yes":   
            board[0:9] = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "] 
            answer="yes"
            break

#Game loop
while True:

    #Refresh the board
    os.system('cls')
    draw_board()
    
    #Loop to account for skipping player go when space is taken
    while True:
  
    #user input of 'cross' at desired gridspace
        user_input = input("Please select which grid space you would like to place the x?  ")
        user_input = int(user_input)

    #No double space useage
        if board[user_input]== " ":
            board[user_input]= "x"
            break 
        else: 
            print("This space is already taken, please choose another available space")
            time.sleep(1)
            os.system('cls')
            draw_board()

    #Check x win
    if is_winner(board, "x"):   
        os.system("cls")
        draw_board()
        print("Congratulations you are the winner!")
        play_again()

    #Tie scenario        
    if is_board_full(board):
        os.system("cls")
        draw_board()
        print("It's a Tie!")
        play_again()

    #Computer input of 'circle' at desired gridspace    
    computer_input = get_computer_move(board, "o") 

    if board[computer_input]== " ":
        board[computer_input]= "o"
    
    #Check o win
    if is_winner(board,"o"):   
        os.system("cls")
        draw_board()
        print("The computer won. The machines are taking over...")
        play_again()

    #Tie scenario        
    if is_board_full(board):
        os.system("cls")
        draw_board()
        print("It's a Tie!")
        play_again()
    
    answer == "no"  

     #improvement notes
        #make stuff more flexible
            #make board into function so 4x4 of 5x5 grid can be done
        #clean up code further
            #userinput +1 instead of leaving the space
            #create repeating function for print board to save lines
            #edit code so that while loop skips a turn when play again function is activated
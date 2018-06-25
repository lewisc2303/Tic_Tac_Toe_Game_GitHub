
import os
import random 
import time

#Creation steps
#Create game board
#User input
#Winning capability
#Computer as input

#Initialise board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

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

#Inputing number which correlates to board and represented by an X
while True:
    os.system('cls')
    draw_board()
    
#user input of 'cross' at desired gridspace
    user_input = input("Please select which grid space you would like to place the x?  ")
    user_input = int(user_input)
    #board[user_input]="x" was an issue that it always showed this message with each run. remove as it is in following if statement

    #Not enable space to be taken twice
    if board[user_input]== " ":
        board[user_input]= "x"
    else: 
        print("This space is already taken, please choose another available space")
        time.sleep(1)

    if (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[4]== "x"and board[5] == "x" and board[6] == "x") or \
     (board[7]== "x"and board[8] == "x" and board[9] == "x") or \
     (board[1]== "x"and board[4] == "x" and board[7] == "x") or \
     (board[2]== "x"and board[5] == "x" and board[8] == "x") or \
     (board[3]== "x"and board[6] == "x" and board[9] == "x") or \
     (board[1]== "x"and board[5] == "x" and board[9] == "x") or \
     (board[3]== "x"and board[5] == "x" and board[7] == "x"):   
        os.system("cls")
        draw_board()
        print("Congratulations you are the winner!")
        break

    os.system('cls')
    draw_board()
#computer input of 'circle' at desired gridspace
    computer_input = input("Please select which grid space you would like to place the o?  ")
    computer_input = int(computer_input)
    #board[user_input]="x" was an issue that it always showed this message with each run. remove as it is in following if statement

    #Not enable space to be taken twice
    if board[computer_input]== " ":
        board[computer_input]= "o"
    else: 
        print("This space is already taken, please choose another available space")
        time.sleep(1)

    if (board[1]== "o"and board[2] == "o" and board[3] == "o") or \
     (board[4]== "o"and board[5] == "o" and board[6] == "o") or \
     (board[7]== "o"and board[8] == "o" and board[9] == "o") or \
     (board[1]== "o"and board[4] == "o" and board[7] == "o") or \
     (board[2]== "o"and board[5] == "o" and board[8] == "o") or \
     (board[3]== "o"and board[6] == "o" and board[9] == "o") or \
     (board[1]== "o"and board[5] == "o" and board[9] == "o") or \
     (board[3]== "o"and board[5] == "o" and board[7] == "o"):   
        os.system("cls")
        draw_board()
        print("The computer won!")
        break
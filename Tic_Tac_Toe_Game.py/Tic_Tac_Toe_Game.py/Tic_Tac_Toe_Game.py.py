
import os
import random 
import time

#Instructions
#Create game board
#User input
#No double space
#Winning functionality

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
    #user input of cross at desired gridspace
    user_input = input("Please select which grid space you would like to place the x?  ")
    user_input = int(user_input)
    board[user_input]="x"

    #Not enable space to be taken twice
    if board[user_input]== " ":
        board[user_input]= "x"
    else: 
        print("This space is already taken, please choose another available space")
        time.sleep(1)

    if (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x") or \
     (board[1]== "x"and board[2] == "x" and board[3] == "x"):   
        os.system("cls")
        draw_board()
        print("Congratulations you are the winner!")
        break
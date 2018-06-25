
import os
import random 
import time

#Creation steps
#Create game board
#User input

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
    os.system("clear")
    draw_board()
    user_input = input("Please select which grid space you would like to place the x")
    user_input = int(user_input)
    board[user_input]="x"

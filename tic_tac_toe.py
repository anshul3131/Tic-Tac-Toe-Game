import numpy as np
import pandas as pd
P1 = np.zeros(10)
P2 = np.zeros(10)
maxMoves = 9
turn  = 1
def GameBoard():
    for i in range(1,10):
        if(P1[i]):
            print('X',end = " ")
        elif(P2[i]):
            print('O',end = " ")
        else:
            print(i,end = " ")
        if(i%3==0):
            print("\n")
def WinCheck(turn) :
    w_cases = np.array([[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]])
    for x in w_cases:
        if(turn):
            if(P1[x[0]]+P1[x[1]]+P1[x[2]]==3):
                return 1
        else:
            if(P2[x[0]]+P2[x[1]]+P2[x[2]]==3):
                return 1
    return 0
print("Welcome to Tic Tac Toe\n")

while maxMoves:
    GameBoard()
    if turn:
        print("Player 1 turn!")
        value = int(input("Please Enter the value : "))
        P1[value] = 1
        if(WinCheck(turn)) :
            print("P1 Wins!")
            break
        turn  = 1 - turn
    else:
        print("Player 2 turn!")
        value = int(input("Please Enter the value : "))
        P2[value] = 1
        if(WinCheck(turn)) :
            print("P2 Wins!")
            break
        turn  = 1 - turn
    maxMoves-=1

if(maxMoves==0):
    print("Game Draw!")

        

    

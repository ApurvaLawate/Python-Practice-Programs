# -*- coding: utf-8 -*-
"""
@author: Apurva Lawate
"""

#This program is just for study purpose and to implement mechanics of snake and ladder
#It is not added with GUI Interface to play on

from PIL import Image
import random

end=100

def show_board():
    img = Image.open("sl.jpg")
    img.show()
    
def check_ladder(points):
    
    if points==2:
        print("Ladder")
        return 38
    elif points==4:
        print("Ladder")
        return 14
    elif points==9:
        print("Ladder")
        return 31
    elif points==33:
        print("Ladder")
        return 85
    elif points==52:
        print("Ladder")
        return 88
    elif points==80:
        print("Ladder")
        return 99
    else:
        #no ladder found
        return points
    
def check_snake(points):
    if points==51:
        print("Snake")
        return 11
    elif points==56:
        print("Snake")
        return 15
    elif points==62:
        print("Snake")
        return 57
    elif points==92:
        print("Snake")
        return 53
    elif points==98:
        print("Snake")
        return 8
    else:
        #no snake found
        return points
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    #Input names of both players
    p1_name=input("Player 1 Enter your name: ")
    p2_name=input("Player 2 Enter your name: ")
    
    #Initiating board square no. of both players
    pp1=0
    pp2=0
    
    turn=0
    
    while(1):
        if turn%2==0:
            print()
            #Player 1 turn
            print(p1_name,"'s turn")
            #Ask for player approval to play
            c=int(input("Press 1 to continue, 0 to quit"))
            if c==0:
                print(p1_name,"scored",pp1)
                print(p2_name,"scored",pp2)
                print("Thank you for playing")
                break
            
            #generate random number from 1 to 6
            dice = random.randint(1,6)
            print("dice showed: ",dice)
            #update board square points
            pp1=pp1 + dice
            
            #check for snakes or ladders
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            print(p1_name,"Scored: ",pp1)
            print(p2_name,"Scored: ",pp2)
            #check if player 1 wins
            
            if pp1>end:
                pp1=end
                
            if reached_end(pp1):
                print(p1_name,"won")
                break
            
        else:
            #Player 1 turn
            print()
            print(p2_name,"'s turn")
            #Ask for player approval to play
            c=int(input("Press 1 to continue, 0 to quit"))
            if c==0:
                print(p1_name,"scored",pp1)
                print(p2_name,"scored",pp2)
                print("Thank you for playing")
                break
            
            #generate random number from 1 to 6
            dice = random.randint(1,6)
            print("dice showed: ",dice)
            #update board square points
            pp2=pp2 + dice
            
            #check for snakes or ladders
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            print(p1_name,"Scored: ",pp1)
            print(p2_name,"scored: ",pp2)
            
            #check if player 2 wins
            
            if pp2>end:
                pp2=end
                
            if reached_end(pp2):
                print(p2_name,"won")
                break
        
        #increment turn even turn for player 1, odd turn for player 2
        turn = turn+1
            

show_board()
play()

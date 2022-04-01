
import random
import matplotlib.pyplot as plt


"""
Allows user to simulate St. Petersburg game with various probabilities of success
If player wins, wealth is doubled
If player loses, wealth is halved
"""

def St_Petersburg ():

     target=int(input("Please enter target wealth for player:"))
     p=float (input("Please enter probability of winning game:"))
     duration=int(input("Please enter number of rounds to be played:"))
     player=int(input("Enter player's initial capital:"))

     player_vals=[]
  
     rounds=[]

     initial=player         

     #In every round
     for i in range(0,duration+1):        
        
        if random.random() <= p:   # with p% chance, do the following if player wins do x else y
            player= player*2         
        else:          
            player=player/2
        player_vals.append(player)
        rounds.append(i)      

        if player==0: 
            print('Player is ruined at round:', i)
            break            

        if player>=target: 
            print('Player has reached target at round:', i)
            break                      

     pnl= ((player-initial)/initial) *100
    
     print('Player Wealth is:', player)
     print( 'Player P/L is: {:.2f}%'.format(pnl),'\n')
          
     #plot graph

    
        
     plt.plot(rounds,player_vals)
     plt.ylabel('Player Welath')
     plt.xlabel ('Round')

     plt.show()


     return

 #Run

St_Petersburg ()
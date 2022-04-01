
import random
import matplotlib.pyplot as plt
"""
This function simulates a user-specified number of rounds of a game with a probability p of the player winning
"""


def gambler_ruin():

#Each round, the player bets a certain amount of money. They win with probability p. If they win, they get win amt added to their bankroll
#If they lose, the house get p amt added

#win_amt amount of money changing hands

#p = probability of success

# player =  player's wealth
#house = house's wealth

# bet_amt amount player bets

# duration total number of rounds

     player_vals=[]
     house_vals =[]
     rounds=[]
     
     player=int(input("Enter player's initial capital:"))
     house=int(input("Enter house's initial capital:"))
     p=float(input("Enter probability of success for game( eg. 0.5 for 50%):"))
     duration=int(input("Enter number of rounds for game to be played:"))  
     bet_amt= int(input("Enter amount to be bet each round:"))

     win_amt=bet_amt


     initial=player
     

     #In every round
     for i in range(0,duration+1):
        if random.random() <= p:   # with p% chance, do the following

            player+= win_amt
            house-= bet_amt
        else:
            house+= bet_amt
            player-= bet_amt

        player_vals.append(player)
        rounds.append(i)
        

        if player==0: 
            print('Player is ruined at round:', i)
            break            
            

        if house==0:
            print('House is ruined at round:', i)
            break
            
            

     pnl= ((player-initial)/initial) *100
     EV= (p*win_amt)-((1-p)*bet_amt)
     print("Expeceted Value is:{:.2f}".format(EV))
     print('Player Wealth is:', player)
     print( 'Player P/L is: {:.2f}%'.format(pnl),'\n', 'House wealth is:{} '.format(house)   )
          
     #plot graph

    
        
     plt.plot(rounds,player_vals)
     plt.ylabel('Player Welath')
     plt.xlabel ('Round')

     plt.show()


     return



gambler_ruin()
 




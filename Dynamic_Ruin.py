"""
 Gambler's ruin simulation where player bets a constant fraction of their wealth
 
 """
import random
import matplotlib.pyplot as plt
   
# p, player=100, house=1000, duration=1000
def dynamic_gambler_ruin():

    player=int(input("Enter player's initial capital:"))
    house=int(input("Enter house's initial capital:"))
    p=float(input("Enter probability of success for game:"))
    duration=int(input("Enter number of rounds for game to be played:"))  


    player_vals=[]
    house_vals =[]
    rounds=[]

    initial=player
          

     #In every round
    for i in range(0,duration+1):
        bet_amt= (0.1*player)
        win_amt= bet_amt
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
    print( 'Player P/L is: {:.2f}%'.format(pnl),'\n',  'House wealth is:{} '.format(house)   )
          
    #plot graph

    
        
    plt.plot(rounds,player_vals)
    plt.ylabel('Player Welath')
    plt.xlabel ('Round')

    plt.show()


    return


dynamic_gambler_ruin()

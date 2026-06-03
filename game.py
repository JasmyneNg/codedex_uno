import card 
import player 

deck=[]
game_hand=[]

def generate_deck(): 
    colors=["red","green","yellow","blue"]
    for x in colors:
        for y in range(0,10):
            if (y<=9): 
                deck.append(card.Card(x,y))
                deck.append(card.Card(x,y))
           
        for y in ["skip","reverse","draw-2","wild"]: 
            if (y!="wild"): 
                deck.append(card.Card(x,y))
                deck.append(card.Card(x,y))
            else: 
                deck.append(card.Card("",y))
                deck.append(card.Card("",y))

def print_deck():
     print("Total Cards  ", len(deck))
     for x in deck: 
        if (x.color==""): 
            print(x.value)
        else: 
            print(x.color,x.value)
    

def assign_cards():
    print_deck()
    
    for x in range(0,7): 
        game_hand.append(deck.pop(0))
    for x in range(0,7): 
        player.player_hand(deck.pop(0))

def run_game(): 
    generate_deck()
    print_deck()
   

run_game()
            

    

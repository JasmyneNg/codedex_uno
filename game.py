import card as card_module
import player 
import random

deck=[]
game_hand=[]
game_stack=[]


current_turn="Player"

def generate_deck(): 
    colors=["red","green","yellow","blue"]
    for x in colors:
        deck.append(card_module.Card(x,0))

        for y in range(1,10):
            deck.append(card_module.Card(x,y))
            deck.append(card_module.Card(x,y))
           
        for y in ["skip","reverse","draw-2","wild","wild draw-4"]: 
            if (y=="wild" or y=="wild draw-4"): 
                deck.append(card_module.Card("",y))
            else: 
                deck.append(card_module.Card(x,y))
                deck.append(card_module.Card(x,y))

    print("Generated Deck!")

def shuffle_deck(): 
    random.shuffle(deck)


def print_deck():
     print("Total Cards  ", len(deck))
     for x in deck: 
        if (x.color==""): 
            print(x.value)
        else: 
            print(x.color,x.value)
    
def print_hand(hand): 
    for x in range(len(hand)): 
        if (hand[x].color==""):
            print(f"{x+1}. {hand[x].value}")
        else:
            print(f"{x+1}. {hand[x].color} {hand[x].value}")


def assign_cards():
  
    for x in range(0,7): 
        game_hand.append(deck.pop(0))
       
    for x in range(0,7): 
        player.player_hand.append(deck.pop(0))

    print("Assigned Cards!")



def check_if_valid_play(card_played):
  
    current_card_color=game_stack[-1].color
    current_card_value=game_stack[-1].value 

    if (card_played.value=="wild" or card_played.value=="wild draw-4"):
        return True 

    else: 
        if (current_card_color==card_played.color or current_card_value==card_played.value): 
            return True 
        elif (current_card_value=="wild" or current_card_value=="wild draw-4" and card_played.color==current_card_color):
            return True
        else: 
            return False

def check_for_emtpy_hand(): 
    if (len(player.player_hand)==0) or (len(game_hand)==0): 
        return True 
    else: 
        return False

def take_game_turn(): 

    #print("GAME STATS====================================")
    #print(f"Current Card: {game_stack[-1].color} {game_stack[-1].value}")
    #print("==============================================")

    
    for x in game_hand: 
        if (check_if_valid_play(x)):
            print("Game Played: ", x.color, x.value) 
            game_stack.append(x)

            if (isinstance(x.value, str)):
                play_unique_card(x,"game") 
            else:
                game_hand.remove(x)

            #print("Game has", len(game_hand), "left!")
            return 

    #did not find card, must draw 
        #print("Game Request To Draw...") 
        drawn_card=deck.pop(0)
        #print("Game Drew:",drawn_card.color,drawn_card.value)
        game_hand.append(drawn_card)
   
   
    
    
def play_unique_card(card,current): 
   
    if (card.value=="wild" or card.value=="wild draw-4"): 
    
        if (current=="game"): 
            target_color=""
            for x in game_hand: 
                if (x.color!=""):
                    target_color=x.color

            card.color=target_color
            game_stack.append(card_module.Card(target_color,card.value))
            game_hand.remove(card)

            take_game_turn()

        else: 
            #print("Debugging Stament ")
            player_wild_choice=input("Enter red, green, yellow, or blue: ")
            card.color=player_wild_choice
            player.player_hand.remove(card)

            take_player_turn()

    elif (card.value=="draw-2"): 
        if (current=="game"): 
            print("+2 Cards")
            player.player_hand.append(deck.pop(0))
            player.player_hand.append(deck.pop(0))

            game_hand.remove(card)
            take_game_turn()
        else: 

            
            game_hand.append(deck.pop(0))
            game_hand.append(deck.pop(0))
            player.player_hand.remove(card)
            take_player_turn()

    elif (card.value=="skip"): 
        if (current=="game"): 
            print("Skipped!")
            game_hand.remove(card)
            take_game_turn() 
        
        else: 
            
            player.player_hand.remove(card)
            take_player_turn() 

    elif (card.value=="reverse"): 
        if (current=="game"):
            game_hand.remove(card) 
            take_game_turn() 
        
        else: 
            print("Reversed!")
            
            player.player_hand.remove(card)
            take_player_turn() 

    if (card.value=="wild draw-4"): 
        if (current=="game"): 
            print("+4 Cards")
            player.player_hand.append(deck.pop(0))
            player.player_hand.append(deck.pop(0))
            player.player_hand.append(deck.pop(0))
            player.player_hand.append(deck.pop(0))

            print_hand(player.player_hand)

           # game_hand.remove(card)
            take_game_turn()
        else: 
            game_hand.append(deck.pop(0))
            game_hand.append(deck.pop(0))
            game_hand.append(deck.pop(0))
            game_hand.append(deck.pop(0))

            #player.player_hand.remove(card)
            take_player_turn()
        
def take_player_turn(): 
    print("PLAYER TURN===========================")
    print(f"Current Card: {game_stack[-1].color} {game_stack[-1].value}")
    print("======================================")
    
    print_hand(player.player_hand)
    
    print("======================================")
    card_play=int(input("Enter a card number to play (1-" + str(len(player.player_hand)) + ") or (0) to draw a card: "))
    if (card_play==0): 

        #print("Player Request To Draw...") 
        drawn_card=deck.pop(0)
        #print("Player Drew:",drawn_card.color,drawn_card.value)
        player.player_hand.append(drawn_card)


    elif (card_play<0 or card_play>len(player.player_hand)): 
        print("Invalid->Try Again")

        take_player_turn()

    else: 
        if (check_if_valid_play(player.player_hand[card_play-1])): 
            
            game_stack.append(player.player_hand[card_play-1])

            #check if unique card 
            if (isinstance(player.player_hand[card_play-1].value, str)): 
                current_card=player.player_hand[card_play-1]
                play_unique_card(current_card,"player")

            else:
                player.player_hand.pop(card_play-1)

           

        else: 
            print("Invalid->Try Again")
            take_player_turn()







def run_game(): 

    generate_deck()
    shuffle_deck()
    #print_deck()
    assign_cards()

    #pull first card off the stack 
    first_card=deck.pop(0)
    game_stack.append(first_card)

    while not check_for_emtpy_hand(): 
        take_player_turn()
        take_game_turn()

    if (len(game_hand==0)): 
        print("Game won Uno!")
    else: 
        print("Player won Uno!")


    player_again=input("Would you like to play again? (T or F)")
    if (player_again=="T"): 
        run_game() 
    else: 
        return 



    
   

run_game()
            

    

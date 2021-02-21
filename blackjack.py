"""
Project: BlackJack
Author: Nicholas Colonna
"""
import random
import time

cards = ["2","3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]   #list of the 13 card values in a standard card deck
suits = ["♥", "♦", "♠", "♣"]    #list of the 4 suits in a standard card deck

'''
Purpose: creates a deck of standard cards and shuffles them
Input: None
Return: list containing a shuffled deck of cards
'''
def shuffled_deck():
    deck = []
    for suit in suits:      #combine cards and suits together to create a deck of 52 cards (non shuffled)
        for card in cards:
            deck.append(card + suit)

    random.shuffle(deck)    #shuffle cards
    return deck

'''
Purpose: returns the value of a card based on the cards face value
Input: cards from hand (list of strings)
Return: integer representing the value of a card in a hand
'''
def hand_value(hand):
    hand_total = 0      
    aces = 0    #counts number of Aces in hand

    for card in hand:
        try:
            if len(card) == 3:          # 10 is only card with length 3
                hand_total += 10
            elif int(card[0]) <= 10:    # 2 - 9 should be assigned based on value
                hand_total += int(card[0])
        except ValueError:
            if card[0] == 'A':          # assume an Ace equals 11 value until we analyze further
                hand_total += 11
                aces += 1
            else:                       # must be J, Q or K
                hand_total += 10

    # Check if Ace should be a 11 or 1
    while aces > 0:
        if hand_total > 21:     #if having an Ace valued at 11 busts our hand, make value a 1
            hand_total -= 10
            aces -= 1
        else:
            break

    return hand_total

"""
Purpose: checks if the user would like to play again
Input: None
Return: boolean (True if keep playing, False if stop playing)
"""
def play_again():
    while True:
        keep_playing = input("\nWould you like to play again? (Y / N): ")
        if keep_playing.upper() == "Y":
            print(40*"_")
            return True
        elif keep_playing.upper() == "N":
            return False
        else:       #invalid input
            print("Sorry, that was not a valid input.")
            #play_again()

"""
Purpose: main loop for the game BlackJack - carries out the core game functions
Input: None
Output: prints game instructions and cards to the screen
Return: None
"""
def blackjack():
    input("\nWelcome to BLACKJACK! Please type 'Enter' to start playing.")
    playing = True      
    while playing:
        card_deck = shuffled_deck()
        bust = False
        stay = False

        # deal initial hands
        player = [card_deck.pop()]
        dealer = [card_deck.pop()]
        player.append(card_deck.pop())
        dealer.append(card_deck.pop())

        
        if hand_value(dealer) == 21 and hand_value(player) == 21:   #Draw if both player and dealer dealt Blackjack
            print("\nDealer: {} - {}".format(hand_value(dealer), dealer))
            print("Player: {} - {}".format(hand_value(player), player))
            print("\nDRAW! Both you and the Dealer have Blackjack.")
            playing = play_again()      
            continue
        elif hand_value(dealer) == 21:      #Player loses if dealer is dealt Blackjack
            print("\nDealer: {} - {}".format(hand_value(dealer), dealer))
            print("Player: {} - {}".format(hand_value(player), player))
            print("\nLOSER! Dealer has Blackjack.")
            playing = play_again()      
            continue
        elif hand_value(player) == 21:      #Player wins if dealt Blackjack
            print("\nDealer: {} - {}".format(hand_value(dealer), dealer))
            print("Player: {} - {}".format(hand_value(player), player))
            print("\nWINNER! You have BLACKJACK!")
            playing = play_again()
            continue

        print("\nDealer: {} - {}".format(hand_value(dealer[1:]), ['??', dealer[1]]))     #Dealer's first card is always dealt face down
        print("Player: {} - {}".format(hand_value(player), player))

        # Player's turn: Loop until player either busts or elects to stay
        while bust == False and stay == False:
            if len(player) == 2:
                choice = input("\nWould you like to Hit, Double Down, or Stay? (H / D / S): ")
            else:
                choice = input("\nWould you like to Hit or Stay? (H / S): ")
            
            if choice.upper() == "S":   #if player elects to stay, turn is over
                stay = True
                break
            elif choice.upper() == "H":     #if player elects to hit, add another card to hand
                player.append(card_deck.pop())
                print("Player: {} - {}".format(hand_value(player), player))
            elif choice.upper() == "D" and len(player) == 2:
                player.append(card_deck.pop())
                print("Player Doubled Down")
                time.sleep(1)
                print("Player: {} - {}".format(hand_value(player), player))
                stay = True
                break
            else:   #invalid input
                print("\nSorry, that was not a valid input.")
                continue
            
            if hand_value(player) > 21:     #player's hand busts
                bust = True
            elif hand_value(player) == 21:  #player's hand is 21
                stay = True

        if bust == True:
            print("\nLOSER! Your hand BUSTS!")
            playing = play_again()
            continue

        # Deal final cards to the dealer until the dealer's hand is greater than or equal to 17
        print("\nDealer: {} - {}".format(hand_value(dealer), dealer))
        while hand_value(dealer) < 17:
            time.sleep(1)
            dealer.append(card_deck.pop())
            print("Dealer: {} - {}".format(hand_value(dealer), dealer))

        time.sleep(1)
        if hand_value(dealer) > 21:                         #dealer busts
            print("\nWINNER! Dealer's hand BUSTS!")
        elif hand_value(player) > hand_value(dealer):       #player > dealer
            print("\nWINNER! Your hand beat the dealer!")
        elif hand_value(player) == hand_value(dealer):      #player = dealer
            print("\nDRAW! Your hand tied the dealer!")
        elif hand_value(player) < hand_value(dealer):       #player < dealer
            print("\nLOSER! Your hand lost to the dealer.")
        
        playing = play_again()


blackjack()
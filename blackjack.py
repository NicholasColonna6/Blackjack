"""
Project: Blackjack Simulator
Version: 1.0
Author: Nicholas Colonna

Summary: This program is a simulator to the popular casino game Blackjack!
"""
import random

cards = ["2","3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]	#list of the 13 card values in a standard card deck
suits = ["♥", "♦", "♠", "♣"]	#list of the 4 suits in a standard card deck

'''
Purpose: creates a deck of standard cards and shuffles them
Input: None
Output: a list containing a shuffled deck of cards
'''
def shuffled_deck():
	deck = []		#list all 52 cards in a standard deck
	for suit in suits:		#combine cards and suits together to create a deck of 52 cards (non shuffled)
		for card in cards:
			deck.append(card + suit)

	#shuffle the deck of cards
	random.shuffle(deck)
	return deck

'''
Purpose: returns the value of a card based on the cards face value
Input: card from hand
Output: an integer representing the value of a card in a hand
'''
def hand_value(hand):
	hand_total = 0		#keeps track of sum of all cards in hand
	aces = 0			#keep count of number of Aces in hand for Ace value adjustments

	for card in hand:	#loop through hand of cards, assigning card values based on faces
		try:
			if len(card) == 3:
				hand_total += 10
			elif int(card[0]) <= 10:
				hand_total += int(card[0])
		except ValueError:
			if card[0] == 'A':		#Assume an Ace equals 11 value until we analyze further
				hand_total += 11
				aces += 1
			else:
				hand_total += 10

	#We now check if Ace should be a 11 or 1
	while aces > 0:
		if hand_total > 21:		#if having an Ace as 11 busts our hand, make a 1
			hand_total -= 10	#subtract the 10 from hand total to account for adjustment
			aces -= 1
		else:					#if hand has not busted, no adjustments needed
			break

	return hand_total

"""
Purpose: checks if the user would like to play again
Input: None
Output: boolean (True if keep playing, False if stop playing)
"""
def play_again():
	keep_playing = input("\nWould you like to play again? (Y / N): ")
	if keep_playing == "Y":
		return True
	elif keep_playing == "N":
		return False
	else:		#invalid input
		print("Sorry, that was not a valid input.")
		play_again()


#print welcome message and prompt user to click 'Enter' when ready to play
input("\nWelcome to BLACKJACK! Please type 'Enter' to start playing.")
playing = True		#boolean allows user to keep playing until they elect to stop
while playing:
	card_deck = shuffled_deck()		#get shuffled deck of cards
	bust = False		#boolean becomes True if player busts (hand above 21)
	stay = False		#boolean becomes True if player elects to Stay or hand equals 21

	#deal initial hands
	player = [card_deck.pop()]		#hand is a list representing the player's hand
	dealer = [card_deck.pop()]		#dealer is a list representing the dealer's hand
	player.append(card_deck.pop())
	dealer.append(card_deck.pop())

	if hand_value(dealer) == 21:		#if dealer is dealt Blackjack, print both dealer cards face up and print message
		print("\nDealer: {}".format(dealer))
		print("Player: {}".format(player))
		print("\nLOSER! Dealer has Blackjack.")
		playing = play_again() 	#prompt user to play again		
		continue
	
	print("\nDealer: {}".format(['??', dealer[1]]))
	print("Player: {}".format(player))

	#check if player has BlackJack, print player has Blackjack and return
	if hand_value(player) == 21:		#if player is dealt Blackjack, print player is a winner
		print("\nBLACKJACK! You WIN!")
		playing = play_again()		#prompt user to play again
		continue

	while bust == False and stay == False:	#loop with same user options until the player Busts or elects to Stay
		choice = input("\nWould you like to Hit or Stay? (H / S): ")
		if choice == "S":	#if user Stays, player turn is over - break loop
			stay = False
			break
		elif choice != "H":	#invalid input
			print("\nSorry, that was not a valid input.")
			continue
		#player elects to hit
		player.append(card_deck.pop())
		print("\nPlayer: {}".format(player))
		
		#check if player Busts or has 21
		if hand_value(player) > 21:		#player hand is greater than 21
			bust = True
			print("\nBUST! You LOSE!")
			continue
		elif hand_value(player) == 21:	#player hand equals 21
			stay = True

	#if player Busts, prompt to play again
	if bust == True:
		playing = play_again()		#prompt user to play again	
		continue

	#Now we complete the round by dealing final cards to dealer
	print("\nDealer: {}".format(dealer))
	while hand_value(dealer) < 17:		#dealer must hit if hand is at or below 16:
		dealer.append(card_deck.pop())
		print("Dealer: {}".format(dealer))

	if hand_value(dealer) > 21: 	#dealer hand busts
		print("\nWIN! Dealer's hand BUSTS!")
	elif hand_value(player) > hand_value(dealer):		#player > dealer
		print("\nWIN! Your hand beat the dealer!")
	elif hand_value(player) == hand_value(dealer):		#player = dealer
		print("\nDRAW! Your hand tied the dealer!")
	elif hand_value(player) < hand_value(dealer):		#player < dealer
		print("\nLOSER! Your hand lost to the dealer.")
	
	playing = play_again()

#need to figure out a way to do math with picture cards (J, Q, K, A)
	#one idea is to create a dictionary for each face and have a corresponding value

#maybe add a way to elect to keep playing with same deck or reshuffle cards?

#find dynamic way to print all cards in hand (no matter how many)
import random
from random import shuffle
print('Hello, welcome to the game 2 red queens!, begin by choosing a card out of the 13 supplied to you')
deck = ['S1', 'S2', 'S3', 'S4', 'S5','S6', 'S7', 'S8', 'S9', 'S10', 'JS', 'QS', 'KS',
'H1', 'H2', 'H3', 'H4', 'H5','H6', 'H7', 'H8', 'H9', 'H10', 'JH', 'QH', 'KH',
'D1', 'D2', 'D3', 'D4', 'D5','D6', 'D7', 'D8', 'D9', 'D10', 'JD', 'QD', 'KD',
'C1', 'C2', 'C3', 'C4', 'C5','C6', 'C7', 'C8', 'C9', 'C10', 'JC', 'QC', 'KC']
my_suits = ['S', 'H', 'D', 'C']
my_class = ["A", "K", "Q", "J"]
#List of card in a deck, suits and classes


def magic_trick():
    deck.remove('QH')
    deck.remove('QD')
    new_deck = [[i] for i in range(53)]
    shuffle(deck)
    return(deck)

magic_trick()
print(deck)
#shuffling the card deck


print('Choose a card from here!')
card_set = deck[:13]
def magic_trick_two():
    shuffle(card_set)
    return(card_set)

magic_trick_two()
print(card_set)
#taking 13 random cards from the deck

print("Please pick a card")
user_input = input("Card choice = ")

def validation():
    if user_input in card_set:
        print("Your card is " + user_input)
        print(card_set)
    else:
        print("Please pick another card ")
        return(input("Card choice = "))
        print(card_set)


validation()
#checking as to whether the card the user inputs is actually in the deck

def magic_trick_three():
    card_set.remove(user_input)
    shuffle(card_set)
    print(card_set)

magic_trick_three()
#taking the cusers card out so the other cards can be shuffled

def placing_back():
    card_set.append(user_input)
    card_set.append('QH')
    card_set.insert(0, 'QD')
#https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list
    print(card_set)

placing_back()
#putting back the users card and the two red Queens

print("Your card is between the two red Queens")

#we next see the dealer parsing through the cards e.g B-E-T-W-E-E-N with a new variable made each time to use the previous outcome of the last function
def main_event_one():
    for items in card_set[0:7]:
        print(items)

main_event_one()
print(card_set[7:17])

card_set_two = card_set[7:17] + card_set[0:7][::-1]
print(card_set_two)

card_set_two = card_set[7:17] + card_set[0:7][::-1]
def main_event_two():
    for items in card_set_two[0:3]:
        print(items)

main_event_two()
print(card_set_two[3:17])

card_set_three = card_set_two[3:17] + card_set_two[0:3][::-1]
print(card_set_three)

card_set_three = card_set_two[3:17] + card_set_two[0:3][::-1]
def main_event_three():
    for items in card_set_three[0:3]:
        print(items)

main_event_three()
print(card_set_three[3:17])

card_set_four = card_set_three[3:17] + card_set_three[0:3][::-1]
print(card_set_four)

card_set_four = card_set_three[3:17] + card_set_three[0:3][::-1]
def main_event_four():
    for items in card_set_four[0:3]:
        print(items)

main_event_four()
print(card_set_four[3:17])

card_set_five = card_set_four[3:17] + card_set_four[0:3][::-1]
print(card_set_five)

card_set_five = card_set_four[3:17] + card_set_four[0:3][::-1]
def main_event_five():
    for items in card_set_five[0:6]:
        print(items)

main_event_five()
print(card_set_five[6:17])

final_set = card_set_five[0:6] + card_set_five[6:17][::-1]
print(final_set)

user_input = input("Is your card between the queens? ")

if user_input == "yes":
    print("Its all magical")
elif user_input == "no":
    print("oh ****")
else:
    print("Only yes or no allowed")
    user_input = input("Is your card between the queens? ")
#Asking the user whether their card is within the two red Queens

def main():
    game = 'Assignment.py'
    print(game)
    play_again()

def play_again():
    while True:
        play_again = input('Would you like to play again?(yes or no) > ')
        if play_again == 'yes':
            main()
        if play_again == 'no':
            exit()
        else:
            print('I am sorry I could not recognize what you entered')
main()
#solution from https://stackoverflow.com/questions/17159485/how-do-you-restart-a-python-guess-a-number-game
#function asking the user whether they want to play again. If yes the game replays, if not then it shuts down. 

#user_input = input("Do you want to play again? ")

#if user_input == "yes":
#    print("Please restart the application")
#elif user_input == "no":
#    print("Thank you for your time")
#else:
#    print("Only yes or no allowed")

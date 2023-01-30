
import random

#a function for the first roll
def first_roll(ask_response):
    die_roll = 0
    if ask_response.lower() == "no":
        print("okay, have a nice day")
        exit 
    elif ask_response.lower() == "yes":
        print("Okay!")
        print("Here is the number you rolled!")
        die_roll = (random.randrange(1,6))
        print(die_roll)
    return die_roll


def repeat_roll(fst_roll):
    print("Here is the next number you rolled!")
    roll_again = (random.randrange(1,6))
    print(str(roll_again) + "\n")
    
    if (roll_again ==1 and fst_roll == 1): 
        print("You rolled a snake eyes pair")
    elif (roll_again ==2 and fst_roll == 2): 
        print("You rolled a ballerina pair")
    elif (roll_again == 3 and fst_roll == 3): 
        print("You rolled a triple pair")
    elif (roll_again == 4 and fst_roll == 4): 
        print("You rolled a square pair")
    elif (roll_again == 5 and fst_roll == 5): 
        print("You rolled a Big Ben pair")
    elif (roll_again == 6 and fst_roll == 6): 
        print("You rolled a boxcar pair")
    else:
        print("Your rolled numbers are unique")

    return roll_again

#main function 
ask = input("Roll a dice? (yes or no)\n")
first_die = first_roll(ask)
again = "y"
while again.lower().strip() != "no":
    again = input("\nWould you like to play again?\n")
    if again.lower() == "no":
        break 
    elif again.lower() == "yes":
        repeat_roll(first_die)
    else: 
        print("incorrect entry")
    

print("Thanks for playing!")

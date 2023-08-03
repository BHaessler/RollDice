import random
DICE_ART = {
    1: (
        " ──────── ",
        "│         │",
        "│    ●    │",
        "│         │",
        " ────────",
    ),
    2: (
        " ──────── ",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        " ──────── ",
    ),
    3: (
        " ──────── ",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        " ──────── ",
    ),
    4: (
        " ──────── ",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        " ──────── ",
    ),
    5: (
        " ──────── ",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        " ──────── ",
    ),
    6: (
        " ──────── ",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        " ──────── ",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def first_roll(ask_response):
    """This function is for the first roll. It takes the input of the user to decide 
    to roll a number. The number is rolled randomly and then given back to the user. 
    """
    die_roll = 0
    if ask_response.lower() == "no":
        print("okay, have a nice day")
        exit 
    elif ask_response.lower() == "yes":
        print("Okay!")
        print("Here is the number you rolled!")
        die_roll = (random.randrange(1,6))
        print(die_roll)
        outputing_dice = print_dice(1, [die_roll])
        print(f"\n{outputing_dice}")
    return die_roll


def repeat_roll(fst_roll):
    """ This is a program that rolls another dice for the user. The dice
    is rolled randomly and then compared to the first to give the user a 
    secondary name for the pair they rolled. 
    """
    print("Here is the next number you rolled!")
    roll_again = (random.randrange(1,6))
    print(str(roll_again) + "\n")
    print("This roll will be compared to your first roll to check for pairs.")
    
    if (roll_again ==1 and fst_roll == 1): 
        print("You rolled a snake eyes pair, which is two ones")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    elif (roll_again ==2 and fst_roll == 2): 
        print("You rolled a ballerina pair, which is two twos")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    elif (roll_again == 3 and fst_roll == 3): 
        print("You rolled a triple pair, which is two threes")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    elif (roll_again == 4 and fst_roll == 4): 
        print("You rolled a square pair, which is two fours")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    elif (roll_again == 5 and fst_roll == 5): 
        print("You rolled a Big Ben pair, which is two fives")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    elif (roll_again == 6 and fst_roll == 6): 
        print("You rolled a boxcar pair, which is two sixes")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    else:
        print("Your rolled numbers are unique")
        outputing_dice = print_dice(2,[roll_again, fst_roll])
        print(f"\n{outputing_dice}")
        
    return roll_again



def print_dice(number_of_die, die_faces): 
    """This is a function that will take the number of dice, and 
    their randomly rolled numbers and show them as a command line
    image, using strings.
    """
    faces_shown = []
    dice_faces_rows = []

    for value in die_faces:
        faces_shown.append(DICE_ART[value])
    
    for row_piece in range(DIE_HEIGHT):
        row_component = []
        for die in faces_shown:
            row_component.append(die[row_piece])
        row_string = DIE_FACE_SEPARATOR.join(row_component)
        dice_faces_rows.append(row_string)


    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS OF YOUR ROLL ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram        


#main function 
ask = input("Roll a dice? (yes or no)\n")
first_die = first_roll(ask)

again = "y" #declaring a variable to use later 
while again.lower().strip() != "no":
    again = input("\nWould you like to play again?\n")
    if again.lower() == "no":
        break 
    elif again.lower() == "yes":
        repeat_roll(first_die)
    else: 
        print("incorrect entry")
    

print("\nThanks for playing!")

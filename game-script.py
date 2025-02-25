"""
SIMPLE ORCHARD GAME

This Python script simulates the popular Haba game, "First Orchard"

The actual game can be found here: https://www.habausa.com/products/my-very-first-games-first-orchard

It is a simple children's game where the goal is
to pick the fruits (from the trees) before the raven
reaches the end of a given path. If the raven reaches the
end of the path and there are still fruits on the trees, the player
loses.

It really is a fun family game and a great game to play with young kids.

"""

import random

def show_instructions() -> None:
    """
    This function will output the basic instructions
    of how to play the game
    :return: None
    """
    txt = ("Your goal is to collect all of the 4 colored fruits before the raven can get to them.\n\n"
           "Type 'r' to roll the dice\n"
           "Type 'i' to show the instructions,\n"
           "Type 'q' to quit the game.\n")

    print(txt)


def roll_dice(faces:str) -> str:
    """
    This function will choose a random value from the
    provided faces found on the simulated dice
    :param faces: a tuple or list
    :return: a string
    """
    # choose a random value from the list
    roll = random.choice(faces)
    # print out to console what the roll value was
    print("You rolled a {}. \n".format(roll))
    return roll

def basket(r:int, g:int, b:int, y:int) -> str:
    """
    This function will enable the user to pick a color that is valid since the basket
    roll allows the user to pick any color (as long as there is at least 1 of that color
    available)
    :param r: integer value denoting how many pieces of red fruit are available
    :param g: integer value denoting how many pieces of green fruit are available
    :param b: integer value denoting how many pieces of blue fruit are available
    :param y: integer value denoting how many pieces of yellow fruit are available
    :return: string denoting the color picked by the user
    """
    # reassigning variables for better nomenclature
    red = r
    green = g
    blue = b
    yellow = y

    print("You can pick any available colored fruit")

    # initialize a variable so that it can allow easy exit out of while loop
    loop_count = 0
    while loop_count == 0:
        status(r = red, g = green, b = blue, y = yellow)
        uc = input("Pick a color (red, green, blue, yellow): ")
        if(uc.lower() not in ['red','green','blue','yellow']):
            print("Invalid color! Try again!\n")
        elif(uc.lower() == 'red' and red > 0):
            print("Great choice! You picked " + uc + "\n")
            loop_count = 1
        elif(uc.lower() == 'green' and green > 0):
            print("Great choice! You picked " + uc + "\n")
            loop_count = 1
        elif(uc.lower() == 'blue' and blue > 0):
            print("Great choice! You picked " + uc + "\n")
            loop_count = 1
        elif(uc.lower() == 'yellow' and yellow > 0):
            print("Great choice! You picked " + uc + "\n")
            loop_count = 1
        else:
            print("That color is not available. Pick a different color.")

    return(uc)

def roll_red(r: int) -> int:
    """
    This function will tell the user they picked up a red fruit
    and deduct 1 from the total amount of red fruits remaining
    :param r: the current number of red fruit still in play
    :return: the new amount of red fruit remaining
    """

    if(r > 0):
        print("You picked up a red fruit")
    red = r - 1
    if (red > 1):
        print("There are now " + str(red) + " pieces of red fruit left \n")
    elif (red == 1):
        print('There is now only ' + str(red) + ' red fruit left \n')
    else:
        print("There are no more red fruits left \n")
    return(red)

def roll_green(g: int) -> int:
    """
    This function will tell the user they picked up a green fruit
    and deduct 1 from the total amount of green fruits remaining
    :param g: the current number of green fruit still in play
    :return: the new amount of green fruit remaining
    """

    if(g > 0):
        print("You picked up a green fruit")
    green = g - 1
    if (green > 1):
        print("There are now " + str(green) + " pieces of green fruit left\n")
    elif (green == 1):
        print('There is now only ' + str(green) + ' green fruit left\n')
    else:
        print("There are no more green fruits left\n")
    return(green)

def roll_blue(b: int) -> int:
    """
    This function will tell the user they picked up a blue fruit
    and deduct 1 from the total amount of blue fruits remaining
    :param b: The current number of blue fruit still in play
    :return: The new amount of blue fruit remaining
    """

    if(b > 0):
        print("You picked up a blue fruit")
    blue = b - 1
    if (blue > 1):
        print("There are now " + str(blue) + " pieces of blue fruit left\n")
    elif (blue == 1):
        print('There is now only ' + str(blue) + ' blue fruit left\n')
    else:
        print("There are no more blue fruits left\n")
    return(blue)

def roll_yellow(y: int) -> int:
    """
    This function will tell the user they picked up a yellow fruit
    and deduct 1 from the total amount of yellow fruits remaining
    :param y: the current number of yellow fruit still in play
    :return: the new amount of yellow fruit remaining
    """

    if(y > 0):
        print("You picked up a yellow fruit")
    yellow = y - 1
    if (yellow > 1):
        print("There are now " + str(yellow) + " pieces of yellow fruit left\n")
    elif (yellow == 1):
        print('There is now only ' + str(yellow) + ' yellow fruit left\n')
    else:
        print("There are no more yellow fruits left\n")
    return(yellow)


def status(r: int,g: int,b: int,y:int) -> None:
    """
    This function will provide a real-time tally of how
    many pieces of colored fruit are still available
    :param r: integer value denoting how many pieces of red fruit are available
    :param g: integer value denoting how many pieces of green fruit are available
    :param b: integer value denoting how many pieces of blue fruit are available
    :param y: integer value denoting how many pieces of yellow fruit are available
    :return: None
    """

    # string builder if there are more than 1 piece
    if(r > 1):
        red_txt = str(r) + " red fruits"
    else:
        # string builder if there is only 1 piece
        red_txt = str(r) + " red fruit"

    if(g > 1):
        green_txt = str(g) + " green fruits"
    else:
        green_txt = str(g) + " green fruit"

    if(b > 1):
        blue_txt = str(b) + " blue fruits"
    else:
        blue_txt = str(b) + " blue fruit"

    if(y > 1):
        yellow_txt = str(y) + " yellow fruits"
    else:
        yellow_txt = str(y) + " yellow fruit"

    base_txt = "Currently: "

    # combine the strings together
    print(base_txt + red_txt + ', ' + green_txt + ', ' + blue_txt + ', and ' + yellow_txt + '\n')

if __name__ == "__main__":

    # initialize the fruit pieces
    red = 4
    green = 4
    blue = 4
    yellow = 4
    raven_step = 0

    # the different face values found on the simulated dice
    faces = ['red', 'green', 'blue', 'yellow', 'raven', 'basket']

    # show the user brief instructions
    show_instructions()

    # while loop will keep running until the user quits, wins, or loses the game
    while True:
        move = input("Enter r to roll dice, s for status, i for instructions, or q to quit: ").lower()

        # while loop to make sure user enters only the valid input values
        while (move not in ['r','q','s','i']):
            print("\nInvalid move. Try again.")
            move = input("\nEnter r to roll dice, s for status, i for instructions, or q to quit: ").lower()

        # user choosing to quit game
        if(move == 'q'):
            print("\nThank you for playing!")
            break

        # user choosing to see how many pieces of fruit are still left
        if(move == 's'):
            status(r = red, g = green, b = blue, y = yellow)
            continue

        # user choosing to see the brief instructions
        if(move == 'i'):
            show_instructions()
            continue

        # user choosing to roll the dice
        if(move == 'r'):
            user_roll = roll_dice(faces)

        # the dice shows "basket" which lets the user pick whatever color they want
        if(user_roll == 'basket'):
            user_roll = basket(r = red, g = green, b = blue, y = yellow)

        # roll a red and there is more than 0 red fruits remaining
        if(user_roll == 'red' and red > 0):
            red = roll_red(r = red)

        # roll a red and there are 0 red fruits remaining
        elif(user_roll == 'red' and red == 0):
            print("There are no more red fruits to pick up! Roll Again!\n")

        # roll a green and there is more than 0 green fruits remaining
        elif(user_roll == 'green' and green > 0):
            green = roll_green(g = green)

        # roll a green and there are 0 green fruits remaining
        elif (user_roll == "green" and green == 0):
            print("There are no more greens to pick up! Roll Again!\n")

        # roll a blue and there are blue fruits remaining
        elif(user_roll == 'blue' and blue > 0):
            blue = roll_blue(b = blue)

        # roll a blue and there are no blue fruits left
        elif(user_roll == "blue" and blue == 0):
            print("There are no more blues to pick up! Roll Again!\n")

        # roll a yellow and there are yellow fruits remaining
        elif(user_roll == 'yellow' and yellow > 0):
            yellow = roll_yellow(y = yellow)

        # roll a yello and there are no yellow fruits remaining
        elif(user_roll == "yellow" and yellow == 0):
            print("There are no more yellows to pick up! Roll Again!\n")

        # action to take if the dice when rolled shows raven
        elif(user_roll == "raven"):
            raven_step = raven_step + 1
            if(raven_step == 5):
                print("The raven has found all the fruits!")
                print("="*35)
                print("You LOSE!")
                print("-"*35)
                print('GAME OVER')
                print("="*35)
                break
            else:
                print("The raven has moved closer to the fruits.")
                print("The raven only needs to move " + str(5 - raven_step) + " more step(s) before it wins!\n")

        # if the sum of all fruits remaining is equal to 0 the game is over
        if(red + green + blue + yellow == 0):
            print("\nYou collected all the fruits!")
            print("*"*35)
            print("YOU WIN!")
            print("*"*35)
            break






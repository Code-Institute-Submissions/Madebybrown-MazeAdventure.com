weapon = False


def starting_room():
    """
    Creates a loop that repeats to print the options if the users'
    input is not in directions. (Example - backward)
    """
    directions = ["left", "right", "forward"]
    print("\n ___________")
    print("\n You find yourself in the middle of a room")
    print(" There are four paths to choose from")
    print(" Where would you like to go?")
    user_input = ""

    while user_input not in directions:
        print(" Options: left | right | backward | forward")
        user_input = input()
        if user_input == "left":
            room_one()
        elif user_input == "right":
            room_four()
        elif user_input == "backward":
            print("\n You find that heavy rocks block this way")
            print(" You have to turn around and take another way.")
        elif user_input == "forward":
            room_two()
        else:
            print("\n Please enter a valid option.")


def room_one():
    """
    Creates a loop that repeats to print the options if the users'
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward"]
    print("\n ___________")
    print("\n You're walking down the tunnel when")
    print(" You suddenly hear a noise echo through the distant tunnels")
    print(" Where should you go?")
    user_input = ""

    while user_input not in directions:
        print(" Options: left | right | backward")
        user_input = input()
        if user_input == "left":
            print("\n You find that heavy rocks block this way")
            print(" You have to turn around and take another way.")
        elif user_input == "right":
            room_three()
        elif user_input == "backward":
            starting_room()
        else:
            print("\n Please enter a valid option.")


def room_two():
    """
    Creates a loop that repeats to print the options if the users'
    input is not in directions. (Example - forward)
    """
    directions = ["left", "right", "backward"]
    print("\n ___________")
    print("\n You hear strange noises")
    print(" You think you have disturbed some ancient spirit")
    print(" Where would you like to go?")
    user_input = ""

    while user_input not in directions:
        print(" Options: left | right | backward")
        user_input = input()
        if user_input == "right":
            print("\n Zombie-like creatures start emerging from the walls")
            print(" As you enter the long hall. You are killed.")
            print(" Rip " + name + "")
            play_again()
        elif user_input == "left":
            print("\n Sorry " + name + "!")
            print(" Spikes came out of the wall and killed you!")
            play_again()
        elif user_input == "backward":
            starting_room()
        else:
            print("\n Please enter a valid option.")


def room_three():
    """
    Creates a loop that repeats to print the options if the users'
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward", "up"]
    print("\n ___________")
    print("\n You see something on the floor")
    print(" It's a phone, someone must have been here recently!")
    print(" ...You hear that noise again, but this time it's closer")
    print(" Where should you go?")
    user_input = ""

    while user_input not in directions:
        print(" Options: forward | backward")
        user_input = input()
        if user_input == "forward":
            print("\n You fall into a pit of poisonous snakes")
            print(" Rip " + name + "!")
            play_again()
        elif user_input == "backward":
            print("\n Whatever made those sounds before just ran into you!")
            print(" Rip " + name + "!")
            play_again()
        elif user_input == "up":
            print("\n There's a rope hanging down from the roof")
            print(" You try to pull it..")
            print(" By accident, you find a secret passage")
            print(" Congratulations " + name + "! You've made it out!")
            play_again()
        else:
            print("\n Please enter a valid option.")


def room_four():
    """
    Creates a loop that repeats to print the options if the users'
    input is not in directions. (Example - left(Hidden weapon))
    """
    directions = ["backward", "forward"]
    global weapon
    print("\n ___________")
    print("\n You see some old scriptures on the walls to the LEFT..")
    print(" Feels like someone is watching you, where would you like to go?")
    user_input = ""

    while user_input not in directions:
        print(" Options: backward | forward")
        user_input = input()
        if user_input == "left":
            print("\n You find this way is a dead end, but wait..")
            print(" Something is shining in the dirt...")
            print(" You found a loaded gun")
            weapon = True
        elif user_input == " backward":
            starting_room()
        elif user_input == " forward":
            undead_monster()


def undead_monster():
    """
    Gives the user the ability to kill the monster with a weapon
    If they've found the hidden passage in the previous room.
    """
    actions = ["fight", "flee"]
    global weapon
    print("\n ___________")
    print("\n A strange zombie-like monster has appeared.")
    print(" You can either run or fight it.")
    print(" What would you like to do?")
    user_input = ""

    while user_input not in actions:
        print(" Options: flee | fight")
        user_input = input()
        if user_input == "fight":
            if weapon:
                print("\n You kill the zombie with the gun you found earlier.")
                print("\n After moving forward, you find one of the exits.")
                print(" Congrats " + name + "!")
                play_again()
            else:
                print("\n The zombie-like creature has killed you!")
                play_again()
        elif user_input == "flee":
            room_four()
        else:
            print("\n Please enter a valid option.")


def play_again():
    """
    Gives the user the ability to restart the game if they win or die.
    """
    options = ["y"]
    print("\n Restart the adventure?")
    user_input = ""

    while user_input not in options:
        print(" Options: y or n")
        user_input = input()
        if user_input == "y":
            starting_room()
        elif user_input == "n":
            quit()
        else:
            print("\n Please enter a valid option.")


if __name__ == "__main__":
    while True:
        print(" ____________________________")
        print("\n Welcome to Maze Adventure!")
        print("\n As an adventurer you've decided to visit the maze of Himo.")
        print(" But while inside you lose track of time")
        print(" And you find yourself lost inside of the maze.")
        print("\n You have to find a way out!")
        print(" But beware! Challenges will present themselves")
        print("\n Be on the lookout for hints")
        print(" And don't forget to look up once in a while")
        print(" You may find a way out!")
        print("\n ___________")
        print("\n What's your name?: ")
        name = input()
        print(" Good luck, " + name + ".")
        starting_room()

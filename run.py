weapon = False


def starting_room():
    """
    Creates a loop that repeats to print the options if the users
    input is not in directions. (Example - backward)
    """
    directions = ["left", "right", "forward"]
    print("\nYou find yourself in the middle of a room")
    print("There are four paths to chose from")
    print("Where would you like to go?")
    user_input = ""
    while user_input not in directions:
        print("Options: left | right | backward | forward")
        user_input = input()
        if user_input == "left":
            room_one()
        elif user_input == "right":
            room_four()
        elif user_input == "backward":
            print("\nYou find that this way is blocked by heavy rocks")
            print("You have to turn around and take another way.")
        elif user_input == "forward":
            room_two()
        else:
            print("\nPlease enter a valid option.")


def room_one():
    """
    Creates a loop that repeats to print the options if the users
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward"]
    print("\nYou're walking down the tunnel when")
    print("You suddenly hear a noise echo through the distant tunnels")
    print("Where should you go?")
    user_input = ""
    while user_input not in directions:
        print("Options: left | right | backward")
        user_input = input()
        if user_input == "left":
            print("\nYou find that this way is blocked by heavy rocks")
            print("You have to turn around and take another way.")
        elif user_input == "right":
            room_three()
        elif user_input == "backward":
            starting_room()
        else:
            print("\nPlease enter a valid option.")


def room_two():
    """
    Creates a loop that repeats to print the options if the users
    input is not in directions. (Example - forward)
    """
    directions = ["left", "right", "backward"]
    print("\nYou hear strange noises")
    print("You think you have disturbed some ancient spirit")
    print("Where would you like to go?")
    user_input = ""

    while user_input not in directions:
        print("Options: left | right | backward")
        user_input = input()
        if user_input == "right":
            print("\nZombie-like creatures start emerging from the side walls")
            print("As you enter the long hall. You are killed.")
            print("Rip " + name + "")
            print("Play Again, Y or N?")
            user_input = input()
            if user_input == "y":
                starting_room()
            else:
                quit()
        elif user_input == "left":
            print("\nCongratulations " + name + "! You made it out!")
            print("Play Again, Y or N?")
            user_input = input()
            if user_input == "y":
                starting_room()
            else:
                quit()
        elif user_input == "backward":
            starting_room()
        else:
            print("\nPlease enter a valid option.")


def room_three():
    """
    Creates a loop that repeats to print the options if the users
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward"]
    print("\nYou see something on the floor")
    print("It's an phone, someone must have been here recently!")
    print("...You hear that noise again, but this time it's closer")
    print("Where should you go?")
    user_input = ""

    while user_input not in directions:
        print("Options: forward | backward")
        user_input = input()
        if user_input == "forward":
            print("\nCongratulations " + name + "! You made it out!")
            print("Play Again, Y or N?")
            user_input = input()
            if user_input == "y":
                starting_room()
            else:
                quit()
        elif user_input == "backward":
            print("\nYou ran straight into whatever made those sounds before!")
            print("Rip " + name + "!")
            print("Play Again, Y or N?")
            user_input = input()
            if user_input == "y":
                starting_room()
            else:
                quit()
        else:
            print("\nPlease enter a valid option.")


def room_four():
    """
    Creates a loop that repeats to print the options if the users
    input is not in directions. (Example - left(Hidden weapon))
    """
    directions = ["backward", "forward"]
    global weapon
    print("\nYou see some old scriptures on the walls to the left")
    print("It feel like someone is watching you, where would you go?")
    user_input = ""

    while user_input not in directions:
        print("Options: backward | forward")
        user_input = input()
        if user_input == "left":
            print("\nYou find this way is a dead end, but wait..")
            print("Theres something shining in the dirt...")
            print("You found a loaded gun")
            weapon = True
        elif user_input == "backward":
            starting_room()
        elif user_input == "forward":
            undead_monster()


def undead_monster():
    actions = ["fight", "flee"]
    global weapon
    print("\nA strange zombie-like monster has appeared.")
    print("You can either run or fight it.")
    print("What would you like to do?")
    user_input = ""

    while user_input not in actions:
        print("Options: flee/fight")
        user_input = input()
        if user_input == "fight":
            if weapon:
                print("\nYou kill the zombie with the gun you found earlier.")
                print("\nAfter moving forward, you find one of the exits.")
                print("Congrats " + name + "!")
                print("Play Again, Y or N?")
                user_input = input()
                if user_input == "y":
                    starting_room()
                else:
                    quit()
            else:
                print("\nThe zombie-like creature has killed you!")
                print("Play Again, Y or N?")
                user_input = input()
                if user_input == "y":
                    starting_room()
                else:
                    quit()
        elif user_input == "flee":
            room_four()
        else:
            print("\nPlease enter a valid option.")


if __name__ == "__main__":
    while True:
        print("Welcome to Maze Adventure!")
        print("\nAs an adventurer you've decided to visit the maze of Himo.")
        print("But while inside you lose track of time")
        print("And you find yourself lost.")
        print("\nYou can choose to walk in multiple directions.")
        print("But beware!")
        print("Challanges will present themselves")
        print("Hope you'll find a way out!")
        print("\nWhat's your name?: ")
        name = input()
        print("Good luck, " + name + ".")
        starting_room()

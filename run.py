WEAPON = False


def starting_room():
    """
    Creates a loop that repeats to print the options if the users 
    input is not in directions. (Example - backward)
    """
    directions = ["left", "right", "forward"]
    print("\nYou find yourself in the middle of a room, there are four paths to chose from, where would you like to go?")
    user_input = ""
    
    while user_input not in directions:
        print("Options: left | right | backward | forward")
        user_input = input()
        if user_input == "left":
            roomOne()
        elif user_input == "right":
            roomFour()
        elif user_input == "backward":
            print("\nYou find that this way is blocked by heavy rocks, you have to turn around and take another way.")
        elif user_input == "forward":
            roomTwo()
        else:
            print("\nPlease enter a valid option.")


def room_one():
    """
    Creates a loop that repeats to print the options if the users 
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward"]
    print("\nYou're walking down the tunnel when \nYou suddenly hear a noise echo through the distant tunnels infront of you \nwhere should you go?")
    userInput = ""
    
    while userInput not in directions:
        print("Options: left | right | backward")
        userInput = input()
        if userInput == "left":
            print("\nYou find that this way is blocked by heavy rocks \nYou have to turn around and take another way.")
        elif userInput == "right":
            roomThree()
        elif userInput == "backward":
            startingRoom()
        else:
            print("\nPlease enter a valid option.")


def room_two():
    """
    Creates a loop that repeats to print the options if the users 
    input is not in directions. (Example - forward)
    """
    directions = ["left","right","backward"]
    print("\nYou hear strange noises. You think you have disturbed some ancient spirit. Where would you like to go?")
    userInput = ""

    while userInput not in directions:
        print("Options: left | right | backward")
        userInput = input()
        if userInput == "right":
            print("Zombie-like creatures start emerging from the sides as you enter the long hall. You are killed.")
            quit()
        elif userInput == "left":
            print("Congratulations! You made it out!")
            quit()
        elif userInput == "backward":
            startingRoom()
        else:
            print("\nPlease enter a valid option.")


def room_three():
    """
    Creates a loop that repeats to print the options if the users 
    input is not in directions. (Example - forward)
    """
    directions = ["right", "backward"]
    print("\nYou see something on the floor, \nIt's an phone, someone must have been here recently! \n...You hear that noise again, but this time it's closer, \nWhere should you go?")
    userInput = ""

    while userInput not in directions:
        print("Options: forward | backward")
        userInput = input()
        if userInput == "forward":
            print("Congratulations! You made it out!")
            quit()
        elif userInput == "backward":
            print("\nYou ran straight into whatever made those sounds before and you died!")
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
    print("\nYou see some old scriptures on the walls to the left, it feel like someone is watching you, where would you go?")
    userInput = ""

    while userInput not in directions:
        print("Options: backward | forward")
        userInput = input()
        if userInput == "left":
            print("\nYou find this way is a dead end, but wait.. theres something shining in the dirt... you found a loaded gun")
            weapon = True
        elif userInput == "backward":
            startingRoom()
        elif userInput == "forward":
            undeadMonster()


def undead_monster():
    actions = ["fight","flee"]
    global weapon
    print("\nA strange zombie-like monster has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""

    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("\nYou kill the zombie with the gun you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("\nThe zombie-like creature has killed you!")
            quit()
        elif userInput == "flee":
            roomFour()
        else:
            print("\nPlease enter a valid option.")


if __name__ == "__main__":
    while True:
        print("Welcome to Riddles Adventure!")
        print("\nAs an adventurer you've decided to visit the maze of Himoshi.")
        print("But while inside you lose track of time,\nAnd you find yourself lost.")
        print("\nYou can choose to walk in multiple directions.")
        print("But beware! \nChallanges will present themselves, Hope you'll find a way out!")
        print("\nWhat's your name?: ")
        name = input()
        print("Good luck, " + name + ".")
        startingRoom()
        break
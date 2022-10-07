# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
weapon = False

def startingRoom():
    """
    Creates a loop that repeats to print the options if the users 
    input is not in directions. (Example - backward)
    """
    directions = ["left", "right", "forward"]
    print("\nYou find yourself in the middle of a room, there are four paths to chose from, where would you like to go?")
    userInput = ""
    
    while userInput not in directions:
        print("Options: left | right | backward | forward")
        userInput = input()
        if userInput == "left":
            roomOne()
        elif userInput == "right":
            print("\nYou walk into a dark hall, and can't see the where to put your feet, you fall into a pit and die.")
            quit()
        elif userInput == "backward":
            print("\nYou find that this way is blocked by heavy rocks, you have to turn around and take another way.")
        elif userInput == "forward":
            roomTwo()
        else:
            print("Please enter a valid option.")


def roomOne():
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
            print("Please enter a valid option.")


def roomTwo():
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
            print("Please enter a valid option.")


def roomThree():
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
            print("Please enter a valid option.")


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
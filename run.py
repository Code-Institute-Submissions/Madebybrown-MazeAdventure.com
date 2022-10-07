# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def startingRoom():
    """
    Creates a loop that repeats the options if the users 
    input is not in directions. (Example - backward)
    """
    directions = ["left", "right", "forward"]
    print("\nYou find yourself in the middle of a room, there are four paths to chose from, where would you like to go?")
    userInput = ""
    
    while userInput not in directions:
        print("Options: left | right | backward | forward")
        if userInput == "left":
            riddleRoomOne()
        elif userInput == "right":
            deathRoom()
        elif userInput == "backward":
            print("You find that this way in blocked by heavy rocks, you have to turn around and take another way.")
        elif userInput == "forward":
            riddleRoomTwo()
        else:
            print("Please enter a valid option.")

# def deathRoom():

# def emptyRoom():

# def riddleRoomOne():

# def riddleRoomTwo():

# def riddleRoomThree():

# def riddleRoomFour():

# def deadEnd():

if __name__ == "__main__":
    while True:
        print("Welcome to Riddles Adventure!")
        print("\nAs an adventurer you've decided to visit the maze of Himoshi.")
        print("But while inside you lose track of time,\n and you find yourself lost.")
        print("\nYou can choose to walk in multiple directions.")
        print("But beware! \nChallanges will present themselves, Hope you'll find a way out!")
        print("What's your name?: ")
        name = input()
        print("Good luck, " + name + ".")
        startingRoom()
        break
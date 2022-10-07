# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def startingRoom():
    print("\nYou find yourself in the middle of a room, there are four paths to chose from, where would you like to go?")

def deathRoom():

def emptyRoom():

def riddleRoomOne():

def riddleRoomTwo():

def riddleRoomThree():

def riddleRoomFour():

def deadEnd():

if __name__ == "__main__":
    while True:
        print("Welcome to Riddles Adventure!")
        print("\nAs an adventurer you've decided to visit the maze of Himoshi.")
        print("But while inside you lose track of time,\n you find yourself lost.")
        print("You can choose to walk in multiple directions.")
        print("But beware! \nChallanges will present themselves, Hope you'll find a way out!")
        print("What's your name?: ")
        name = input()
        print("Good luck, " + name + ".")
        startingRoom()
        break
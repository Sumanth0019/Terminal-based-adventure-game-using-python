import random

def start_adventure():
    print("Welcome to the Galactic Exploration Adventure!")
    print("1. Land on the planet\n2. Continue exploring space")
    choice = input("Enter choice: ")
    if choice == '1':
        land_on_planet()
    elif choice == '2':
        explore_space()
    else:
        start_adventure()

def land_on_planet():
    print("1. Take the left path\n2. Take the right path")
    choice = input("Enter choice: ")
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        land_on_planet()

def explore_space():
    print("1. Communicate with the aliens\n2. Avoid the alien ship")
    choice = input("Enter choice: ")
    if choice == '1':
        communicate_with_aliens()
    elif choice == '2':
        print("You avoid the alien ship and find a hidden space station. Mission successful!")
    else:
        explore_space()

def left_path():
    print("1. Take the artifact\n2. Leave it")
    choice = input("Enter choice: ")
    if choice == '1':
        print("The artifact grants you special powers. Mission successful!")
    elif choice == '2':
        print("You find an alien civilization. Mission successful!")
    else:
        left_path()

def right_path():
    print("1. Fight the creature\n2. Run back")
    choice = input("Enter choice: ")
    if choice == '1':
        if random.choice([True, False]):
            print("You defeat the creature. Mission successful!")
        else:
            print("The creature overpowers you. Mission failed.")
    elif choice == '2':
        land_on_planet()
    else:
        right_path()

def communicate_with_aliens():
    if random.choice([True, False]):
        print("The aliens are friendly. Mission successful!")
    else:
        print("The aliens attack your ship. Mission failed.")

if __name__ == "__main__":
    start_adventure()

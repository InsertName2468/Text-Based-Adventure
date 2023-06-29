import time

def introduction():
    print("You wake up in a dimly lit room. You have no memory of how you got here.")
    time.sleep(2)
    print("As you look around, you notice an eerie silence hanging in the air.")
    time.sleep(2)
    print("There are three doors in front of you - a red door, a blue door and and a black door.")
    time.sleep(2)

def choose_door():
    choice = input("Which door do you choose? (Red/Black/Blue): ").lower()
    if choice == "red":
        red_door()
    elif choice == "black":
        black_door()

    elif choice == "blue":
        blue_door()
    else:
        print("Invalid choice. Try again.")
        choose_door()

def red_door():
    print("You open the red door and enter a dark corridor.")
    time.sleep(2)
    print("You hear faint whispers echoing through the corridor.")
    time.sleep(2)
    print("As you move forward, the whispers grow louder.")
    time.sleep(2)
    print("Suddenly, a ghostly figure appears in front of you!")
    time.sleep(2)
    print("Game Over!")
    time.sleep(2)
    quit

def black_door():
    print("You open the black door and find yourself in a room filled with mirrors.")
    time.sleep(2)
    print("Your reflection in the mirrors seems distorted and sinister.")
    time.sleep(2)
    print("You feel a chill run down your spine as you notice movement in the mirrors.")
    time.sleep(2)
    print("Your own reflection reaches out from the mirror and pulls you in!")
    time.sleep(2)
    print("Game Over!")
    time.sleep(2)
    quit

def blue_door():
    print("Cautiously, you opened the blue door, hoping there is no danger behind the door.")
    time.sleep(2)
    print("As you opened the door, you saw nothing but pitch black.")
    time.sleep(2)
    print("Suddenly the your room turned pitch black as like inside the door")
    time.sleep(2)
    print("You suddenly realised that behind the door,it's your bedroom and there is another you grinning at you then suddenly slam the door shut, leaving you in pitch blackness......")
    time.sleep(2)
    print("Game Over?")
    time.sleep(2)
    quit
    

def play_game():
    introduction()
    choose_door()

play_game()

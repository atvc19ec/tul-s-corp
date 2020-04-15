import sys
import os
import time
import pickle

# We have a title screen that the player will reach before the actual game begins.


def title_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        main()
    elif option.lower() == "help":
        helpScreen()
    elif option.lower() == "quit":
        sys.exit(0)
    while option.lower != ["play", "help", "quit"]:
        print("Option chosen is invalid")
        title_screen_selection()


def title_screen():
    print("-------------------------")
    print("| Welcome to Tul's Corp |")
    print("-------------------------")
    print("|       - Play -        |")
    print("|       - Help -        |")
    print("|       - Quit -        |")
    print("-------------------------")
    title_screen_selection()


def prelude():
    time.sleep(3)
    print("Huh?")
    time.sleep(1)
    print("We said, how would yo...")
    time.sleep(2)
    print("I...")
    print("How would you establish a database that could optimize the issues with the retrieval of data?")
    print("....")
    time.sleep(1)
    print("...I")
    time.sleep(2)
    print("I... don't know....")
    time.sleep(4)


def helpScreen():
    print("In order to play the game, you must type your choices,"
          " and in order to inspect as to what your choices are,\n"
          "You must type 'Inspect' in the action box.")
    print("\nThe actions you can perform will vary with respect to the situation you are in.")
    title_screen_selection()


def displayIntro():
    print("Having spent the past few years of yours grovelling on the ground,"
          "you end up realising that you can't live on under your dad's roof any longer."
          "\nMore like they kicked you out since you've spent way too much time and way too much wasted effort on "
          "their part. ")
    time.sleep(5)
    print("\nYou decide that you want to get out there in the professional world and actually become somebody needed."
          "\nYou also realise that you need to get your documents and your resume if you want to apply for a job, "
          "you rush back in and get your files, "
          "and manage to get out with your files, your laptop bag,"
          " and fortunately, some cash lying in the hall.\n Running from the deadly brunt of the utensils"
          " that your mom throws at you, you embark on your own business adventure,"
          " pointing at the gods that this shall be your great business story.")
    time.sleep(7)


def main():
    displayIntro()
    player_data = {"name": dataInput(), "wallet": 3000}
    pickle.dump(player_data, open("player_data", 'wb'))

    exit(0)  # for now, the game doesn't have the next stage to go to. so, it terminates here.


# not exactly sure whether or not, we should take the name of the character, instead of just going with the flow.
def dataInput():
    player_name = input("Enter the name of your character : ")
    print("This shall be the tale of {} ".format(player_name))
    return player_name


# It would be a great implementation idea, if we could manage to have a calender show up at the start of each day.
# Kinda showing how the player is progressing.


def clear():
    if os.name == 'posix':
        os.system("cls")
    else:
        os.system("clear")


# the code which runs and calls
print("Skip the prologue?")
response = input("> ")
clear()
if response.lower()[0] is 'n':
    prelude()
    clear()
title_screen()

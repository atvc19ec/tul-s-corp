import pickle
import time
import dayone
#Need to add the alert of having the day two appear
def dayexe():
    if(dayone.stay_at_hotel):
        print("You wake up feeling groggy but very comfortable, after getting up from the bed,\n you admire the view from the room"
        + " and go down to the dining section to have the first meal of the day."
        +"\nYou glance around and see the rush of the busy folk. "
        +"\nSeems like a drag.")
        time.sleep(4)
        print("Thinking about it, you too want a job.")
        print("Maybe one of these days you'll get lucky? Ah, fat chance.")
        time.sleep(6)
    else:
        print("You wake up pretty fre-... nope, the ceiling's leaking.")
        print("Well, on the bright side, your clothes seem to have dried and hot water is available.")
        time.sleep(4)
        print("You decide to get out and buy some food.")
        print('Proceeding up to the reception, you ask, "Hey, Where\'s the nearest fast food?"')
        print('"To the right, walk a bit and you\'ll find the nearest WacDonald\'s."')
        print("You mutter a thanks before leaving out the door. Almost considering never returning if it weren\'t for the laptop in the room.")
        print("You're on your way to grab a bite, when you see a car pull up to the driveway.")
        time.sleep(8)
        print("The window rolls down as your eyes widen. It's Miss Sumuri.")
        print("Those posters don't lie. You think to yourself.\nShe's Gorgeous.")
        print("You get your order and go before staring turns to gawking.")
        print("Sigh. It's another sad day with beauties walking by.")
        print("Maybe one of these days you'll get lucky? Ah, fat chance.")
        time.sleep(6)
    
    print("You return back to the room and remember about those applications you sent out last night.")
    print("You go ahead and check on whether you received a reply.")
    print("Out of the 5 big companies that you applied for, you've received a reply from three of them.")
    print('\n"WHAT"\n')
    print("It's Tul's corp.... they replied positively to your application.")
    print("You look at the other two and think about which one you're going to open first.")
    print("1. Tul's Corp\n2. Dat Tech\n3. VJB Enterprises")
    print("You go through all the responses.")
    tulsresp()
    datresp()
    vjresp()

    print("You figure that you can only go to one, considering that they all, unfortunately, take place on the same day.")

    while True:
        resp = input("> ")
        if resp.lower() is "inspect":
            print("Enter the name of the company")
        elif resp.lower()[0] is 't':
            print("You decide to take the interview of the largest in the game.\nTul's Corp.")
        elif resp.lower()[0] is 'd':
            print("You decide that Dat Tech really has the future in it's hold, being a rival to Tul's Corp.\nIt doesn't fall short of a dream company.")
        else:
            print("You decide that the other two just aren't your style. ")

def tulsresp():
    print()

def datresp():
    print()

def vjresp():
    print()

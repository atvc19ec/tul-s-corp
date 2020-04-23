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
    
    print("You return back to the room and ")

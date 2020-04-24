from time import sleep
import pickle
import os


def dayexe(path):
    db = load_data(path)
    print("Knowing the wrath that would be exhibited if you go back home without a job,"
          "\nyou come to the conclusion that you'll be needing to stay at a nearby hotel for the night.")
    sleep(3)
    print("You check your wallet for the money that you have for now."
          "\nApparently, more than you thought.")
    print("\n> Money in your wallet : {}".format(db["wallet"]))
    print("---")
    print("\nYou notice a droplet fall on your wrist, while proceeding on to the main road, as you look at your watch."
          "\nSeems to be 6 o' clock."
          "\n\nThe rain starts to pour."
          "\nYou contemplate your choice of staying at the hotel,"
          " and realise that you're already pretty much out of money."
          "\nA motel seems to be a better option."
          " You decide to flip for it, and toss a coin into the air.")
    res = input("\n\n> Do you get a heads or a tails?")

    stay_at_hotel = False
    if res.lower()[0] == 'h':
        stay_at_hotel = True
    sleep(2)
    if stay_at_hotel:
        print("You decide to go to a hotel, probably making the right choice considering the terrors of a motel."
              "\nAll those movies pretty much scarred you for life whenever you think of a motel.")
        print("Anyway, you'd probably be safer in a hotel anyway."
              "You think about the food service, the fluffy bedsheets, and the wonderful bathroom,"
              " as you get distracted by the passing cars and the traffic lights."
              "\nRight. You need to get there first.")
    else:
        print("Considering the fact that you're already out of the house,"
              " you realise that it's best to save up on your cash."
              "\nPerhaps motels aren't really as bad as they seem on the big screen."
              "\nProbably more for a dramatic effect, you take a big gulp as you look at the passing cars"
              " and the hazy traffic lights, as you lift your hand to hail a cab, ignoring the water that "
              "drenches your sleeved clothing.")
    sleep(7)
    print("Approaching your way, comes a yellow coloured cab."
          "You get in quickly in order to avoid the rain.")
    print('\nCab Driver: "Where to?"')
    if stay_at_hotel:
        print("> Botanical View")
    else:
        print("> Just get me to a motel not far from town.")
    print()
    print('Cab Driver: "Gotcha."')

    print("-" * 20)
    sleep(3)
    print("You look out the car's window as you glance at the large posters.")
    sleep(3)
    print(" What keeps you apart from one another? We have your backs.")
    sleep(3)
    print("  The runtime takes a while, but, make sure you don't!")
    sleep(3)
    print("   Half the time, Double the efficiency with our SDKs.")
    sleep(3)

    print("While the posters themselves, were of different products in the IT industry."
          "\nThere was the one factor, that all of them shared."
          "\n\nTul's Corp.\n"
          "\nA massive behemoth of a corporation."
          "\nIt started off by taking part in one of the sectors of the IT industry,"
          " and managed to branch out extensively. Ending up as the leading software development company,"
          " Tul's corp was trusted throughout as one of the largest and safest cloud computing service provider."
          "\nHaving expanded their territory into the other sectors, they created an OS that was fast, efficient and"
          " nearly took over the world by storm.")
    sleep(4)
    clear()

    if stay_at_hotel:
        print("You reach the hotel, and the cab ride costs you just as much as was expected."
              "\nYou manage to get yourself checked in, and quickly retire into your room as you fall onto the bed."
              "\nNot very graciously, but, the bed pretty much has your back.")
        print("You realise that it's a good idea to probably take a bath, the rain took quite a toll on your clothes.")
        print("Letting go of your worries for a bit, you go freshen up.")
    else:
        print("You manage to reach the motel in one piece,"
              " and the cab managed to cost you more than you expected. Nearly to the point, where you had "
              " to haggle with the driver."
              "\nYou get into the motel grumbling about the kind of choices you make for money.")
        print("The motel doesn't seem that bad...")
        sleep(3)
        print("At first.")
        sleep(2)
        print("The roof leaks, the hot water's not really hot water, in fact is that even water?"
              "\nYou resign yourself to your fate and just lie down on the bed.")
    clear()
    sleep(5)
    print("You come to a realisation that maybe, you should at least find a source of income before you doze off.")
    print("Opening up your laptop, you check up the jobs available around town, for an amazing man such as yourself.")
    sleep(4)
    print("There are none.")
    sleep(3)
    print("You decide that you might as well just start from the bottom up and go all in by applying as an intern.")
    print("You apply for a ton of available internships not knowing what offer you might get.")
    sleep(6)
    print("It's been a pretty long day.\nYou think about whether all of this is even worth the trouble.")
    sleep(4)
    print("A problem for an another day, you think to yourself.")
    print("-" * 20)
    if stay_at_hotel:
        charges = {"Cab Charges": 80, "Hotel Charges": 500}
    else:
        charges = {"Cab Charges": 100, "Hotel Charges": 200}
    stats = day_budget(db, charges)
    return stats


def load_data(path):
    stats = open(path, 'rb')
    db = pickle.load(stats)
    for name in db:
        print(name, '=>', stats)
    stats.close()
    return db


def day_budget(db, charges):
    print(str(db))  # To test whether the file is correct. Cannot check directly since the format is not supported.
    for i in range(len(db)):
        db["wallet"] -= (charges["Cab Charges"] + charges["Hotel Charges"])
    return db


def clear():
    if os.name == 'posix':
        os.system('cls')
    else:
        os.system('clear')

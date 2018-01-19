import time

AY = "You are the daughter of the Headmaster. You are in danger. They want to find you."
AYstatus = "You are scared. What is happening?"
hp = 10
ep = 10
AYHP = str(hp)
AYEP = str(ep)
AYstats = {"health": (AYHP + "/10"),"energy": (AYEP + "/10")}
ANTIMONY = {"who am i?": AY, "status": AYstatus, "stats": AYstats}
fruit_snacks = {"description": "Delicious, gummy fruit snacks. Your mother disapproves of these but they fill you up well. \n (Restores 3 HP, Restore 2 EP)\n", "quantity": 3}
crackers = {"description": "Whole wheat crackers with nuts that are pretty bland...\n (Restores 5 HP, Restores 5 EP)", "quantity": 1}
thimble = {"description": "Thimble is your best stuffed bear friend and is very large. Sometimes you use him as a pillow.", "quantity":1}
mittens = {"description":"large, leather mittens ready to protect your hands from the sharp, hot, and cold", "quantity": 1}
BACKPACK = {"fruit snacks":fruit_snacks, "crackers": crackers, "Thimble": thimble,"mittens": mittens}


the_beginning = ['''Your mother and you are sitting in the back seat of a limousine. You have been flying in an airplane from California for over 5 hours.''',
"Coming from the airport to visit your father, the limousine is approaching the academy your father is principal of",
"and you are excited, as you haven't seen him in such a long time. You are currently looking at the flora and fauna",
"of the forest creeping over the path the limousine slowly drives over. The sky is fading into twilight and the stars are stifiled by the clouds.",
" ", "The air is cold."]
the_crisis = '''You see smoke rising in the distance from where your father's academy is...\n
your mother is distracted, talking on the phone about some business. '''
transition1 = ["Your vision is clouded by the contorting of metal",
"and rush of colors and fire. It blackens but",
"as soon as the limousine teeters to a stop...your eyes widen in fear."]

def death():
    print("You are dead.")
    time.sleep(5)
    print("What did I even expect from you?")
    time.sleep(4)
    exit()

print('Season: Summer \nMonth: June \nWho are you: Antimony A. \nHow old Are you: 4 years old\n')

time.sleep(4)
ready = input("Ready?").lower()
fire_list = ["You turn to your mother and tell her of the fire.", "The smoke starts to thicken.", "It grows.", "Your mother stops talking on the phone and looks up to see the dark cloud forming."]

if ready == "no":
    death()

if ready == "yes":
    x = 0
    y = 0
    while y <= 5:
        print(the_beginning[y])
        time.sleep(4)
        y = y+ 1
    print(the_crisis)
    fire = input("Do you say something about the smoke? (Yes/No)").lower()
    if fire == "yes":
        print(fire_list[x])
        time.sleep(4)
        print("Your mother looks up. A firey force slams into the limousine and drives the top of the hood to the ground.")
    while fire == "no":
        x = x+1
        if x == 4:
            break
        else:
            print(fire_list[x])
            fire = input("Do you say something about the smoke? (Yes/No)").lower()
            if fire == "yes" or "no":
                print("It's too late. Your mother looks up. A firey force slams into the limousine and drives the top of the hood to the ground.")
time.sleep(4)
ask1 = input("Continue?")
if ask1 == "yes":
    x = 0
    while x <= 2:
        print(transition1[x])
        time.sleep(4)
        x = x+1
    print("You find your body hanging onto the safety of your seatbelt. The car is turned over, so you are hanging upside down in the ruins of the car. Your mother is unconcious.")
    time.sleep(2)
    print("You smell gas and a fire is dangerously close to the front of the totaled car...")
if ask1 == "no":
    death()

ask2 = input("What would you like to do?").lower()
if ask2 == "observe" or "look around" or "search the car" or "search" or "look":
    print("You see a lot of glass on the ceiling of the car. You know you're going to cut yourself. Your backpack is on the floor within arm's reach.")
    ask3 = input("What would you like to do?").lower()
    if ask3 == "get backpack" or "backpack" or "grab backpack" or "pick up backpack":
        print("You have picked up your BACKPACK! A tad ratty, pink, and reliable backpack of yours. It holds all you prepared to spend the weekend with your father!")
if ask2 == "unclip seatbelt" or "take off seatbelt" or "seatbelt" or "get out":
    print("You unclip the seatbelt and you fall unprotected into the broken glass. You find your wrist has been slit.")
    time.sleep(2)
    print("You vision begins to fade. You heart beat quickens. You begin to bleed.")
    time.sleep(2)
    print("You're tired....so tired.")
    time.sleep(1)
    print("You collapse onto the ground.")
    death()















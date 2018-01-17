import time

ANTIMONY = {"who am i?": AY, "status": AYstatus, "stats": AYstats}
AY = "You are the daughter of the Headmaster. You are in danger. They want to find you."
AYstatus = "You are scared. What is happening?"
AYstats = {"health": AYHP + "/10","energy": AYEP + "/10"}
BACKPACK = {"fruit snacks":fruit_snacks, "crackers": crackers, "Thimble": thimble, "pajamas": pjs, "mittens": mittens, "hat":hat, "toothbrush":toothbrush}
fruit_snacks = dir(description: "Delicious, gummy fruit snacks. Your mother disapproves of these but they fill you up well. \n (Restores 3 HP, Restore 2 EP)\n", quantity: 3)
crackers = {description: "Whole wheat crackers with nuts that are pretty bland...\n (Restores 5 HP, Restores 5 EP)", quantity: 1}

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
            if fire == "yes":
                print("It was too late. Your mother looks up. A firey force slams into the limousine and drives the top of the hood to the ground.")
                print(" ")
time.sleep(4)
ask1 = input("Continue?")
if ask1 == "yes":
    x = 0
    while x <= 2:
        print(transition1[x])
        time.sleep(4)
        x = x+1
if ask1 == "no":
    death()















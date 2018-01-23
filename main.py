#to use the time library, import time
import time

#create fire_game list to create not a time constraint, but choice constraint
fire_game = ["The fire at the front of the car burns.", "The fire crawls over to the front window", "You hear a clicking noise. THE LIMOUSINE EXPLODES."]
#the bottom lines were created if game is progressed further after the semester
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

#scripts created as variable to keep coding clean and control the timing of lines - to be more user friendly
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

#function death to end game if player fails
def death():
    print("You are dead.")
    time.sleep(5)
    print("What did I even expect from you?")
    time.sleep(4)
    exit()

#establishes setting
print('Season: Summer \nMonth: June \nWho are you: Antimony A. \nHow old Are you: 4 years old\n')
#sleep functions will be used to break up lines
time.sleep(4)
#inputs will be used through out for choices and to dictate events, function lower is used to prevent breaking
ready = input("Ready? (Type 'yes' or 'no')   ").lower()
#initial fire_list to lead player to first actual event of the game
fire_list = ["You turn to your mother and tell her of the fire.", "The smoke starts to thicken.", "It grows.", "Your mother stops talking on the phone and looks up to see the dark cloud forming."]

#player must continue and drive events without quitting or else they lose
if ready == "no":
    death()
#any other answers can be used to continue events despite not being 'yes'
if ready != "no":
    x = 0
    y = 0
    #begins looping for timing of scripts
    while y <= 5:
        print(the_beginning[y])
        time.sleep(4)
        y = y+ 1
    #establishes the first problem
    print(the_crisis)
    #this section was intended to make the user not willing to play or wanting to stay put
    #gradually more uncomfortable and forced to make a choice - if game expanded, choices will result in point values and changes of events
    fire = input("Do you say something about the smoke? (Yes/No)   ").lower()
    #the choice if they wish to continue events
    if fire == "yes":
        print(fire_list[x])
        time.sleep(4)
        print("Your mother looks up. A firey force slams into the limousine and drives the top of the hood to the ground.")
    #if events are not driven by the player
    while fire == "no":
        x = x+1
        if x == 4:
            break
        else:
            print(fire_list[x])
            fire = input("Do you say something about the smoke? (Yes/No)   ").lower()
            if fire == "yes" or "no":
                print("It's too late. Your mother looks up. A firey force slams into the limousine and drives the top of the hood to the ground.")
time.sleep(4)
#if they say no to continuing, they die
ask1 = input("Continue (Yes or No)?   ")
#below is if they say yes
if ask1 == "yes":
    x = 0
    while x <= 2:
        print(transition1[x])
        time.sleep(4)
        x = x+1
    #establishes main puzzle
    print("You find your body hanging onto the safety of your seatbelt. The car is turned over, so you are hanging upside down in the ruins of the car. Your mother is unconcious.")
    time.sleep(2)
    print("You smell gas and a fire is dangerously close to the front of the totaled car...")

if ask1 == "no":
    death()
#hints player to act, either to observe first or unclip their seatbelt
ask2 = input("What would you like to do? (Hint: can you see anything?)   ").lower()
if ask2 == "observe" or "look around" or "search the car" or "search" or "look":
    print("You see a lot of glass on the ceiling of the car. You know you're going to cut yourself. Your backpack is on the floor within arm's reach.")
else:
    print("You unclip the seatbelt and you fall unprotected into the broken glass. You find your wrist has been slit.")
    time.sleep(2)
    print("You vision begins to fade. You heart beat quickens. You begin to bleed.")
    time.sleep(2)
    print("You're tired....so tired.")
    time.sleep(1)
    print("You collapse onto the ground.")
    death()
#next action to be made: to grab and use the backpack, otherwise, the player will die
ask3 = input("What would you like to do? (Hint: Interact with your surroundings.)   ").lower()
t = 0
if ask3 == "get backpack" or "backpack" or "grab backpack" or "pick up backpack":
    print("You have picked up your BACKPACK! A tad ratty, pink, and reliable backpack of yours. It holds all you prepared to spend the weekend with your father!")
    ask4 = input("Open backpack? (yes/no)").lower()
    if ask4 == "yes":
        print("You have fruit snacks,crackers,Thimble,a pillow, and mittens")
    if ask4 == "no":
        print(fire_game[t])
        t = t +1
    ask5 = input("Use pillow? (y/n)").lower()
    if ask5 == "yes":
        print("You place the pillow on the ceiling.")
        ask6 = input("What would you like to do? (Hint: the seatbelt)")
        if ask6 == "seatbelt" or "remove seatbelt" or "unclip seatbelt":
            print("You fall down safely into the pillow. It shreds a little but you are safe.")
    if ask5 != "yes":
        death()
if ask3 != "get backpack" or "backpack" or "grab backpack" or "pick up backpack":
    print(fire_game[t])
    t = t +1

print("You have successfully escaped and survived the tutorial! Thanks for playing!")










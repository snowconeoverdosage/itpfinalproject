import time


def death():
    print("You are dead.")
    time.sleep(5)
    print("What did I even expect from you?")
    time.sleep(1)
    exit()

print('Season: Summer \n Month: June \n Who are you: Antimony Agnihotri \n How old Are you: 4 \n')
ready = input("Ready?").lower()

the_beginning = '''Your mother and you are sitting in the back seat of a limousine. You have been flying for over 5 hours. \n
Coming from California to visit your father, the limousine is approaching the academy your father is principal of \n
and you are excited, as you haven't seen him in such a long time. You are currently looking at the flora and fauna \n
of the forest creeping over the path the limousine slowly drives over. The sky is fading into twilight and the stars \n
are stifiled by the clouds.
'''
the_crisis = ''' You see smoke rising in the distance...your mother is distracted, talking on the phone about some business. '''


if ready == "yes":
    print(the_beginning)
    time.sleep(6)
    print(the_crisis)
    time.sleep(5)
    fire = input(Tell your mother about the smoke.)
    if
if ready == "no":
    death()

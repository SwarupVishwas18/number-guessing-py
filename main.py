import random
import time
print("NUMBER GUESSING GAME")
name = input("Enter your name : ")
time.sleep(2)
print(f"Hey {name}, I am Half Blood Prince, Host of this amazing game..!!")
print("Rules are simple :-")
print("I'll think about the number and you will guess it")
print("You have 6 chances, so play safely")
print("If you guess number larger than mine then you are HOT..!!")
print("If low, you are COLD..!!")
print("And if you are correct then you are BULLSEYE..!!")
print("And Number will be from 1-25... So all the best..!!")
time.sleep(2)
rnd = 1

results = {}


def quit_prompt(rnd):
    yn = input("\n\nDo you want to continue , Y/N ? ")
    if yn.upper() == 'Y':
        rnd += 1

        print("\n####################################################################")
        print("-----------------------REFRESHING TABLES----------------------------")
        print(
            f":::::::::::::::::::::::::: ROUND {rnd} ::::::::::::::::::::::::::: ")
        print("####################################################################\n")
        time.sleep(3)
        return rnd, True
    else:
        time.sleep(2)
        print(f"\n{name} Your result is --->>>")
        for key, val in results.items():
            print(f"\n\nROUND {key} = {val}")
            time.sleep(1)
        print("Thank You..!!")
        print("Created By Swarup Deepak Vishwas..!!")
        time.sleep(10)
        return rnd, False


control = True

while control:
    guess_count = 0
    print("\n\nI have guessed number between 1-25")
    ai_number = random.randint(1, 25)
    while guess_count < 6:
        guessed_number = int(input("\nYour guess is : "))

        if guessed_number == ai_number:
            print("\nYOU ARE BULLSEYE..!!")
            results[rnd] = "W O N . . ! !"
            rnd, control = quit_prompt(rnd)

            guess_count = 10

        elif guessed_number < ai_number:
            print("\nYOU ARE COLD..!!")
            guess_count += 1
        else:
            print("\nYOU ARE HOT..!!")
            guess_count += 1

        if guess_count >= 6 and not(guess_count > 8):
            print("\n\nYou have completed all the chances, So you have failed")
            results[rnd] = "L O S T . . ! !"
            rnd, control = quit_prompt(rnd)
            guess_count = 10

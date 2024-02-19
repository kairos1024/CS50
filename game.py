# Import random
import random
# Have the user input a level(the highest number that can be selected/randomized)
# Reprompt incase of vaule errors
while True:
    try:
        level=int(input("Level: "))
    except ValueError:
        continue
    if level <=0:
        continue

    r = random.randint(1, level)
    break
# Have the user guess the number that was randomly generated
# Reprompt incase of vaule errors(if the number was too high or too low)
while True:
    try:
     guess=int(input("Guess: "))
    except ValueError:
     continue

    if guess < r:
        print("Too small!")
    elif guess > r:
        print("Too large!")
    else:
         print("Just right!")
         break













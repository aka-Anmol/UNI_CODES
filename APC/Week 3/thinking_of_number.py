import random

tries = 1

#thinking of the number
number = random.randint(1, 20)
guess = int(input("Think of a number between 1 and 20: "))

while number != guess:
    
    tries += 1
    
    if guess > number:
        print("Too high")
    elif guess< number:
        print("too low")
        

    guess = int(input("Guess again:  "))

print(f"WELL DONE!!! You have guessed the number in {tries} tries")

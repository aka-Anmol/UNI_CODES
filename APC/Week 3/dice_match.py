import random

throws = 0
dice_pair = False


 
while dice_pair == False :

    # throw the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print(f"Throw {dice1} and {dice2}")

    throws += 1

    if dice1 == dice2:
        print(f' It took {throws} throws to get {dice1} for both the dice')
        
        dice_pair = True
        

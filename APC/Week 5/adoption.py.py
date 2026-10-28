#Adoption center program using dictionaries

pets = {}
action = input("'a', 'f', 'c', 'r', 'l', or 'e'? ")

while action != "e":
    pet = None
    if action == "a":
        print("add ")
        name = input("Enter name: ")
        
        for animal in pets:                  #pet and animal are like the key and the species is the value
            if animal == name:
                pet = animal
                
        if pet is not None:
            print(f"{name} is already in the centre")
        else:
            species = input("Enter the species: ")
            pets[name] = species
            print(f"{name} joined the centre")
        
    elif action == "f":
        print("find")
        name = input("Enter name you want to find: ")
        if name in pets:
            print(f"{name} is in the centre and it's species is : {species}")
        else:
            print(f"{name} is not in the centre")
        
    elif action == "c":
        print("check")
        name = input("Which pet are we looking for today? ")
        if name in pets:
            print(f"{name} is available for adoption and it's species is : {species}")
        else:
            print(f"{name} is not available")
        
        
    elif action == "r":
        print("remove")
        name = input("Which pet are we adopting? ")
        if name in pets:
            print(f"{name} is no longer available for adoption and it's species is : {species}")
            del pets[name]
            print(pets.items())
        else:
            print(f"{name} is not in the centre ")
        
    elif action == "l":
        print("list")
        print(pets.items())
        
    else:
        print("Invalid action - try again")
    action = input("'a', 'f', 'c', 'r', 'l', or 'e'? ")


#if action == "a":
#     name = input("Enter name: ")
#     for animal in pets:
#        if animal == name:
#            pet = animal
#
#        if pet is not None:
#            print(f"{name} is already in the centre")
#        else:
#            species = input("Enter the species: ")
#            pets[name] = species
#            print(f"{name} joined the centre")



    






       
                
        

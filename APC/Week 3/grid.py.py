#output grid of asterisks

width = int(input("Enter Width: " ))
height = int(input("Enter Height: " ))

for row in range(width):
    for column in range(height):
        print("*", end = " ")   
    print() 

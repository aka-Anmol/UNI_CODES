# initialising a list called all
all = [3, -7, 0, 1, -2, 9, -5]
print(all)

pos = []
neg = []

for number in all:
    if number > 0:
        pos.append(number)

    elif number < 0:
        neg.append(number)
      
    else:
        print("zero is not a positive or negative integer")


print(neg)
print(pos)

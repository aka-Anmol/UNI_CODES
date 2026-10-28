#Get the temperature of the water
temp = int(input("Entre the temperature of the water in degree Celcius: "))

#output the state of the water
if temp >= 100:
    print("The state is gas")
elif temp >= 1:
    print("The state is liquid")
else:
    temp <= 0
    print("The state is solid")
    

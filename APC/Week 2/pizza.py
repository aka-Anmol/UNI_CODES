#pizza type
total = 8
pizza = input("Do you want all the toppings on your pizza? ")
if pizza == "yes":
     print("The cost of your pizza with all the toppings is £14.00")

if pizza == "no":
    print("The cost of your no toppings pizza is £8.00")

if pizza == "no":
    mushrooms =  input("Do you wnat to add mushrooms? ")
    if mushrooms == "yes":
         print("The cost is +£1.00")
         total = total+1

    bacon = input("Do you wnat to add bacon? ")
    if bacon == "yes":
        print("The cost is +£1.50")
        total = total+1.50

    pepperoni = input("Do you wnat to add pepperoni? ")
    if pepperoni == "yes":
       print("The cost is +£1.50")
       total = total+1.50

    meetballs = input("Do you wnat to add  meatballs? ")
    if  meetballs == "yes":
         print("The cost is +£2.00")
         total = total+2
    print(f'Your total for the pizza is {total} pounds')
  

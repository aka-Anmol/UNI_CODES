valid = True

#basic store inventory

#get details
name = input("Enter product name: ")
id = input("Enter product id: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product stock quantity: "))

#validation
if price < 0:
    print("Price must be atleast zero")
    valid = False

if quantity < 0:
    print("Quantity must be atleast zero")
    valid = False

if quantity < 5:
    print("Warning: low in stock")


if valid:
    #calculate stock value
    stock_value = price * quantity

    #print stock value
    print(f"Product: {name}, ID: {id}, Price: £{price:.2f}, Quantity: {quantity}, Stock value: £{stock_value:.2f}")#for the 2 siffigs add .2f
else:
    print("One or more inputs invalid")

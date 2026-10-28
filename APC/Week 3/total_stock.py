#store inventory with validation

stock_count = 0
stock_total = 0
more_records = input("Do you want to input a stock records?")

while more_records == "yes":
    
    #get details
    name = input("Enter product name: ")
    id = input("Enter product id: ")

    price = float(input("Enter product price: "))
    quantity = int(input("Enter product stock quantity: "))

    valid = True

    if price < 0:
        print("Price cannot be negative")
        valid = False

    if quantity < 0:
        print("Quantity cannot be negative")
        valid = False    

    #calculate stock value
    if valid:    
        stock_value = price * quantity
        stock_total = stock_total + stock_value
        stock_count += 1

        #print stock value
        print(f"Product: {name}, ID: {id}, Price: £{price:.2f}, Quantity: {quantity}, Stock value: £{stock_value:.2f}")

        if quantity < 5:
            print("Low stock")

    more_records = input("Do you want to input another stock record?")

print(f"The total stock value is: £{stock_total:.2f}")


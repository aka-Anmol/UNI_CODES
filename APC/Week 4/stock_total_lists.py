# store inventory - extended for multiple records
total_stock_value = 0
more_stock = input("Do you want to add stock records? : ")
records = []

while more_stock == "yes":
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
        
    # calculate stock value
    if valid:
        stock_value = price * quantity
        
        # Make a touple, and add it to the records list
        record = (name, id, price, quantity, stock_value)
        records.append(record)

        total_stock_value += stock_value
        
        #print(f"Product: {name}, ID: {id}, Price: £{price:.2f}, Quantity: {quantity}, Stock value: £{stock_value:.2f}")

        if quantity < 5:
            print("Low stock")
    else:
        print("Invalid data - record not included in totals")

    # ask for next record
    more_stock = input("\nDo you want to add more records? ")

# output all products
for record in records:
    name, id, price, quantity, stock_value = record
    print(f"Product: {name}, ID: {id}, Price: £{price:.2f}, Quantity: {quantity}, stock_value: £{stock_value:.2f}")
    
# output total value
print(f"\nTotal stock value for all valid products: £{total_stock_value:.2f}")

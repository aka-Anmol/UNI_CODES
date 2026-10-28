#input stock records

#get details
name = input("Enter the product name: ")
product_id = input("Enter the product ID: ")
price = float(input("Enter the price per item: "))
quantity = int(input("Enter the qunatity in stock: "))

#calculate stock value

stock_value = price * quantity

#output the stock value
print(f"{name} (Product ID: {product_id}) has the stock value of {stock_value: .2f}")

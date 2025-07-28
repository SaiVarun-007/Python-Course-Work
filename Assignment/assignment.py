# Zomato Membership Product Information System

# Task 1: Take Product Details as Input

# Taking unique product ID from user as integer
product_id = int(input("Enter Product ID: "))

# Taking product name from user as string
product_name = input("Enter Product Name: ")

# Taking product price as a float
price = float(input("Enter Price: "))

# Taking multiple categories as a comma-separated string and converting to list
categories = input("Enter Categories (comma-separated): ").split(',')

# Taking stock information - available and sold - as integers
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))

# Creating a tuple to hold stock details
stock_details = (available_stock, sold_stock)

# Taking discount percentage and storing as float
discount_percentage = float(input("Enter Discount Percentage: "))

# Taking product features, splitting by comma, converting to a set to ensure uniqueness
features = set(input("Enter Product Features (comma-separated): ").split(','))

# Taking supplier name, contact, and location
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

# Creating a dictionary to hold supplier details
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

# Task 2: Display Product Details Using Different Formatting Methods

# 1. Using Comma Separation (sep=',')
# Prints product ID, name, and price separated by commas using the sep argument
print("\n1. Using Comma Separation:")
print("Product ID, Name, Price:", product_id, product_name, price, sep=',')

# 2. Using Percentage Formatting (% operator)
# Displays discount formatted to two decimal places using old-style % formatting
print("\n2. Using Percentage Formatting:")
print("Product Discount: %.2f%%" % discount_percentage)

# 3. Using f-strings (f"")
# Displays product info using modern f-string formatting
print("\n3. Using f-strings:")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price:.2f}")  # ₹ symbol and formatting price to 2 decimal places
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")  # Accessing first value from tuple

# 4. Using .format() method
# Displaying supplier details using the .format() string method
print("\n4. Using .format() method:")
print("Supplier Details: Name - {0}, Contact - {1}, Location - {2}".format(
    supplier_details["Name"], supplier_details["Contact"], supplier_details["Location"]))

# Displaying Additional Details for completeness
# Showing categories list, features set, and stock tuple
print("\nAdditional Details:")
print(f"Categories: {categories}")
print(f"Features: {features}")
print(f"Stock Details (Available, Sold): {stock_details}")

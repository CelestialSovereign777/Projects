import os
import datetime

#Class to create a menu of infinite items
class Menu():
   def __init__(self, *args):
      self.options = args

   def display(self): #Display the menu
      for i, option in enumerate(self.options, 1):
         print(f"{i}. {option}")

# Initialize variables
tables = []
total_sales = 0

# Define the Waiter class to store waiter information
class Waiter:
    def __init__(self, name, password):
        self.name = name
        self.password = password

# Define the Table class to store table information
class Table:
    def __init__(self, number, waiter, customers=0):
        self.number = number
        self.waiter = waiter
        self.customers = customers
        self.orders = []

# Define the MenuItem class to store menu item information
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Read login credentials from Login.txt and create waiter objects
waiters = []
with open("Login.txt", "r") as login_file:
    for line in login_file:
        name, password = line.strip().split(",")
        waiters.append(Waiter(name, password))

# Read menu items from Stock.txt and create menu item objects
menu = []
with open("Stock.txt", "r") as stock_file:
    for line in stock_file:
        name, price = line.strip().split(",")
        menu.append(MenuItem(name, int(price)))

# Function to validate login credentials
def validate_login(username, password):
    for waiter in waiters:
        if waiter.name == username and waiter.password == password:
            return waiter
    return None

# Function to display the main menu options
def display_menu():
    print("Main Menu:")
    print("1. Assign Table")
    print("2. Change customers")
    print("3. Add to Order")
    print("4. Prepare bill")
    print("5. Complete Sale")
    print("6. Cash up")
    print("0. Log Out")

# Function to assign a table to a waiter
def assign_table(waiter):
    table_number = int(input("Enter table number: "))
    for table in tables:
        if table.number == table_number:
            print("Table already assigned to", table.waiter.name)
            return
    customers = int(input("Enter number of customers: "))
    tables.append(Table(table_number, waiter, customers))
    print("Table", table_number, "assigned to", waiter.name)

# Function to change the number of customers at a table
def change_customers(waiter):
    table_number = int(input("Enter table number: "))
    for table in tables:
        if table.number == table_number and table.waiter == waiter:
            table.customers = int(input("Enter number of customers: "))
            return
    print("Invalid table number or not assigned to current waiter")

# Function to add an order to a table
def add_to_order(waiter):
    table_number = int(input("Enter table number: "))
    for table in tables:
        if table.number == table_number and table.waiter == waiter:
            while True:
                print("Menu Items:")
                for index, item in enumerate(menu, start=1):
                    print(index, item.name)
                choice = int(input("Enter menu item number (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(menu):
                    quantity = int(input("Enter quantity: "))
                    table.orders.append((menu[choice - 1], quantity))
                    print("Order added")
                else:
                    print("Invalid menu item number")
            return
    print("Invalid table number or not assigned to current waiter")

# Function to prepare and display the bill for a table
def prepare_bill(table):
    print("-" * 72)
    print(f"The bill of table {table.number}:\n")
    print("{:<30s}{:<20s}{:<20s}".format("Item", "Quantity", "Price"))
    total_order_price = 0
    for item, quantity in table.orders:
        price = item.price
        item_total = price * quantity
        total_order_price += item_total
        print("{:<30s}{:<20d}R{:<20d}".format(item.name, quantity, item_total))
    
    print("\nThe total of your order was R", total_order_price)
    print("You were helped by", table.waiter.name)
    print("-" * 72)

    filename = f"{table.waiter.name}-{datetime.datetime.now()}" # Gives file a unique name
    with open(filename, "w") as file:
        file.write("-" * 72 + "\n")
        file.write(f"The bill of table {table.number}:\n\n")
        file.write("{:<30s}{:<20s}{:<20s}\n".format("Item", "Quantity", "Price"))
        for item, quantity in table.orders:
            price = item.price
            item_total = price * quantity
            file.write("{:<30s}{:<20d}R{:<20d}\n".format(item.name, quantity, item_total))
        file.write("\n")
        file.write("The total of your order was R {}\n".format(total_order_price))
        file.write("You were helped by {}\n".format(table.waiter.name))
        file.write("-" * 72 + "\n")

    print("Bill saved to", filename)

# Function to complete a sale for a table
def complete_sale(waiter, total_sales):
    table_number = int(input("Enter table number: "))
    for table in tables:
        if table.number == table_number and table.waiter == waiter:
            if table.orders:
                print("Sale completed")
                total_sale = sum(item.price * quantity for item, quantity in table.orders)
                total_sales += total_sale  # Increment total_sales
                table.orders = []
                table.customers = 0
                tables.remove(table)
                return total_sales
            else:
                print("No orders to complete sale")
                return total_sales
    print("Invalid table number or not assigned to current waiter")
    return total_sales

# Function to display the total sales and clear the daily total
def cash_up():
    global total_sales
    print("Total Sales:", total_sales)
    clear_total = input("Clear daily total? (yes/no): ")
    if clear_total.lower() == "yes":
        total_sales = 0

# Function to validate login credentials
def validate_login(username, password):
    with open("Login.txt") as login_file:
        for line in login_file:
            line = line.strip()
            if line:
                stored_username, stored_password = line.split(",")
                if username == stored_username and password == stored_password:
                    return Waiter(username, password)
    return None

loginMenu = Menu("Login", "Exit")
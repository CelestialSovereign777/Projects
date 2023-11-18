from PointOfSaleClasses import *

# Initialize variables
tables = []
total_sales = 0

try:
    # Login process
    current_waiter = None
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console
        print("Welcome to Highlands Cafe\n")
        loginMenu.display()
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            current_waiter = validate_login(username, password)
            if current_waiter is None:
                print("Invalid username or password")
            else:
                break
        elif choice == "2":
            current_waiter = None
            break
        else:
            print("Invalid choice")

    # Main program loop
    while current_waiter is not None:
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console
        print("Logged in as:", current_waiter.name)
        print("Available Tables:")
        if tables:
            for table in tables:
                print("Table", table.number)
        else:
            print("No tables available")

        # Print assigned tables for the current waiter
        print("\nAssigned Tables:")
        assigned_tables = [table for table in tables if table.waiter == current_waiter]
        if assigned_tables:
            for table in assigned_tables:
                print("Table", table.number)
        else:
            print("No tables assigned to", current_waiter.name)

            display_menu()# Display the option menu
            choice = input("Enter your choice: ")
            if choice == "1": #Options for job execution
                assign_table(current_waiter)
            elif choice == "2":
                change_customers(current_waiter)
            elif choice == "3":
                add_to_order(current_waiter)
            elif choice == "4":
                prepare_bill(current_waiter)
            elif choice == "5":
                total_sales = complete_sale(current_waiter, total_sales)
            elif choice == "6":
                cash_up()
            elif choice == "0":
                current_waiter = None
                tables.clear()
                print("Logged out")
            else:
                print("Invalid choice")
            input("Press Enter to continue...")

except ValueError: #Catches most common error when runniing program
    print("Please enter a valid option")
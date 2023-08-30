class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Property:
    def __init__(self, name, purchase_price):
        self.name = name
        self.purchase_price = purchase_price
        self.expenses = []
        self.incomes = []
        self.roi = None

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def calculate_roi(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        total_incomes = sum(income.amount for income in self.incomes)
        self.roi = ((total_incomes - total_expenses) / self.purchase_price) * 100

class User:
    def __init__(self, username):
        self.username = username
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

def roi_calc():
    users = []
    while True:
        print("\nWelcome to ROI Calculator! Please choose from the following options:")
        print("Select 1 to: Create User")
        print("Select 2 to: Add Property to User")
        print("Select 3 to: Add Expense to Property")
        print("Select 4 to: Add Income to Property")
        print("Select 5 to: Calculate ROI for Property")
        print("Select 6 to: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            user = User(username)
            users.append(user)
            print(f"User {username} created.")
            
        elif choice == "2":
            username = input("Enter username: ")
            user = find_user(username, users)
            
            if user:
                property_name = input("Enter property name: ")
                purchase_price = float(input("Enter purchase price: "))
                property = Property(property_name, purchase_price)
                user.add_property(property)
                print(f"Property {property_name} added to {username}'s portfolio.")
            else:
                print("User not found.")
                
        elif choice == "3":
            property_name = input("Enter property name: ")
            user, property = find_user_property(property_name, users)
            if user and property:
                expense_name = input("Enter expense name: ")
                expense_amount = float(input("Enter expense amount: "))
                expense = Expense(expense_name, expense_amount)
                property.add_expense(expense)
                print(f"Expense {expense_name} added to {property_name}.")
            else:
                print("User or property not found.")
                
        elif choice == "4":
            property_name = input("Enter property name: ")
            user, property = find_user_property(property_name, users)
            if user and property:
                income_name = input("Enter income name: ")
                income_amount = float(input("Enter income amount: "))
                income = Income(income_name, income_amount)
                property.add_income(income)
                print(f"Income {income_name} added to {property_name}.")
            else:
                print("User or property not found.")
                
        elif choice == "5":
            property_name = input("Enter property name: ")
            print("Sorry, we are still working on our ROI Algorithm, please check back soon!")
            #user, property = find_user_and_property(property_name, users)
            #if user and property:
            #    property.calculate_roi()
            #else:
            #    print("User or property not found.")
            break
            
        elif choice == "6":
            print("Thank you for using ROI Calculator!")
            break
        else:
            print("Invalid choice. Please select a number from 1-6.")

def find_user(username, users):
    for user in users:
        if user.username == username:
            return user
    return None

def find_user_property(property_name, users):
    for user in users:
        for property in user.properties:  # rework this double for loop
            if property.name == property_name:
                return user, property
    return None, None



roi_calc()
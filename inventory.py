#This program  will read from the text file inventory.txt and perform the following on the data, 
# to prepare for presentation to managers.

from tabulate import tabulate

class Shoe:
    def __init__(self, country, code, product, cost, quantity):                                          # Created a constructor to initialize variables.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):                                                                                  #  Created a method to get cost of shoes.
        """Returns the cost of the shoes. """
        return self.cost

    def get_quantity(self):                                                                              #  Created a method to get quantity of shoes.
        """Returns the quantity of the shoes."""
        return self.quantity

    def __str__(self):                                                                                   # Created a method  for string represantation of a class.
        """returns a string representation of a class."""
        return f"{self.code}: {self.product}, {self.quantity} available at {self.cost} each"

#=============Shoe list===========

shoes_list = []                                                                                          # The list will be used to store a list of objects of shoes.

#==========Functions outside the class==============

def read_shoes_data():                                                                                   # Function for reading file inventory.txt.   
    """function opens the invetory.txt, reads data, 
    create shoe object and append this object to shoe list.
    """                                                                                    
    try:                                                                                                 # Try-catch block.
        with open("inventory.txt") as file:
            next(file)                                                                                   # Skipping header line.
            for line in file:                                                                            # Using  for loop to write data in dictionary after extracting it line by line.
                fields = line.strip().split(",")
                country, code, product, cost, quantity = fields
                shoes_list.append(Shoe(country, code, product, int(cost), int(quantity)))
        print("Inventory data has been loaded from file.")
    except FileNotFoundError:                                                                            # Except block. 
        print("Error: Inventory file not found.")
    except Exception as e:
        print(f"An error occurred while reading the inventory file: {str(e)}")

def capture_shoes():                                                                                      # Function for capturing shoes. 
    """function allows user to capture shoe data,
    create shoe object and append this object to shoe list.
    """
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoes_list.append(Shoe(country, code, product, cost, quantity))
    print("Shoe added to inventory.")

def view_all():                                                                                              # Function for veiwing all shoes in file inventory.txt. 
    """function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function."""
    print(tabulate([str(shoe).split(": ") for shoe in shoes_list], headers=["Code", "Product", "Quantity", "Cost"]))

def re_stock():                                                                                              # Function to restock shoes.
    """function will find the shoe object with the
    lowest quantity, which are the shoes that need to be
    re-stocked."""
    low_stock_shoe = min(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with code {low_stock_shoe.code} has the lowest quantity of {low_stock_shoe.get_quantity()}.")
    quantity_to_add = int(input("How many shoes would you like to add? "))
    low_stock_shoe.quantity += quantity_to_add
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    print("Inventory file has been updated.")

def search_shoe():                                                                                          # Function to search for shoes using their code.
    """function will search for a shoe from the list
    using the shoe code and return this object 
    so that it will be printed."""
    code = input("Enter the code of the shoe: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found in inventory.")

def value_per_item():                                                                                       # Function to calculate value per item.
    """function will calculate the total value
    for each item . """
    for shoe in shoes_list:
        print(f"{shoe.code}: Value = {shoe.cost * shoe.quantity}")

def highest_qty():                                                                                         # Function to find the highest shoes quantity, and print as for sale.
    pass
    high_qty_shoe = max(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with code {high_qty_shoe.code} has the highest quantity of {high_qty_shoe.get_quantity()} and is for sale.")


#==========Main Menu=============

def main():                                                                                                 # Function to execute each of the functions above.
    """executes each function above."""
    read_shoes_data()
    while True:
        print("\nInventory Management System")
        print("1. Capture shoe data")
        print("2. View all shoes")
        print("3. Restock shoes")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Display the shoe with the highest quantity")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()        





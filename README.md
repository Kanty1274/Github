# Github:
## Kanty Projects Github Repository

# Inventory Management System (inventory.py)
This is a simple inventory management system implemented in Python. It allows you to manage a list of shoes, including capturing new shoe data, viewing the existing inventory, restocking shoes, searching for shoes using their codes, calculating the total value per item, and displaying the shoe with the highest quantity for sale.

## Requirements:

Python 3.x
_**'tabulate'**_ library (can be installed via _**'pip install tabulate'**_)

## Usage:

1 item 1. Make sure you have Python installed on your system.

1 item 2. Install the required _**'tabulate'**_ library by running the following command:
          *Copy code*
          pip install tabulate

1 item 3. Download the _**'inventory.py**_ file and _**'inventory.txt'**_ (contains shoe data) and place them in the same directory.
        
1 Item 4. Run the script using the following command on the cmd(comand utility):
          *Copy code*
          python inventory.py

## Functionality:

### 1. Capture Shoe Data
       You can enter shoe data, including the country, code, product, cost, and quantity. This data will be added to the shoe list.

### 2. View All Shoes
       View the details of all shoes in the inventory.

### 3. Restock Shoes
       Find the shoe with the lowest quantity, and restock it by specifying the quantity to add.

### 4. Search for a Shoe
       Search for a shoe using its unique code and display its details.

### 5. Calculate Value Per Item
       Calculate the total value of each shoe item by multiplying its cost by its quantity.

### 6. Display the Shoe with the Highest Quantity
       Find the shoe with the highest quantity and indicate that it is available for sale.

### 7. Exit
       Exit the inventory management system.

## Shoe Class
   The **'Shoe'** class represents a shoe object and contains the following attributes:

. **'country'**: The country of the shoe.
. **'code'**: The unique code of the shoe.
. **'product'**: The product description of the shoe.
. **'cost'**: The cost of the shoe.
. **'quantity'**: The quantity available in the inventory.


## Screenshots:

![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)

## Credits

This project was created by [Sinqobile Kanty Moluli]. 
- [Contributor 1](https://github.com/Kanty1274/Github/) - [Owner]
- [Contributor 2](link-to-github-profile-2) - [Role]
  
## Note:

   Make sure to have the _**'inventory.txt'**_ file in the same directory as the script for data loading purposes.
   If the file is not found, the script will handle the exception and display an appropriate message.

  Feel free to use, modify, and distribute this inventory management system according to your needs.

  Happy shoe inventory management! 🚀
  
  

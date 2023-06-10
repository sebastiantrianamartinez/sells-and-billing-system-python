# Sales System

## Description
This is a sales and billing system developed using the Tkinter library in Python. The system allows for product sales, creating new products, generating reports, and updating inventory.

## Requirements
- Python 3.x
- Tkinter
- Matplotlib

## Usage
1. Run the Python file to start the application.
2. A window will appear with the interface of the sales and billing system.
3. To make a sale:
   - Select a product from the dropdown menu.
   - Enter the quantity of products to sell.
   - Click the "Add" button to add the product to the current sale list.
   - Repeat the above steps to add more products to the current sale.
   - Once you have added all the desired products, click the "Sell" button to complete the sale.

## Features
- Current Sell:
  - Allows selecting products and specifying quantities to add them to the current sale.
  - Displays the list of products in the current sale.
- Add Products:
  - Allows creating new products by entering their name, quantity, and price.
- Reports:
  - Provides two options for generating reports:
    - Sales Graph: Displays a graph of sales over time.
    - Cash Graph: Displays a graph of revenue over time.
- Stock:
  - Allows updating the stock of a selected product by specifying an additional quantity.

## Class Structure
- `App`: Represents the main application class. It handles the GUI and the logic for various actions.
- `product`: Represents a product class that handles product-related operations, such as creating and updating products.
- `sell`: Represents a sell class that handles the logic for selling products.
- `tracking`: Represents a tracking class that generates reports on sales and revenue.

## Dependencies
- `tkinter`: Used for creating the graphical user interface.
- `ttk`: Used for creating combobox widgets.
- `tkFont`: Used for defining font styles.
- `messagebox`: Used for displaying error and success messages.
- `matplotlib.pyplot`: Used for creating and displaying graphs.

## Additional Notes
- Make sure all the required dependencies are installed before running the application.
- The application assumes the existence of the `product.py`, `sell.py`, and `tracking.py` files for the respective classes.
- The code provided is a basic implementation and may require further modifications and improvements based on specific requirements.

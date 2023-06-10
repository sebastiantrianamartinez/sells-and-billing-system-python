# Product Class Documentation

The `product` class represents a product in the sales and billing system.

## Constructor

### `__init__(self, name, price, stock)`

The constructor initializes a `product` object with the provided parameters.

- `name` (str): The name of the product.
- `price` (float): The price of the product.
- `stock` (int): The stock quantity of the product.

## Method: `create()`

The `create()` method creates a new product entry in the product database file.

- Returns: The ID of the created product.

## Method: `update()`

The `update()` method updates the information of an existing product in the product database file.

## Method: `updateStock(id)`

The `updateStock()` method updates the stock quantity of a product identified by its ID in the product database file.

- `id` (int): The ID of the product to update.

## Method: `select(id)`

The `select()` method retrieves the information of a product identified by its ID from the product database file.

- `id` (int): The ID of the product to retrieve.

## Method: `getAll()`

The `getAll()` method retrieves information for all products stored in the product database file.

- Returns: A list of lists, where each inner list contains the product ID and name.

```python
class product:
    def __init__(self, name, price, stock):
        # Constructor implementation
        
    def create(self):
        # Create method implementation
        
    def update(self):
        # Update method implementation
        
    def updateStock(self, id):
        # Update stock method implementation
        
    def select(self, id):
        # Select method implementation
        
    def getAll():
        # getAll method implementation

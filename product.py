class product:
    def __init__(self, name, price, stock):
        with open("assets/data/products.txt", "r") as productFile:
            id = sum(1 for line in productFile)
        self.id = id + 1 
        self.name = name
        self.price = price
        self.stock = stock
    
    def create(self):
        productFile = open("assets/data/products.txt", "a")
        productFile.write(
            str(self.id) 
            + "-"
            + self.name
            + "-"
            + str(self.price)
            + "-"
            + str(self.stock)
            + "\n"
        )
        productFile.close
        return self.id
    
    def update(self):
        with open("assets/data/products.txt", "r") as productFile:
            lines = productFile.readlines()
        lines[self.id - 1] = (
            str(self.id)
            + "-"
            + self.name
            + "-"
            + str(self.price)
            + "-"
            + str(self.stock) 
        )
        with open("assets/data/products.txt", "w") as productFile:
            productFile.writelines(lines)
            print("success")
    
    def updateStock(self, id):
        with open("assets/data/products.txt", "r") as productFile:
            lines = productFile.readlines()
        product = str(lines[id - 1]).split('-')
        product[3] = str(int(product[3]) + self.stock)
        newLine = ""
        for element in product:
            newLine += element + "-"
        newLine = newLine[:-1] + "\n"
        lines[id - 1] = newLine
        with open("assets/data/products.txt", "w") as productFile:
            productFile.writelines(lines)
        return "Actualización exitosa!!"
    
    def select(self, id):
        with open("assets/data/products.txt", "r") as productFile:
            lines = productFile.readlines()
        return lines[id - 1]
    
    def getAll():
        productsArray = [] 
        with open("assets/data/products.txt", "r") as productFile:
            lines = productFile.readlines()
            for line in lines:
                substrings = line.strip().split('-')
                if len(substrings) >= 2:
                    productsArray.append(substrings[:2])
        return productsArray
from product import product
from datetime import datetime
import json
with open('config.json') as config_file:
    config = json.load(config_file)

class sell:
    def __init__(self, products, quantities):
        self.products = products
        self.quantities = quantities
        self.agent = config['market_agent']
        self.market = config['market_name']
    
    def sell(self):
        i = 0
        currentSell = ""
        bill = "Factura " + self.market + "\nFecha: " + str(datetime.now()) + "\n" + "Vendedor: " + self.agent + "\n"
        bill += "\n\n" + "Productos:\n"
        total = 0
        for product_id in self.products:
            
            product_object = product("", 0, 0)
            product_info = product_object.select(product_id).split("-")
            product_name = product_info[1]
            product_price = int(product_info[2])
            quantity = self.quantities[i]
            total += (product_price*quantity)
            currentSell += f"{product_name} (x{quantity}) ({product_price * quantity})---"
            bill += f"{product_name} (x{quantity}) ({product_price * quantity}) \n"
            i += 1
        currentSell += "Total: " + str(total)
        bill += "Total: " + str(total)
        

        sellInfo = str(datetime.now().strftime("%Y_%m_%d")) + "-" + str(total) + "-"
        for item in self.products:
            sellInfo += str(item) + ","
        sellInfo += "\n"
        self.billment(bill, sellInfo)
        return [" resumen: " + currentSell, bill]
    
    def billment(self, billText, sellInfo):
        currentBill = "bill-" + str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        newBillFile = open("assets/data/billment/" + currentBill + ".txt", "w")
        newBillFile.write(billText)
        newBillFile.close()
        sellsFile = open("assets/data/sells.txt", "a")
        sellsFile.write(sellInfo)
        sellsFile.close()





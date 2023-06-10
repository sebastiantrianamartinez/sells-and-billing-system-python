import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from product import product
from sell import sell
from tracking import tracking
import matplotlib.pyplot as plt

#Array of products

products = product.getAll()
sellProducts = []
sellQuantities = []

class App:
    def __init__(self, root):
        #setting title
        root.title("Sistema de ventas ")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        systemTitle=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=16)
        systemTitle["font"] = ft
        systemTitle["fg"] = "#333333"
        systemTitle["justify"] = "left"
        systemTitle["text"] = "Bienvenido al sistema de venta y facturación."
        systemTitle.place(x=10,y=10,width=524,height=30)

        #------CURRENT SELL------------------------------------------------------
        self.combobox=ttk.Combobox(root)
        self.combobox["values"] = products  # Obtener solo los nombres de los productos
        self.combobox["font"] = tkFont.Font(family='Arial', size=10)
        self.combobox["foreground"] = "#333333"
        self.combobox["justify"] = "left"
        self.combobox.current(0)
        self.combobox.place(x=10, y=50, width=298, height=30)

        self.sellQuantity=tk.Entry(root)
        self.sellQuantity["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.sellQuantity["font"] = ft
        self.sellQuantity["fg"] = "#333333"
        self.sellQuantity["justify"] = "center"
        self.sellQuantity.insert(0, "Cantidad")
        self.sellQuantity.place(x=320,y=50,width=69,height=30)

        sellAdd=tk.Button(root)
        sellAdd["bg"] = "#efefef"
        ft = tkFont.Font(family='Arial',size=10)
        sellAdd["font"] = ft
        sellAdd["fg"] = "#000000"
        sellAdd["justify"] = "center"
        sellAdd["text"] = "Añadir"
        sellAdd.place(x=400,y=50,width=68,height=30)
        sellAdd["command"] = self.sellAdd_command

        sell=tk.Button(root)
        sell["bg"] = "#1e90ff"
        sell["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        sell["font"] = ft
        sell["fg"] = "#ffffff"
        sell["justify"] = "center"
        sell["text"] = "Vender"
        sell.place(x=10,y=90,width=459,height=30)
        sell["command"] = self.sell_command

        # ADD PRODUCTS----------------------------

        productsDesc=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        productsDesc["font"] = ft
        productsDesc["fg"] = "#333333"
        productsDesc["justify"] = "center"
        productsDesc["text"] = "Productos:"
        productsDesc.place(x=10,y=160,width=70,height=25)

        self.productsName=tk.Entry(root)
        self.productsName["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.productsName["font"] = ft
        self.productsName["fg"] = "#333333"
        self.productsName["justify"] = "center"
        self.productsName.insert(0, "Nombre")
        self.productsName.place(x=10,y=190,width=243,height=30)

        self.productsQuantity=tk.Entry(root)
        self.productsQuantity["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.productsQuantity["font"] = ft
        self.productsQuantity["fg"] = "#333333"
        self.productsQuantity["justify"] = "center"
        self.productsQuantity.insert(0, "Cantidad")
        self.productsQuantity.place(x=10,y=230,width=72,height=31)

        self.productsPrice=tk.Entry(root)
        self.productsPrice["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.productsPrice["font"] = ft
        self.productsPrice["fg"] = "#333333"
        self.productsPrice["justify"] = "center"
        self.productsPrice.insert(0, "Precio")
        self.productsPrice.place(x=90,y=230,width=83,height=30)

        productsAdd=tk.Button(root)
        productsAdd["bg"] = "#1e90ff"
        productsAdd["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        productsAdd["font"] = ft
        productsAdd["fg"] = "#ffffff"
        productsAdd["justify"] = "center"
        productsAdd["text"] = "Crear"
        productsAdd.place(x=180,y=230,width=72,height=30)
        productsAdd["command"] = self.productsAdd_command

        reportsTitle=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        reportsTitle["font"] = ft
        reportsTitle["fg"] = "#333333"
        reportsTitle["justify"] = "left"
        reportsTitle["text"] = "Informes:"
        reportsTitle.place(x=10,y=280,width=70,height=25)

        reportsSells=tk.Button(root)
        reportsSells["bg"] = "#efefef"
        ft = tkFont.Font(family='Arial',size=10)
        reportsSells["font"] = ft
        reportsSells["fg"] = "#000000"
        reportsSells["justify"] = "center"
        reportsSells["text"] = "Grafica de ventas"
        reportsSells.place(x=10,y=310,width=152,height=30)
        reportsSells["command"] = self.reportsSells_command

        reportsCash=tk.Button(root)
        reportsCash["bg"] = "#efefef"
        ft = tkFont.Font(family='Arial',size=10)
        reportsCash["font"] = ft
        reportsCash["fg"] = "#000000"
        reportsCash["justify"] = "center"
        reportsCash["text"] = "Grafica de ingresos"
        reportsCash.place(x=10,y=350,width=152,height=30)
        reportsCash["command"] = self.reportsCash_command

        stockTitle=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        stockTitle["font"] = ft
        stockTitle["fg"] = "#333333"
        stockTitle["justify"] = "left"
        stockTitle["text"] = "Stock:"
        stockTitle.place(x=320,y=160,width=70,height=25)

        self.combobox_2=ttk.Combobox(root)
        self.combobox_2["text"] = "Seleccione un producto"
        self.combobox_2["values"] = products
        self.combobox_2["font"] = tkFont.Font(family='Arial', size=10)
        self.combobox_2["foreground"] = "#333333"
        self.combobox_2["justify"] = "left"
        self.combobox_2.current(0)
        self.combobox_2.place(x=320, y=190, width=241, height=30)

        self.stockQuantity=tk.Entry(root)
        self.stockQuantity["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.stockQuantity["font"] = ft
        self.stockQuantity["fg"] = "#333333"
        self.stockQuantity["justify"] = "center"
        self.stockQuantity.insert(0,"Adicional")
        self.stockQuantity.place(x=320,y=230,width=100,height=30)

        stockUpdate=tk.Button(root)
        stockUpdate["bg"] = "#1e90ff"
        stockUpdate["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        stockUpdate["font"] = ft
        stockUpdate["fg"] = "#ffffff"
        stockUpdate["justify"] = "center"
        stockUpdate["text"] = "Actualizar"
        stockUpdate.place(x=440,y=230,width=121,height=30)
        stockUpdate["command"] = self.stockUpdate_command
        
        currentSellTitle=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        currentSellTitle["font"] = ft
        currentSellTitle["fg"] = "#333333"
        currentSellTitle["justify"] = "left"
        currentSellTitle["text"] = "Esta venta:"
        currentSellTitle.place(x=240,y=300,width=70,height=25)

        self.currentSellList=tk.Text(root)
        #self.currentSellList.insert(tk.END,"2 Escobas de 2000")
        self.currentSellList.place(x=240,y=330,width=323,height=150)


    def sellAdd_command(self):
        currentProduct = self.combobox.current()
        currentQuantity = self.sellQuantity.get()
        if not currentQuantity.isdigit():
            messagebox.showinfo("Error", "Los datos ingresados no son válidos")
            return 0
        sellProducts.append(int(currentProduct) + 1)
        sellQuantities.append(int(currentQuantity))
        self.currentSellList.insert( tk.END,
            self.combobox.get() + "-" + currentQuantity + "\n"
        )



    def sell_command(self):
        if len(sellProducts) <= 0:
            messagebox.showinfo("Error", "Debe seleccionar al menos 1 producto")
            return 0
        sellObject = sell(sellProducts, sellQuantities)
        sellment = sellObject.sell()
        
        ventana_alerta = tk.Toplevel(root)
        ventana_alerta.title("Alerta")
        # Título de la alerta
        label_titulo = tk.Label(ventana_alerta, text="Proceso exitoso")
        label_titulo.pack()
        # Texto de la alerta
        label_texto = tk.Label(ventana_alerta, text="El proceso se ha completado correctamente, " + sellment[0])
        label_texto.pack()
        # Función para ver la factura
        def ver_factura():
            # Aquí puedes agregar el código para mostrar la factura
            messagebox.showinfo("Factura:", sellment[1])

        # Botón para ver la factura
        boton_ver_factura = tk.Button(ventana_alerta, text="Ver Factura", command=ver_factura)
        boton_ver_factura.pack()

        # Botón para cerrar la ventana de alerta
        boton_cerrar = tk.Button(ventana_alerta, text="Cerrar", command=ventana_alerta.destroy)
        boton_cerrar.pack()
            

    def productsAdd_command(self):
        productName = self.productsName.get()
        productQuantity = self.productsQuantity.get()
        productPrice = self.productsPrice.get()
        if productName == "" or productName == "Nombre" or not productQuantity.isdigit() or not productPrice.isdigit():
            messagebox.showinfo("Error", "Los datos ingresados no son válidos")
            return 0
        productObject = product(productName, productPrice, productQuantity)
        creation = productObject.create()
        messagebox.showinfo("Proceso exitoso", "El producto ha sido añadido con exito, id: " + str(creation))
        self.productsName.delete(0,tk.END)
        self.productsQuantity.delete(0,tk.END)
        self.productsPrice.delete(0,tk.END)

    def reportsSells_command(self):
        trackingObject = tracking()
        tracks = trackingObject.sellsReport()
        plt.plot(tracks[0], tracks[1])
        plt.show()


    def reportsCash_command(self):
        trackingObject = tracking()
        tracks = trackingObject.sellsReport()
        plt.plot(tracks[0], tracks[1])
        plt.show()


    def stockUpdate_command(self):
        if not self.stockQuantity.get().isdigit():
            messagebox.showinfo("Error", "Los datos ingresados no son válidos")
            return 0
        productId = self.combobox_2.current() + 1
        newProductStock = int(self.stockQuantity.get())
        productObject = product("", 0, newProductStock)
        updateRequest = productObject.updateStock(productId)
        messagebox.showinfo("Proceso exitoso", updateRequest)


    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

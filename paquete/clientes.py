import random

class Clientes(object) : 

    def __init__ (self, nombre, apellido, direccion) :

        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

        self.compra = []

    #Esta funcion en realidad solo se utiliza cuando junto la primer entregfa con la segunda. De momento no va a ver su utilidad.
    def crear_cliente(self) :

        self.nombre = input("\nIngrese su nombre: ")
        while True :
            #Corroboramos que no se ingrese un nombre vacio
            if self.nombre == "" :
                print("\nNo ha ingresado ningún dato.")
                self.nombre = input("\nIngrese su nombre: ")

            else:
                break

        self.apellido = input("\nIngrese su apellido: ")
        while True :
            #Corroboramos que no se ingrese un apellido vacio
            if self.apellido == "" :
                print("\nNo ha ingresado ningún dato.")
                self.apellido = input("\nIngrese su apellido: ")

            else:   
                break

        self.direccion = input("\nIngrese su dirección: ")
        while True :
            #Corroboramos que no se ingrese una direccion vacia
            if self.direccion == "" :
                print("\nNo ha ingresado ningún dato.")
                self.direccion = input("\nIngrese su dirección: ")

            else:    
                break


    def __str__ (self) :

        self.crear_cliente()

        print(f"\nSe registro la siguiente persona:\nNombre: {self.nombre} \nApellido: {self.apellido}")
    

    def agregar_producto(self, producto, precio):

        self.compra.append((producto, precio))
        
        print(f"\nHa agregado el producto: '{producto}' a su carrito por: ${precio}")


    def mostrar_compra(self):

        total_compra = 0

        print("\nCarrito de compras:")

        for producto, precio in self.compra:
            print(f"  Producto: {producto} |  Precio: ${precio}") 
            total_compra += precio

        if total_compra == 0 :
            print("Su carrito esta vacío")
        else :
            print(f"\nTotal de la compra: ${total_compra}")


    def menu_compra(self):
        while True:
            print("\nMENU \n1. Agregar productos al carrito \n2. Ver carrito \n3. Salir del programa")

            menu_resp = int(input("\nIngrese su respuesta en forma numérica: "))

            if menu_resp == 1:
                producto = input("\nIngrese el nombre del producto: ")
                precio = random.uniform(1.0, 100.0) 
                self.agregar_producto(producto, precio)

            elif menu_resp == 2:
                self.mostrar_compra()

            elif menu_resp == 3:
                self.compra_envio()
                print("\n¡¡Muchas gracias por elegirnos!!")
                break

            else:
                print("Opción inválida. Inténtalo nuevamente.")


    def compra_envio (self) :

        
        print(f"\nSu compra se enviara a la dirección {self.direccion} a nombre de {self.nombre} {self.apellido}")
    
    



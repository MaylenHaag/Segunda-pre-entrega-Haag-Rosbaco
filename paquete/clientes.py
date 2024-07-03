import random

class Clientes(object) : 

    def __init__ (self, nombre, apellido, direccion) :

        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

        self.compra = []

    def __str__ (self) :

        print(f"Se registro la siguiente persona: {self.nombre} {self.apellido}")
    

    def agregar_producto(self, producto, precio):

        self.compra.append((producto, precio))
        
        print(f"Ha agregado el producto: '{producto}' a su carrito por: ${precio}")


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


    def menu(self):
        while True:
            print("\nMENU \n1. Agregar productos al carrito \n2. Ver carrito \n3. Salir del programa")

            menu_resp = int(input("\nIngrese su respuesta en forma numérica: "))

            if menu_resp == 1:
                producto = input("Ingrese el nombre del producto: ")
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
    
    



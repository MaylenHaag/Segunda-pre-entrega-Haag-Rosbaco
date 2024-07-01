import random

class Clientes(object) : 

    def __init__ (self, nombre, apellido, direccion) :

        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

        self.compra = [] #me gustaria que este afuera del init

    def __str__ (self) :

        print(f"Se registro la siguiente persona: {self.nombre} {self.apellido}")
    

    def agregar_producto(self, producto, precio):

        self.compra.append((producto, precio))
        
        print(f"Ha agregado el producto: '{producto}' a su carrito por: ${precio}")


    def mostrar_compra(self):

        print("Su carrito de compras es:")

        total_gastado = 0

        for producto, precio in self.compra:
            print(f"  - {producto} (${precio})") #quiero cambiar este formato
            total_gastado += precio

        print(f"Total gastado: ${total_gastado}")


    def menu(self):
        while True:
            print("\n--- Bienvenidos al menu de la tienda ---")
            print("1. Agregar producto al carrito(stock sin limites)")
            print("2. Mostrar carrito")
            print("3. Salir")

            opcion = input("Selecciona una opción (1/2/3): ")
            if opcion == "1":
                producto = input("Nombre del producto: ")
                precio = random.uniform(1.0, 100.0)  # Precio aleatorio entre 1 y 100
                self.agregar_producto(producto, precio)
            elif opcion == "2":
                self.mostrar_compra()
            elif opcion == "3":
                print("¡Gracias por compra en Tienda RomeroLeandro!!!!!\n hasta la proxima")
                break
            else:
                print("Opción inválida. Inténtalo nuevamente.")


    def compra_envio (self) :

        print(f"La compra {self.compra} se enviara a la dirección {self.direccion}")
    
    



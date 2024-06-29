class Clientes(object) :
    
    def __init__ (self, nombre, apellido, direccion, compra) :

        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.compra = compra


    def __str__ (self) :

        return f"Se registro la siguiente persona: {self.nombre} {self.apellido}"
    

    def compra_envio (self) :

        return f"La compra {self.compra} se enviara a la dirección {self.direccion}"
    
    pass



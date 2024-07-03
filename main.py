from paquete.clientes import Clientes


p_nombre = input("Ingrese su nombre: ")
p_apellido = input("Ingrese su apellido: ")
p_direccion = input("Ingrese su direccion: ")

cliente = Clientes(nombre = p_nombre, apellido = p_apellido, direccion = p_direccion)

cliente.menu()












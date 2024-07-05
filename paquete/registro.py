from clientes import Clientes

#TUTOR DIEGO:
#Esto todavia no funciona bien, mi idea es que la persona pueda crear un usuario, ingresar, luego hacer la compra y salir.
#Este archivo esta en modificacion por lo que va a ver que no se ejecuta.

#REGISTRO DE USUARIOS

#Creo diccionario donde se guardaran los datos de los usuarios
DB = {}

cliente = Clientes

#FUNCIONES DE USUARIO

#Funcion para registrar y guardar usuarios
def registro_usuarios (DB):

    usuario = input("\nIngrese el nombre del usuario a crear: ")
    while True :
        #Corroboramos que no se ingrese un usuario vacio
        if usuario == "" :
            print("\nNo ha ingresado ningún dato.")
            usuario = input("\nIngrese el nombre del usuario a crear: ")
        #Corroboramos que no se cree un nombre de usuario ya existente
        elif usuario in DB :
            print("\nUsuario existente. Debe usar otro nombre.")
            usuario = input("\nIngrese el nombre del usuario a crear: ")
        else :
            break

    contraseña = input("Ingrese la contraseña: ")
    while True :        
        #Corroboramos que no se ingrese una contraseña vacia
        if contraseña == "":
            contraseña = input("\nSu contraseña no puede estar vacía. Vuelva a ingresarla: ")
        else :
            break

 #   u_nombre = input("\nIngrese su nombre: ")
#     while True :
 #        #Corroboramos que no se ingrese un nombre vacio
#        if u_nombre == "" :
 #           print("\nNo ha ingresado ningún dato.")
 #           u_nombre = input("\nIngrese su nombre: ")
#
 #       else:
 #           break

 #   u_apellido = input("\nIngrese su apellido: ")
  #  while True :
        #Corroboramos que no se ingrese un apellido vacio
  #      if u_apellido == "" :
 #           print("\nNo ha ingresado ningún dato.")
 #           u_apellido = input("\nIngrese su apellido: ")

 #       else:   
 #           break

  #  u_direccion = input("\nIngrese su dirección: ")
 #   while True :
 #       #Corroboramos que no se ingrese una direccion vacia
 #       if u_direccion == "" :
 #           print("\nNo ha ingresado ningún dato.")
 #           u_direccion = input("\nIngrese su dirección: ")

  #      else:    
  #          break
    
    
  #  cliente = Clientes(nombre = u_nombre, apellido = u_apellido, direccion = u_direccion)

    
    #Imprimimos elnombre de usuario y contraseña recien registrados
    cliente.__str__()
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {contraseña}")

    guardo_usuarios(usuario, contraseña)

    menu_ingreso()

    return usuario, contraseña


#Funcion para guardar los datos de los usuarios en el diccionario "DB"
def guardo_usuarios (usuario, contraseña):
    
    DB[usuario] = contraseña

    return DB


#Funcion para mostrar todos los usuarios registrados
def mostrar_usuarios(DB) :
    print("\nLa lista de usuarios registrados es: ")   

    for usuario, contraseña in DB.items() :
        print(f"\nUsuario: {usuario}")
        print(f"Contraseña: {contraseña}")

    menu_ingreso()


#Funcion para hacer el login
def login(DB):
    intentos = 3
    #Bucle para permitir solo 3 intentos 
    while intentos > 0:
        usuario = input("\nIngrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        #Corroboramos que el usuario exista
        if usuario in DB :
            #En caso de existir el usuario, corroboramos que la contraseña sea correcta e iniciamos sesion
            if DB[usuario] == contraseña :
                print("\nInicio de sesión exitoso")
                cliente.menu_compra()
                break
            #Si la contraseña no es correcta, volvemos a pedir nombre de usuario y contraseña
            elif DB[usuario] != contraseña :
                print("\nUsuario o contraseña incorrectos.")
                intentos -= 1
        #Si el nombre de usuario no existe, volvemos a pedir nombre de usuario y contraseña
        else :
            print("\nUsuario o contraseña incorrectos.")
            intentos -= 1

        if intentos == 0 :
            print("Has agotado los intentos. \nPrograma finalizado.")
                
            
# FUNCION MENU Y BIENVENIDA

#Funcion menu
def menu_ingreso ():
    print("\nMENU \n1. Ingresar al programa \n2. Registrar un usuario \n3. Ver los usuarios registrados \n4. Salir del programa")

    menu_resp = int(input("\nIngrese su respuesta en forma numérica: "))

    if menu_resp == 1 :
        login(DB)
    elif menu_resp == 2 :
        registro_usuarios(DB)
    elif menu_resp == 3 :
        mostrar_usuarios(DB)
    elif menu_resp == 4 :
        print("\nHa finalizado el programa")
    else :
        print("\nRespuesta incorrecta.")
        menu_ingreso()


salida = 0

while salida == 0:
   
   respuesta = input("\n¿Desea registrarse?\nIngrese 'SI' si se desea registrar, en caso contrario ingrese 'NO': \n")

   if respuesta == 'no' or respuesta == 'nO' or respuesta == 'No' or respuesta == 'NO':
        salida = 1
        print("\nHa finalizado el programa")

   elif respuesta == 'si' or respuesta == 'sI' or respuesta == 'Si' or respuesta == 'SI':
        #Llamamos a la funcion "registro_usuarios" para crear el usuario
        salida = 1
        registro_usuarios(DB)

   else:
        print("\nRespuesta incorrecta.")
        
       








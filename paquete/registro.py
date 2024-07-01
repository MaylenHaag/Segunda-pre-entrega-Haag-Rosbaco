from clientes import Clientes

#REGISTRO DE USUARIOS

#Creo diccionario donde se guardaran los datos de los usuarios
DB = {}


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
        else:
            print("\nEl usuario ha sido correctamente registrado!")
            break

        u_nombre=input("\nIngrese su nombre: ")
        u_apellido=input("Ingrese su apellido: ")
        u_direccion=input("Ingrese su direccion: ")

    Clientes(nombre=u_nombre, apellido=u_apellido, direccion=u_direccion)
    
    #Imprimimos elnombre de usuario y contraseña recien registrados
    print(f"\nNombre de usuario: {usuario}")
    print(f"Contraseña: {contraseña}")

    guardo_usuarios(usuario, contraseña)

   

    #menu()

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

    menu()


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
def menu ():
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
        menu()


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
        
       








"""
 El sistema debe componer por un menu con las siguientes opciones
 1) Registrar cuarto
 2) Consultar cuartos
 3) Salida del hotel
 4) Salir del hotel
 
1) Debe registrar en el cuarto (posicion siguiente del diccionario) 
    Cuantas personas estaran en ese cuarto y por la n cantidad de personas registrar
    Nombre - apellidos - telefono - email 
    Mostrar los datos registrados para confirmar

2) Se deben mostrar los cuartos ocupados y preguntar al usuario que cuarto quiere ver
    Mostrar la cantidad de pesonas en el cuarto y la informacion de las mismas

3) Se debe preguntar cual cuarto se desocupa mostrar el valor a pagar y limpiar el cuarto y sus ocupantes
    calculo (Valor = 155.400 * persona )

4) Salir del sistema
"""
#persona= {'nombre': 'Federiko', 'apellidos': 'Leivo', 'telefono': '2234234', 'email': 'federiko@gmail.com'}
#perro = {'dueño': 'Federiko','raza':'canino','vacunas':['tosferina','rabia','cancha']}
import os
def menu():
    os.system('cls')
    print("Bienvenido al Hotel Overlook")
    print ("1. Registrarse")
    print ("2. Consultar cuartos")
    print ("3. Salida del hotel")
    print ("9. Salir del hotel")

crt1={'nombre': ['Lina', 'Andres'],
        'apellido': ['Rengifo', 'Bolivar'],
        'telefono': ['4534522', '7457456'],
        'email': ['lina@correo', 'andres@correo']}
crt2={}
crt3={}
crt4={'nombre': ['Maria', 'Catalina'],
        'apellido': ['Rodriguez', 'Martinez'],
        'telefono': ['5445235', '8593453'],
        'email': ['maria@correo', 'cata@correo']}

hotel={
    "cuarto1":crt1,
    "cuarto2":crt2,
    "cuarto3":crt3,
    "cuarto4":crt4
}    

while True:
    menu()

    def regis():
        cntPersonas= int(input("Digite la cantidad de personas que van a reservar cuarto: "))
        nombre=[]
        apellido=[]
        telefono=[]
        email=[]
        for x in range(cntPersonas):
            dgNombre=input("Digite su nombre: ")
            nombre.insert(x,dgNombre)

            dgApellido=input("Digite su apellido: ")
            apellido.insert(x,dgApellido)

            dgTelefono=input("Digite su telefono: ")
            telefono.insert(x,dgTelefono)

            dgEmail=input("Digite su email: ")
            email.insert(x,dgEmail)

        hotel.update({'cuarto2': {'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'email': email} })
        print(hotel)
        input("hotel: ")

    def ver():
        crVer= input("Digite el cuarto que desea ver: ")
        if(crVer)==("crt1"):
            #crVer= crt1
            if (len(crt1)>0):
                print(crt1)
                input("Salir: ")
            else: 
                input("Cuarto vacio")

        if(crVer)==("crt2"):
            #crVer= crt2
            if (len(crt2)>0):
                print(crt2)
                input("Salir: ")
            else: 
                input("Cuarto vacio")

        if(crVer)==("crt3"):
            crVer= crt3
            if (len(crVer)>0):
                print(crt3)
                input("Salir: ")
            else: 
                input("Cuarto vacio")

        if(crVer)==("crt4"):
            crVer= crt4
            if (len(crVer)>0):
                print(crt4)
                input("Salir: ")
            else:
                input("Cuarto vacio") 

    def verificarDisponibilidad():
        crDeseado= input("Digite el cuarto que desea ocupar: ")

        if(crDeseado)==("crt1"):
            crDeseado= crt1
            if (len(crDeseado)>0):
                input("Cuarto ocupado: ")
            else: 
                regis()

        if(crDeseado)==("crt2"):
            crDeseado= crt2
            if (len(crDeseado)>0):
                input("Cuarto ocupado: ")
            else: 
                regis()

        if(crDeseado)==("crt3"):
            crDeseado= crt3
            if (len(crDeseado)>0):
                input("Cuarto ocupado: ")
            else: 
                regis()

        if(crDeseado)==("crt4"):
            crDeseado= crt4
            if (len(crDeseado)>0):
                input("Cuarto ocupado: ")
            else: 
                regis()


    opcionMenu = input("Ingrese una opción valida: ")
    if opcionMenu=='1':
        verificarDisponibilidad()
    elif opcionMenu=='2':
        regis()
        input("Sal: ")
    elif opcionMenu=='3':
        input("Pulse enter para salir")
    elif opcionMenu=="9":
        break
    else: 
        input("No ha pulsado una opcion valida: ")

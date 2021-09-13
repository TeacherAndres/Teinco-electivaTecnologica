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
    
    def registrar():
        #print("crt1, crt2, crt3, crt4")
        crDeseado= input("Digite el cuarto que desea ocupar: ")

        if(crDeseado)==("crt1"):
            crDeseado= crt1
            if (len(crDeseado)>0):
                print("cuarto ocupado: ")
            else: 
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

        if(crDeseado)==("crt2"):
            crDeseado= crt2
            if (len(crDeseado)>0):
                print("cuarto ocupado: ")
            else: 
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

        if(crDeseado)==("crt3"):
            crDeseado= crt3
            if (len(crDeseado)>0):
                print("cuarto ocupado: ")
            else: 
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

        if(crDeseado)==("crt4"):
            crDeseado= crt4
            if (len(crDeseado)>0):
                print("cuarto ocupado: ")
            else: 
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

    opcionMenu = input("Ingrese una opción valida: ")
    if opcionMenu=='1':
        registrar()
    elif opcionMenu=='2':
        print(hotel)
        input("Consultar cuartos: ")
    elif opcionMenu=='3':
        print("Salir del Hotel: ")
        def tablaN():
            i=1
            vD1 = int(input("Ingrese un valor \n"))
            print("Tabla del '",vD1,"': ")
            while(i<=10):
                print("'",vD1,"' * '",i,"' = '",vD1*i,"'")
                i+=1
        tablaN()
        input("Pulse enter para salir")
    elif opcionMenu=="9":
        break
    else: 
        input("No ha pulsado una opcion valida: ")

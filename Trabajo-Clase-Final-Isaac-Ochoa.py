opcion=int
PersonasARegistrar=int
Habitacion = int
while opcion !=4:
    def Menu():
            print("\t*******---------*********")

            print("\t 1. Registrar cuarto")

            print("\t 2. Consultar cuatros")

            print("\t 3. Salida del hotel")

            print("\t 4. Salir del sistema")


            print("\t********---------*********")

    Menu()
    opcion = int(input("\t Selecione la opcion del menu que desea realizar\n"))
       
    Cuarto={
        0:{'Nombre': ['Isaac', 'Esteban'], 
        'Apellido': ['Ochoa', 'Garcia'],
        'Telefono': [12, 1122],
        'Email': ['Isaac877', 'EstebanGar']},
        1:'Vacio',
        2:'Vacio',
        3:'Vacio',
        4:{'Nombre': ['Hernan'], 
        'Apellido': ['Torres'],
        'Telefono': [6485 ],
        'Email': ['Hernan45']},
        5:'Vacio',
        6:{'Nombre': ['Andres', 'Arturo','Santiago'], 
        'Apellido': ['Sotelo', 'Laverde','Lozano'],
        'Telefono': [877, 11522,3698],
        'Email': ['AndiSotelo', 'Art12','LozanoSnati']},
        7:'Vacio',
        8:'Vacio',
        9:'Vacio',
        10:{'Nombre': ['Daniel'], 
        'Apellido': ['Villa'],
        'Telefono': [5401 ],
        'Email': ['DVilla54']},
        }

    def RegistroCuarto():
        x=0
        while x < len(Cuarto):
            if Cuarto[x]=='Vacio':
                print("Cuartos Desocupados", x)
                print("\n")    
        
            x+=1
        Habitacion=int(input("Digite el numero de la habitacion que desea ocupar :  "))
        Cuarto[Habitacion]={
            'Nombre':[],
            'Apellido':[],
            'Telefono':[],
            'Email':[]}
    
        
        PersonasARegistrar=int(input("Digite el numero de personas que ingresaran :  "))
        x=0
        while (x < PersonasARegistrar): 
            Nombre=input("Digite el Nombre de inquilino  :  ")
            Apellido=input("Digite el Apellido de inquilino  :  ")
            Telefono=int(input("Digite el numero telefonico del inquilino:  "))
            Email=input("Digite el Email del inquilino  :  ")

            Cuarto[Habitacion]['Nombre'].insert(x,Nombre)
            Cuarto[Habitacion]['Apellido'].insert(x,Apellido)
            Cuarto[Habitacion]['Telefono'].insert(x,Telefono)
            Cuarto[Habitacion]['Email'].insert(x,Email)
            x+=1
        
        print(Cuarto[Habitacion])   
    def ConsultarCuarto():
        x=0
        while x < len(Cuarto):
            if Cuarto[x]!='Vacio':
                print("Cuartos Ocupados", x)
                print("\n")    
            x+=1
        Habitacion=int(input("Digite el numero de la habitacion que desea ver :  "))
        print(len(Cuarto[Habitacion]['Nombre']),"  Inquilino(s)")
        print(Cuarto[Habitacion])
    def SalidaDelHotel():
            HabitacionDesocupada=int(input("Digite el numero de la habitacion que se va a ser desocupada :  "))
            print(Cuarto[HabitacionDesocupada])
            ValorAPagar=155.400 * len(Cuarto[HabitacionDesocupada]['Nombre'])
            print(f"Valor a total a pagar : {ValorAPagar} ")
            Cuarto.pop(HabitacionDesocupada)

    def switch():       
                    
        if (opcion==1):
            RegistroCuarto()
        elif (opcion==2):
            ConsultarCuarto()
        elif (opcion==3):
            SalidaDelHotel()  
    switch() 

"""
 El sistema debe componer por un menu con las sigientes opciones
 1) Registrar cuarto
 2) Consultar cuatros
 3) Salida del hotel
 4) Salir del hotel
 
1) Debe registrar en el cuarto (pocision sigueinte del diccionario) 
    Cuantas persdonas estaran en ese cuarto y por la n cantidad de personas registrar
    Nombre - apellidos - telefono - email 
    Mostrar los datos registrados apra confirmar

2) Seben mostrar los caurtos ocupados y preguntar al usuario que cuarto quiere ver
    Mostrar la cantida de pesonas en el cuarto y la infromacion de las mismas

3) Se debe preguntar cual cuarto se desocupa mostrar el valor a pagar y limpiar el cuaerto y sus ocupantes
    calculo (Valor = 155.400 * persona )

4) Salir del sistema
"""
Salir=True
Cuartos={0:'Desocupado',1:'Desocupado', 2:'Desocupado', 3:'Desocupado', 4:'Desocupado', 5:'Desocupado', 6:'Desocupado', 7:'Desocupado', 8:'Desocupado', 9:'Desocupado'}
Personas={}

def RegistrarCuarto():
    
    x=0
    while x < len(Cuartos):
        if Cuartos[x]=='Desocupado':
            print("El cuarto número ", x," esta :",Cuartos[x])
        x+=1

    repeticion=True

    while(repeticion):

        Cuartodeseado=int(input("Digite el cuarto que desea \n"))
        if Cuartodeseado>=10 or Cuartodeseado<0:
            print("Este cuarto no exite, por favor ingrese  uno valido")
        elif (Cuartos[Cuartodeseado]!='Desocupado'):
            print("Este cuarto esta ocupado, por favor ingrese uno valido")
        else:
            repeticion=False

    Cuartos[Cuartodeseado]={'Nombre':[],'Apellido':[],'Telefono':[],'Email':[]}
   
    NumeroPersonas=int(input("Digite el número de personas que se hospedaran en el cuarto \n"))
    

    n=0
    while n<NumeroPersonas: 

        NombrePersona=input("Digite el nombre del huésped:  ")
        Cuartos[Cuartodeseado]['Nombre'].insert(n,NombrePersona)
        
        ApellidoPersona=input("Digite el apellido del huésped:  ")
        Cuartos[Cuartodeseado]['Apellido'].insert(n,ApellidoPersona)

        TelefonoPersona=input("Digite el telefono del huésped:  ")
        Cuartos[Cuartodeseado]['Telefono'].insert(n,TelefonoPersona)

        EmailPersona=input("Digite el Email del huésped:  ")
        Cuartos[Cuartodeseado]['Email'].insert(n,EmailPersona)
        print("\n")
        n+=1
    
    n=0
    print("\t Información suministrada")
    while n<NumeroPersonas:
        print("\n")
        print(n+1,". ",Cuartos[Cuartodeseado]['Nombre'][n],Cuartos[Cuartodeseado]['Apellido'][n]," Telefono: ",Cuartos[Cuartodeseado]['Telefono'][n]," Email: ",Cuartos[Cuartodeseado]['Email'][n])
        n+=1

    Confirmar=True

    while(Confirmar):
        print("1. Si")
        print("2. No")
        Confirmacion=int(input("¿Desea guardar esta información? \n"))
        if Confirmacion==1:
            print("La información a sido correctamente guardada")
            Confirmar=False
        elif Confirmacion==2:
            print("\n")
            print("1. Si")
            print("2. No")
            Confirmacion2=int(input("¿Esta seguro que quiere borrar el registro? \n"))
            if Confirmacion2==1:
                Cuartos[Cuartodeseado]='Desocupado'
                Confirmar=False
            elif Confirmacion2==2:
                print("")
            else:
                print("Por favor ingrese una opcion correcta ('1' o '2'")
        else:
            print("Por favor ingrese una opcion correcta ('1' o '2'")

def ConsultarCuarto():
    x=0
    print("\t CUARTOS OCUPADOS:")
    while x < len(Cuartos):
        if Cuartos[x]!='Desocupado':
            print("Cuarto número ", x)
        x+=1
    repeticion=True
    
    while(repeticion):
        CuartoAConsultar=int(input("Digite el cuarto que desea consultar \n"))
        if CuartoAConsultar>=10 or CuartoAConsultar<0:
            print("Este cuarto no exite, por favor ingrese  uno valido")
        elif (Cuartos[CuartoAConsultar]=='Desocupado'):
            print("Este cuarto esta Desocupado, por favor ingrese uno valido")
        else:
            CantidadPersonas=int(len(Cuartos[CuartoAConsultar]['Nombre']))
            n=0
            print("\t Informacion personas en el cuarto")
            print("Personas en el cuarto:", CantidadPersonas)
            while n<CantidadPersonas:
                print("\n")
                print(n+1,". ",Cuartos[CuartoAConsultar]['Nombre'][n],Cuartos[CuartoAConsultar]['Apellido'][n]," Telefono: ",Cuartos[CuartoAConsultar]['Telefono'][n]," Email: ",Cuartos[CuartoAConsultar]['Email'][n])
                n+=1
            repeticion=False

def DesocuparCuarto():
    x=0
    print("\t CUARTOS OCUPADOS:")
    while x < len(Cuartos):
        if Cuartos[x]!='Desocupado':
            print("Cuarto número ", x)
        x+=1
    repeticion=True
    
    while(repeticion):
        DesocuparCuarto=int(input("\n Digite el cuarto que desea desocupar\n"))

        if DesocuparCuarto>=10 or DesocuparCuarto<0:
            print("Este cuarto no exite, por favor ingrese  uno valido")
        elif (Cuartos[DesocuparCuarto]=='Desocupado'):
            print("Este cuarto esta Desocupado, por favor ingrese uno valido")
        else:
            print("\n")
            print("1. Si")
            print("2. No")
            Confirmacion2=int(input("¿Esta seguro que quiere desocupar este cuarto? \n"))
            if Confirmacion2==1:
                CantidadPersonas=int(len(Cuartos[DesocuparCuarto]['Nombre']))
                print("Personas en este cuarto: ", CantidadPersonas," * 155.400, Total a cancelar: ", 155400*CantidadPersonas)
                Cuartos[DesocuparCuarto]='Desocupado'
                print("Cuarto desocupado con exito")
                repeticion=False
            elif Confirmacion2==2:
                repeticion=False
            else:
                print("Por favor ingrese una opcion correcta ('1' o '2'")

while(Salir):
    print("\n")
    print("\t MENÚ PARA RECEPCIONISTA HOTEL NN")
    print("\n")
    print("1.Registrar cuarto")
    print("2.Consultar cuarto")
    print("3.Desocupar cuarto")
    print("4.Salir")

    opcion=int(input("Digite que opción desea \n"))

    if opcion==1:
        RegistrarCuarto()
    elif opcion==2:
        ConsultarCuarto()
    elif opcion==3:
        DesocuparCuarto()
    elif opcion==4:
        print("Gracias por usar nuestro sistema, Adios")
        Salir=False
    else:
        print("Digite una opción valida")

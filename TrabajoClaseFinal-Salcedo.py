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

2) Se deben mostrar los cuartos ocupados y preguntar al usuario que cuarto quiere ver
    Mostrar la cantidad de personas en el cuarto y la infromacion de las mismas

3) Se debe preguntar cual cuarto se desocupa mostrar el valor a pagar y limpiar el cuarto y sus ocupantes
    calculo (Valor = 155.400 * persona )

4) Salir del sistema
"""


DONOMAR=[]
salir = False
while not salir:
    print("1.Registrar-cuarto")
    print("2.Consultar-personas")
    print("3.Salida-del-hotel")
    print("4.Salir-Hotel")
    opcion = input("::")
    if opcion == "1":
        print("Registrar cuarto")
        O=int(input("Cantidad de personas que se ingresan al cuarto"))
        cuarto=list()
        for x in range(O):
            nombre=input("Nombre persona ")
            print("persona # ",x+1)
            apellido=input("Apellido persona")
            print("persona # ",x+1)
            Telefono=input("Telefono")
            print("persona # ",x+1)
            email=input("Email")
            print("persona # ",x+1)
            cuarto.append(nombre)
            cuarto.append(apellido)
            cuarto.append(Telefono)
            cuarto.append(email)
            print(f" Señor/a {nombre}  {apellido} de telefono: {Telefono} y de email: {email}")
        DONOMAR.append(cuarto)
    elif opcion == "2":
        print("Consultar cuartos")
        print("Cuartos disponibles\n","#",len(DONOMAR))
        preguntaCuarto=int(input("¿Cual cuarto desea ver?"))
        print("Cuarto #",preguntaCuarto)
        print("Cantidad personas ",len((DONOMAR[preguntaCuarto-1]))/4)
        print ("Datos personas ",DONOMAR[preguntaCuarto-1])

    elif opcion == "3":
        print("Salida del hotel precio")
        print("Cuartos actuales\n","#",len(DONOMAR))
        preguntaCuarto=int(input("¿Cual cuarto se desocupa?"))
        print("Se desocupara el cuarto #",preguntaCuarto)
        print("Cantidad personas ",len((DONOMAR[preguntaCuarto-1]))/4)
        print("Cantidad personas ",len((DONOMAR[preguntaCuarto-1]))/4*155400)
        DONOMAR.pop(preguntaCuarto-1)
    elif opcion =="4":
        print("Bai Bai")
        salir = True
    else:
        print("Numero no valido")
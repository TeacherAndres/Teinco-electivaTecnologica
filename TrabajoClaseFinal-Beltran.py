#El sistema debe componer por un menu con las sigientes opciones
#1) Registrar cuarto
#2) Consultar cuatros
#3) Salida del hotel
#4) Salir del hotel
#1) Debe registrar en el cuarto (pocision sigueinte del diccionario) 
    #    Cuantas persdonas estaran en ese cuarto y por la n cantidad de personas registrar
    #    Nombre - apellidos - telefono - email 
    #    Mostrar los datos registrados apra confirmar
#2) deben mostrar los cuartos ocupados y preguntar al usuario que cuarto quiere ver
    #    Mostrar la cantida de pesonas en el cuarto y la infromacion de las mismas
#3) Se debe preguntar cual mcuarto se desocupa mostrar el valor a pagar y limpiar el cuaerto y sus ocupantes
    #    calculo (Valor = 155.400 * persona )
#4) Salir del sistema
box_hotel=[]
Contador_personas=[]
def registrarCuarto():
        print("Buenos días señor huesped en estos momentos esta en el apartado para registrar la información de las personas que se hospedaran")
        personas_Registradas=int(input("Cuantas personas se quedaran en la habitación \n"))
        Contador_personas.append(personas_Registradas)
        registro_infor=list()
        for z in range(personas_Registradas):
            nombre=input("Ingrese su Nombre\n")
            registro_infor.append(nombre)
            apellido=input("Ingrese su Apellido\n")
            registro_infor.append(apellido)
            telefono=input("Ingrese su Telefono\n")
            registro_infor.append(telefono)
            email=input("Ingrese su Email\n")         
            registro_infor.append(email)
            print("Señ@r Huesped:",nombre,apellido,"Con Telefeno:",telefono,"y con email:",email)
        box_hotel.append(registro_infor) 
        confimacion=int(input("¿Señor Huesped los datosque registro estan correctos? (Si=1 No=2)"))
        if confimacion==2:
            print("El número de cuartos que estan registrados son: ",len(box_hotel))
            cuarto_huesped=int(input("Para poder hacer el borrado de este registro,¿En que cuarto se iba a hospedar?"))
            box_hotel.pop(cuarto_huesped-1)
        elif confimacion ==1:
            print("Su información se registro correctamente")
        else:
            print("Opción erronea")

def consultaCuarto():
        print("Señor huesped en este apartado podra observar los cuartos que estan registrados ")
        print("El número de cuartos que estan registrados son: ",len(box_hotel))
        cuarto_registrado=int(input("¿Cual cuarto desea observar?\n"))
        print("El cuarto: ",cuarto_registrado)
        print("El total de personas que estan registradas son: ",Contador_personas[cuarto_registrado-1])
        print ("Los datos de las personas de ese cuarto son: \n",box_hotel[cuarto_registrado-1])


def salidaHotel():
    
        print("Señor huesped en este apartado puede realizar check out de su abitación")
        cuarto_salida=int(input("¿En que cuarto se estaba hospedando?\n"))
        print("Se desocupara el cuarto #",cuarto_salida)
        print("Las personas que estaban hospedadas en este cuarto son: ",Contador_personas[cuarto_salida-1])
        print("El valor que debe pagar es de:","$",Contador_personas[cuarto_salida-1]*155400)
        print("Gracias por hospedarce en el hotel playa blanca,que tenga un buen día")
        box_hotel.pop(cuarto_salida-1)

while True:
  print("******")
  print("Bienvenido al hotel playa blanca en el siguitente menú encontrara el registro para su habitación y salida de este mismo")
  print("1. Registrar cuarto")
  print("2. Consultar cuartos")
  print("3. Salida del hotel")
  print("4. Salir del hotel")
  print("*****")
  print("Selecione la opcion del menú a la que quiere ingresar: ")
  opcion = int(input())
  if opcion == 4:
    print("Que tenga un buen día, gracias por hospedarse en nuestro hotel")  
    break
  elif opcion == 1:
      registrarCuarto()
  elif opcion == 2:
      consultaCuarto()
  elif opcion == 3:
      salidaHotel()
    
  else:
      print("Escribio una opción que no pertenece al menú")

ContarPersonas=[]
Hotel=[] 
def RegiCuarto():
       
        PersoRegistradas=int(input("Cuantas personas se quedaran en el cuarto: \n"))
        ContarPersonas.append(PersoRegistradas)

        RegisInfo=list()
        for z in range(PersoRegistradas):

            nombre=input("Ingrese su nombre: \n")
            RegisInfo.append(nombre)

            apellido=input("Ingrese su apellido: \n")
            RegisInfo.append(apellido)

            telefono=input("Digite su telefono: \n")
            RegisInfo.append(telefono)

            email=input("Ingrese su correo: \n")         
            RegisInfo.append(email)

            print("Seño(a)r:",nombre,apellido,"telefeno:",telefono,"correo:",email)
            Hotel.append(RegisInfo) 

        Aceptar=int(input("Los datos ingresados son correctos: \n NO=1 SI=0: "))

        if Aceptar==1:
            print("Los cuartos que se han registrado: ",len(Hotel))   

        elif Aceptar==0:
            print("Se ha registrado correctamente")

        else:
            print("Error")

def RevisarCuarto():
        
        print("Los cuartos registrados son: ",len(Hotel))

while True:

  print("Bienvenido (Seleccione una opcion) ")
  print("1 Registrar un cuarto")
  print("2 Consultar los cuartos")
  print("3 Salir del hotel")

  print("Selecione una opcion: ")
  opcion = int(input())
  if opcion == 3:
    print("-- Ha salido de el hotel --")  
    break

  elif opcion == 1:
      RegiCuarto()

  elif opcion == 2:
      RevisarCuarto()

  else:
      print("Opcion incorrecta")
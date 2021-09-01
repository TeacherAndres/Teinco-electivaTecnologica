#menu

finalizar = False

while not finalizar:
    print("Menu")
    print("1.Asignar cuarto")
    print("2.Asignar datos de personas")
    print("3.Datos de las personas")
    print("4. salir")
    choice = input(":: ")
  
    if choice == "1":
        print("Asignar cuarto")


    elif choice == "2":
        print("Asignar datos de personas")

        numeropersonas=int(input("Digite cuantas personas estaran en el cuarto \n"))

        nombres=[]
        edades=[]
        acudientes=[]

        for x in range (1,numeropersonas+1):

            pedirnombre=input("Digite su nombre \n")
            nombres.insert(x,pedirnombre)

            pediredad=int(input("Digite su edad \n"))
            edades.insert(x,pediredad)

            if pediredad<18:
                pediracudiente=input("Digite el nombre de su acudiente \n")
                acudientes.insert(x,pediracudiente)

            else:
                acudientes.insert(x,"Esta persona es mayor de edad, no tiene un acudiente")


    elif choice == "3":
        print("")
    elif choice =="4":
        finalizar = True
    else:
        print("Número no valido")
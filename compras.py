#cuantos productos va a comprar 
#que producto compro 
#si lo compro por internet o lo pago en efectivo
# #efectivo 1 punto
# precencial 10 puntos
#internet 6, 



CantCompra= int(input("Digite la cantidad a comprar: "))

Puntos=0
for x in range(CantCompra):
    InfoCompra= input("Digite que va comprar: ")
    ValCompra= int(input("Digite el valor de la compra: "))
    MedCompra= int(input("Por que medio compra?:\n 1= Presencial\n 2=Internet\n 3=otro\n"))
    if(MedCompra==1):
        ValCompra+=ValCompra
        Puntos+=10
        print("Usted compro: ", InfoCompra,", por el medio de la opcion  : \n 1  Presencial\n 2 Internet\n 3 otro\n" ,MedCompra," Precio total acumulado: ",(ValCompra))
        print("Usted sumo: ",Puntos ,"  puntos acumulables")
    elif (MedCompra==2):
        ValCompra+=ValCompra
        Puntos+=6
        print("Usted compro: ", InfoCompra,", por el medio de la opcion  : \n 1  Presencial\n 2 Internet\n 3 otro\n" ,MedCompra," Precio total acumulado: ",(ValCompra))
        print("Usted sumo: ",Puntos ,"  puntos acumulables")
        

    elif (MedCompra==3):
        ValCompra+=ValCompra
        Puntos+=1
        print("Usted compro: ", InfoCompra,", por el medio de la opcion  : \n 1  Presencial\n 2 Internet\n 3 otro\n" ,MedCompra," Precio total acumulado: ",(ValCompra))
        print("Usted sumo: ",Puntos ,"  puntos acumulables")

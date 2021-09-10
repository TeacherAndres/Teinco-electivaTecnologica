#cuantos productos va a comprar 
#que producto compro 
#si lo compro por internet o lo pago en efectivo
# #efectivo 1 punto
# precencial 10 puntos
#internet 6, 



CantCompra= int(input("Digite la cantidad que compró: "))
ValorTotalAcumulado=0
Puntos=0

for x in range(CantCompra):
   
    InfoCompra= input("Digite que compró: ")
    ValCompra= int(input("Digite el valor de la compra: "))
    MedCompra= int(input("Por que medio compra?:\n 1= Presencial\n 2=Internet\n 3=otro\n 4=salir"))
    if(MedCompra==1):
        Puntos+=10
    elif (MedCompra==2):
        Puntos+=6
    elif (MedCompra==3):
        Puntos+=1  
    ValorTotalAcumulado+=ValCompra  
    print("Usted compro: ", InfoCompra,", por el medio de la opcion  : \n 1  Presencial\n 2 Internet\n 3 otro\n" ,MedCompra," Precio total acumulado: ",ValorTotalAcumulado)
    print("Usted sumo: ",Puntos ,"  puntos acumulables")


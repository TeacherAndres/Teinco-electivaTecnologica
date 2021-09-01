#cuantos productos va a comprar 
#que producto compro 
#si lo compro por internet o lo pago en efectivo
# #efectivo 1 punto
# precencial 10 puntos
#internet 6, 


InfoCompra= input("Digite que va comprar: ")
CantCompra= int(input("Digite la cantidad a comprar: "))
ValCompra= int(input("Digite el valor de la compra: "))
MedCompra= int(input("Por que medio compra?: 1= Presencial\n 2=Internet\n3=otro"))
Puntos=0
for x in range(CantCompra):
    if(MedCompra=="1"):
        ValCompra+=ValCompra
        Puntos+=10
        print("Usted compro: ", InfoCompra,"Valor"," por un valor de: ",(ValCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",Puntos ,"  puntos")
    elif (MedCompra=="2"):
        ValCompra+=ValCompra
        Puntos+=6
        print("Usted compro: ", InfoCompra,"Valor"," por un valor de: ",(ValCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",Puntos ,"  puntos")
        

    elif (MedCompra=="3"):
        ValCompra+=ValCompra
        Puntos+=1
        print("Usted compro: ", InfoCompra,"Valor"," por un valor de: ",(ValCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",Puntos ,"  puntos")
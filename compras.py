#cuantos productos va a comprar 
#que producto compro 
#si lo compro por internet o lo pago en efectivo
# #efectivo 1 punto
# precencial 10 puntos
#internet 6, 


InfoCompra= input("Digite que va comprar: ")
CantCompra= int(input("Digite la cantidad a comprar: "))
ValCompra= int(input("Digite el valor de la compra: "))
MedCompra= int(input("Por que medio compra?: "))
Puntos=0
for x in range(CantCompra):
    if(MedCompra=="1"):
        ValCompra+=ValCompra
        Puntos+=10
        print("Usted compro: ", InfoCompra,"Valor"," por un valor de: ",(ValCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",Puntos ,"  puntos")
    elif (MedCompra=="2"):
        ValCompra+=ValCompra
        print("Usted compro: ", InfoCompra," Veces por un valor de: ",(ValCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",(Puntos))
    elif (MedCompra=="3"):
        ValCompra+=ValCompra
        print("Usted compro: ", InfoCompra," ",CantCompra," Veces por un valor de: ",(ValCompra*CantCompra), "por el medio de: ",MedCompra)
        print("Usted sumo: ",(CantCompra*6))
<<<<<<< Updated upstream
#Software
#Software  || Online: 6 puntos, Presencial: 10 puntos, Otros: 1 punto

InfoCompra= input("Digite que va comprar: ")
CantCompra= int(input("Digite la cantidad a comprar: "))
ValCompra= int(input("Digite el valor de la compra: "))
MedCompra= input("Por que medio compra?: ")

if(MedCompra=="pre"):
    print("Usted compro: ", InfoCompra,"por un valor de: ",(ValCompra*CantCompra), "por el medio de: ",MedCompra)
    print("Usted sumo: ",(CantCompra*6))
else:
    print("Usted compro: ", InfoCompra,"por un valor de: ",(ValCompra*CantCompra), "por el medio de: ",MedCompra)
    print("Usted sumo: ",(CantCompra*6))

=======
InfoCompra= input("Digite que va comprar: ")
CantCompra= int(input("Digite la cantidad a comprar: "))
MedCompra= int(input("Por que medio compra?: "))
MedCompra= input("Por que medio compra?: ")
if(MedCompra=="pre"):
    print("Usted compro: ", InfoCompra," ",CantCompra," Veces por un valor de: ",(ValCompra*CantCompra), "por el medio de: ",MedCompra)
    print("Usted sumo: ",(CantCompra*6))
else:
    print("Usted compro: ", InfoCompra," ",CantCompra," Veces por un valor de: ",(ValCompra*CantCompra), "por el medio de: ",MedCompra)
    print("Usted sumo: ",(CantCompra*6))
>>>>>>> Stashed changes

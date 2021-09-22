import winsound 
def PreguntasTorturadoras():
    F=2000 #Frecuencia
    D=2000 #Duracion 



    """print("\U0001F601") #Sonriente
    print("\U0001F973") #Fiesta
    print("\U0001F640") #Gato con cara medio palida
    print("\U0001F921") #Payaso
    print("\U00002620") #Calabera
    print("\U0001F627") #Preocupado
    print("\U0001F62C") #Muelitas
    print("\U0001F631") #LaPalida
    print("\U0001F609") #Guiño
    print("\U0001F590") #Manin
    print("\U0001F914") #Duda"""
    RespCor=0

    while RespCor!=5:

        print("Holaa!!","\U0001F590","\U0001F601","Juguemos\n ")
        
        while RespCor!=1:
            print("\t Responde...","\U0001F914")
            resp=int(input("¿Cual es el resultado de 3 x 4? :\t",))
            
            if resp==3*4:
                print("¡¡YEII!! Tu respuesta es correcta","\U0001F609","\U0001F973")
                RespCor+=1
            else:
                print("\U0001F627","\U0001F62C","\U0001F640","NO YEI... Tu respuesta es incorrecta","\U0001F631","\U0001F921","\U00002620")
                winsound.Beep(F,D)
                F+=1000
                D+=1000
                if F==9000:
                    F=2000
                    D=2000
        while RespCor!=2:
            F=2000 #Frecuencia
            D=2000 #Duracion 
            print("\t Responde...","\U0001F914")
            resp=int(input("¿Cual es el resultado de 5 x 3? : \t"))
            
            if resp==5*3:
                print("¡¡YEII!! Tu respuesta es correcta","\U0001F609","\U0001F973")
                RespCor+=1
            else:
                print("\U0001F627","\U0001F62C","\U0001F640","NO YEI... Tu respuesta es incorrecta","\U0001F631","\U0001F921","\U00002620")
                winsound.Beep(F,D)
                F+=1000
                D+=1000
                if F==9000:
                    F=2000
                    D=2000
        while RespCor!=3:
            F=2000 #Frecuencia
            D=2000 #Duracion 
            print("\t Responde...","\U0001F914")
            resp=int(input("¿Cual es el resultado de 6 + 2? : \t"))
            
            if resp==6+2:          
                print("¡¡YEII!! Tu respuesta es correcta","\U0001F609","\U0001F973")
                RespCor+=1
            else:
                print("\U0001F627","\U0001F62C","\U0001F640","NO YEI... Tu respuesta es incorrecta","\U0001F631","\U0001F921","\U00002620")
                winsound.Beep(F,D)
                F+=1000
                D+=1000
                if F==9000:
                    F=2000
                    D=2000
        while RespCor!=4:
            F=2000 #Frecuencia
            D=2000 #Duracion 
            print("\t Responde...","\U0001F914")
            resp=int(input("¿Cual es el resultado de 6 - 4? : \t"))
            
            if resp==6-4:
                print("¡¡YEII!! Tu respuesta es correcta","\U0001F609","\U0001F973")
                RespCor+=1
            else:
                print("\U0001F627","\U0001F62C","\U0001F640","NO YEI... Tu respuesta es incorrecta","\U0001F631","\U0001F921","\U00002620")
                winsound.Beep(F,D)
                F+=1000
                D+=1000
                if F==9000:
                    F=2000
                    D=2000
        while RespCor!=5:
            F=2000 #Frecuencia
            D=2000 #Duracion 
            print("\t Responde...","\U0001F914")
            resp=int(input("¿Cual es el resultado de 10 / 2? : \t"))
            
            if resp==10/2:
                print("¡¡YEII!! Tu respuesta es correcta","\U0001F609","\U0001F973")
                print("¡¡GRACIAS POR JUGAR!! Vuelve pronto","\U0001F590","\U0001F60E")
                RespCor+=1
            else:
                print("\U0001F627","\U0001F62C","\U0001F640","NO YEI... Tu respuesta es incorrecta","\U0001F631","\U0001F921","\U00002620")
                winsound.Beep(F,D)
                F+=1000
                D+=1000
                if F==9000:
                    F=2000
                    D=2000
PreguntasTorturadoras()
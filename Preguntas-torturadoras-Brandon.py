import winsound

#Declarar variables
F=2000
D=2000

ciclo=True
respuesta=True
pregunta=0
print("\n \tBienvenido a su consurso preferido !Si logras 5 puntos ganas!")

while(ciclo):

    #Resetear frecuencia y duracion
    if F==9000:
        F=2000
        D=2000

    #Pregunta 1
    if pregunta==0:
        respuesta=True
        while(respuesta):
            Respuesta1=input("\n \t¿Cuanto es 20 + 11?\n")
            if Respuesta1 == "31":
                print("\U0001F63B Bien hecho ganaste 1 punto \U0001F63B")
                pregunta+=1
                respuesta=False
            else:
                print("\U0001F62A MAL \U0001F62A")
                winsound.Beep(F,D) 
                F+=1000
                D+=1000

    #Pregunta 2
    elif pregunta==1:
        print("\t ¿Un cerdo puede mirar hacia arriba?\n")
        print("1. Si")
        print("2. No")
        respuesta=True
        while(respuesta):

            Respuesta2=input("Digita 1 para si o 2 para no\n")
            if Respuesta2 == "2":
                print("\U0001F63B Bien hecho ganaste 1 punto \U0001F63B")
                pregunta+=1
                respuesta=False
            else:
                print("\U0001F62A MAL \U0001F62A")
                winsound.Beep(F,D) 
                F+=1000
                D+=1000

    #Pregunta 3
    elif pregunta==2:
        respuesta=True
        while(respuesta):
            Respuesta3=input("\t ¿Cuanto es 23 + 45? \n")
            if Respuesta3 == "68":
                print("\U0001F63B Bien hecho ganaste 1 punto \U0001F63B")
                pregunta+=1
                respuesta=False
            else:
                print("\U0001F62A MAL \U0001F62A")
                winsound.Beep(F,D) 
                F+=1000
                D+=1000
    
    #Pregunta 4
    elif pregunta==3:
        respuesta=True
        while(respuesta):
            Respuesta4=input("\t ¿Cuanto es 500 + 200?\n")
            if Respuesta4 == "700":
                print("\U0001F63B Bien hecho ganaste 1 punto \U0001F63B")
                pregunta+=1
                respuesta=False
            else:
                print("\U0001F62A MAL \U0001F62A")
                winsound.Beep(F,D) 
                F+=1000
                D+=1000

    #Pregunta 5
    elif pregunta==4:
        print("\t ¿Los elefantes pueden saltar?\n")
        print("1. Si")
        print("2. No")
        respuesta=True
        while(respuesta):

            Respuesta4=input("Digita 1 para si o 2 para no\n")
            if Respuesta4 == "2": 
                print("\U0001F63B Bien hecho ganaste 1 punto \U0001F63B")
                pregunta+=1
                respuesta=False
            else:
                print("\U0001F62A MAL \U0001F62A")
                winsound.Beep(F,D) 
                F+=1000
                D+=1000

    if pregunta==5:
        print("\U0001F63B \U0001F63B \U0001F63B!Bien hecho tu ganas! \U0001F63B \U0001F63B \U0001F63B")
        ciclo=False

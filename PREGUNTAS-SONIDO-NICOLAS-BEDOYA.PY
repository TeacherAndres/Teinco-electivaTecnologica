import winsound
print("----- \U0001F600 PREGUNTAS MATEMATICAS (BASICAS) \U0001F600 -----")

#Pregunta1
p1= int(input("1.  ¿Cuanto es 2+2?: \n"))
f=4000 #frecuencia
d=2000 #duracion
while p1 !=4:
    print("Respuesta incorrecta")
    f+=1000
    d+=1000 
    winsound.Beep(f,d)
    p1= int(input("1.  ¿Cuanto es 2+2?: \n"))
    
    
#Pregunta2
p2= int(input("Respuesta Correcta \U0001F600 \n 2.  ¿Cuanto es 12+1?: \n"))
f=4000 #frecuencia
d=2000 #duracion
while p2 !=13:
    print("Respuesta incorrecta")
    f+=1000
    d+=1000 
    winsound.Beep(f,d)
    p2= int(input("2.  ¿Cuanto es 12+1?: \n"))

#Pregunta3
p3= int(input("Respuesta Correcta \U0001F600 \n 3.  ¿Cuanto es 100-99?: \n"))
f=4000 #frecuencia
d=2000 #duracion
while p3 !=1:
    print("Respuesta incorrecta")
    f+=1000
    d+=1000
    winsound.Beep(f,d)
    p3= int(input("3.  ¿Cuanto es 100-99?: \n"))

#Pregunta4
p4= int(input("Respuesta Correcta \U0001F600 \n 4.  ¿Cuanto es 5x5?: \n"))
f=4000 #frecuencia
d=2000 #duracion
while p4 !=25:
    print("Respuesta incorrecta")
    f+=1000
    d+=1000
    winsound.Beep(f,d)
    p4= int(input("4.  ¿Cuanto es 5x5?: \n"))

#Pregunta5
p5= int(input("Respuesta Correcta \U0001F600 \n 5.  ¿Cuanto es 10/2?: \n"))
f=4000 #frecuencia
d=2000 #duracion
while p5 !=5:
    print("Respuesta incorrecta")
    f+=1000
    d+=1000
    winsound.Beep(f,d)
    p5= int(input("5.  ¿Cuanto es 10/2?: \n"))


print("----- \U0001F609 FIN DE LAS PREGUNTAS \U0001F609 -----")

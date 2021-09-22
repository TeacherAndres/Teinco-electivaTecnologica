"""
Cree un programa que realice 5 preguntas matemáticas a un usuario (Fáciles)
cada vez que el usuario se equivoque el sistema desplegara un sonido (Frecuencia / duración inicial 2000)
y por cada vez  que se equivoque el sistema cambiara la frecuencia y aumentara la duración del sonido.
Hasta que responda bien las 5 preguntas.

import random
numero = random.randint(1, 6)

print(numero)
"""
import random
import winsound
import os
def menu():
    os.system('cls')
    print("──────▄▀▄─────▄▀▄\n─────▄█░░▀▀▀▀▀░░█▄\n─▄▄──█░░░░░░░░░░░█──▄▄\n█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")
    print("PREGUNTAS TORTURADORAS \U0001F47A", "\U0001F4A3")
    print("La puntuacion actual es de: ",puntos," \U0001F632")
    print ("1. Pregunta #01 SUMA")
    print ("2. Pregunta #02 RESTA")
    print ("3. Pregunta #03 MULTI")
    print ("4. Pregunta #04 DIVISION")
    print ("5. Pregunta #05 EXPONENTE")
    print ("9. Salir")

global puntos
global frecuencia
global duracion

def pre1():
    print("Pregunta #01: ")
    global puntos
    global frecuencia
    global duracion
    while True:
        print("¿Cúal es el resultado de la suma de 2 + 3? ")
        r1=int(input("Digite el resultado: "))
        if(r1!=5):
            frecuencia= random.randint(1000,8000)
            duracion+=1000
            print("Repuesta incorrecta! \U0001F616 Frecuencia actual: ",frecuencia," duracion actual: ",duracion)
            winsound.Beep(frecuencia,duracion)
        else:
            print("Respuesta correcta: \U0001F917")
            puntos+=1
            break

def pre2():
    print("Pregunta #02: ")
    global puntos
    global frecuencia
    global duracion
    while True:
        print("¿Cúal es el resultado de la resta de 7 - 5: ")
        r2=int(input("Digite el resultado: "))
        if(r2!=2):
            frecuencia= random.randint(1000,8000)
            duracion+=1000
            print("Repuesta incorrecta! \U0001F616 Frecuencia actual: ",frecuencia," duracion actual: ",duracion)
            winsound.Beep(frecuencia,duracion)
        else:
            print("Respuesta correcta: \U0001F917")
            puntos+=1
            break

def pre3():
    print("Pregunta #03: ")
    global puntos
    global frecuencia
    global duracion
    while True:
        print("¿Cúal es el resultado de la multiplicacion de 3 * 3: ")
        r3=int(input("Digite el resultado: "))
        if(r3!=9):
            frecuencia= random.randint(1000,8000)
            duracion+=1000
            print("Repuesta incorrecta! \U0001F616 Frecuencia actual: ",frecuencia," duracion actual: ",duracion)
            winsound.Beep(frecuencia,duracion)
        else:
            print("Respuesta correcta: \U0001F917")
            puntos+=1
            break

def pre4():
    print("Pregunta #04: ")
    global puntos
    global frecuencia
    global duracion
    while True:
        print("¿Cúal es el resultado de la division entre 1/1: ")
        r4=int(input("Digite el resultado: "))
        if(r4!=1):
            frecuencia= random.randint(1000,8000)
            duracion+=1000
            print("Repuesta incorrecta! \U0001F616 Frecuencia actual: ",frecuencia," duracion actual: ",duracion)
            winsound.Beep(frecuencia,duracion)
        else:
            print("Respuesta correcta: \U0001F917")
            puntos+=1
            break

def pre5():
    print("Pregunta #05: ")
    global puntos
    global frecuencia
    global duracion
    while True:
        print("¿Cúal es el resultado de la potencia de 2'2: ")
        r5=int(input("Digite el resultado: "))
        if(r5!=4):
            frecuencia= random.randint(1000,8000)
            duracion+=1000
            print("Repuesta incorrecta! \U0001F616 Frecuencia actual: ",frecuencia," duracion actual: ",duracion)
            winsound.Beep(frecuencia,duracion)
        else:
            print("Respuesta correcta: \U0001F917")
            puntos+=1
            break

puntos = 0
duracion =2000
frecuencia =0

while puntos<5:
    menu()
    opcionMenu = input("Ingrese una opción valida: ")
    if opcionMenu=='1':
        pre1()
        input("Salir: ")
    elif opcionMenu=='2':
        pre2()
        input("Salir: ")
    elif opcionMenu=='3':
        pre3()
        input("Salir: ")
    elif opcionMenu=='4':
        pre4()
        input("Salir: ")
    elif opcionMenu=='5':
        pre5()
        input("Salir: ")
    elif opcionMenu=="9":
        break
    else: 
        input("No ha pulsado una opcion valida: ")
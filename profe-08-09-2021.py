#Definir y crear diccionario (perro)
perro = {'dueño': 'Federiko','raza':'canino','vacunas':['tosferina','rabia','cancha']}
#Imprimir diccionario perro
print(perro)
#Imprimir valor por la llave
print(perro['dueño'])
#Imprimir valor por llave y pocision interna
print(perro['vacunas'])
print(perro['vacunas'][0])
print(perro['vacunas'][2])
#ZIP
print("******************** ZIP ***************")
diccionariobasico = dict(zip('abcd',[1,2,3,4]))
print(diccionariobasico)
#KEYS
print("******************** KEYS ***************")
keys=perro.keys()
print(keys)
#VALUES
print("******************** VALUES ***************")
valores=perro.values()
print(valores)
#COPY
print("******************** COPY ***************")
perro2 = perro.copy()
print(perro2)
#FROMKEYS
print("******************** FROMKEYS ***************")
perro3 = perro2.fromkeys(['a','b','c','d','e'],1)
print(perro3)
#get()
print("******************** GET ***************")
valorI = perro2.get('dueño')
print(valorI)
#pop()
print("******************** POP ***************")
dic = {'a':1,'b':2,'c':3,'d':4}
print(dic)
dic.pop('b')
dic.pop('c')
print(dic)
#setdeault
print("******************** setdeault ***************")
dic = {'a':1,'b':2,'c':3,'d':4}
valor = dic.setdefault('a')
print(dic)
valor = dic.setdefault('e',['a','b','c'])
print(dic)
print(dic['e'][2])
#INSERT
print("******************** INSERT ***************")
datosUsr = []
print(datosUsr)
datosUsr.insert(0,'pepe')
datosUsr.insert(1,'majarrez')
datosUsr.insert(2,'limonche')
print(datosUsr)
#UPDATE
print("******************** UPDATE ***************")
dicI = {'a':1,'b':2,'c':3,'d':4}
discS = {'a':1,'b':2,'e':3,'f':4}

dicI.update(discS)
print(dicI)
dict= {'valorUltimo':'este es'}
dicI.update(dict)
print(dicI)
# SEGUNDA FORMA DE CREAR UN DICCIONARIOS
"""

print("******************** CREAR DICCIONARIO SEGUNDA FORMA  ***************")
d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])
print (d2)
"""
#FOR
print("******************** RECORRE DICCIONARIO ***************")
for x in perro:
    print(perro[x])

#ANIDAR DICCIONARIO
print("******************** ADICIONAR DICCIONARIO ***************")

dicI = {'a':1,'b':2,'c':3,'d':4}
discS = {'nombre':'Raul','apellido':'MElano','Telefono':312313,'direccion':'CALLE falas 123'}

a = {
    "dicLEtras":dicI,
    "dicDatosPEr":discS
}
print(a)
print("******************** ADICIONAR DICCIONARIO DENTRO DE DICCIONARIO ***************")

b = {
    "dicDatosPerro":perro,
    "dicCumpuestoI":a
}
print(b)
print(b.get('dicCumpuestoI'))

#Nicolas Bedoya
print(b.get('dicCumpuestoI')
.get('dicDatosPEr')
.get('direccion'))
#Nicolas Bedoya






#Brandon Rodriguez print(b.get('dicCumpuestoI').get('dicDatosPEr').get('direccion'))
















#direccion= b.get('dicCumpuestoI').get('dicDatosPEr').get('direccion')
direccion= b.get('dicCumpuestoI')
#dir= direccion.get('dicDatosPEr')
final=dir.get('direccion')
#print("la direccion es: ",direccion)
print("la direccion es: ",final)
#Andres Leiva
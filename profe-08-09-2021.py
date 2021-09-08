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

dicI.update({'f':4,'h':5})
print(dicI)
dict= {'valorUltimo':'este es'}
dicI.update(dict)
print(dicI)

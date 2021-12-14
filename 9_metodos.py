# lo metodos para manipular texto son modificadores de strings, quiere decir qe puedo modificar la variable que contega un string o cadena de texto, por ejemplo pasar de mayus a minusculas
# como veremos a continuacion'


""" .upper(): pasa todo en mayúscula.

.capitalize(): solo pasa en mayúscula la primera letra.

.strip(): borra los espacios de sobre que tenga la cadena de caracteres.

.lower(): pasa todo a minúscula.

.replace(a,b): remplaza letras. Primero va qué letra se quiere reemplazar & luego a cuál se quiere pasar.

.len(): te dice cuantos caracteres tiene el string (o cadena de caracteres, es lo mismo). Es aplicable para una variable o en darle un string dentro de len. """

nombre = "erika"
nombre = nombre.upper()# en este ejemplo se esta modificando el nompre y se pone en mayuscula totalmente
print(nombre)

nombre = nombre.lower() # en este ejemplo se usa lower para cambiar la variable nombre a minuscuklas
print(nombre)

nombre = nombre.capitalize()
print(nombre) #en este ejemplo estamos colocando el nombre con la primera letra en mayusculas

nombre = nombre.strip() #en este ejemplo se le quitan los espcacios que hayan al inicio o al final de cada palabra
print(nombre)

nombre = ("erika")
nombre = nombre.replace("e", "o") # en este ejemplo reemplazamos  las letras e de la variable por o, se debe escribir el parametro dentro de la funcion en comillas""" recordando que es u string y separado por cuma coma
print(nombre)

len(nombre) #con este parametro podemos saber cuantas letaras tiene el string

nombre[2] #esto se llama indice y es la forma de acceder a los caracteres de cada string.
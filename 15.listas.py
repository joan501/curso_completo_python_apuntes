# las LISTAS es una coleccion de datos agrupados dentro  de corchetes []
#"la sintaxis de la lista seria ingresar valores dentro de los corchetes seguidos de comas 
#['perro',1,'ojo',34,False]"

lista = ['perro',1,5,9,'socio',3,4]
#tambien podemos agregar elementos a la lista
#metodos para manipular 
lista.append(4)#metodo apend agrega un elemento a la lista
#lista.clear()#elimina los elementos dentro de la lista
lista2 = lista.copy() #aqui estoy copiando los valores de la lista1 a la lista 2
#print(lista)
#print(lista2)
#print(lista2.count(4))#para contar los elementos dentro de la lista se pone el metodo .count()y dentro del()se pone el elemento que quieres contar como en el ejemplo
                      #se pone print(lista2.count(4))aqui queremos ver cuantas veces se repite el 4 en la lista deberia devolver 1vez 
#para contar los elementos dentro de la lista pero globalmente queremos saber cuantos hay y no especificamenta como el metodo .count en el conteo globalo lo que hacemos es lo siguiente:
#print(len(lista),len(lista2))#en este caso usariamos la funcion len() y dentro de los parentesis iria 
#tambien puedo poder el len en una variable y contar los elementos como se muestra a continuacion
largoLista1 = len(lista)
largoLista2 = len(lista2)
print(largoLista1,largoLista2)#metemos la funcion len en una variable 

#tambien podemos acceder a los elementos de un arreglo en una lista usando el indice, puedo acceder al elemento con la sintaxis lista[0] solo se puede un numero porque son indicies
#print(lista[4])

#como eliminamos elementos de una lista usando el metodo .pop()
lista.pop()#pop elimina el ultimo elemento de la lista y tambien como funciona el indice, si pones el numero del indice que quieras borrar lo borra ()
#para eliminar un elemento en particular usamos el metodo .remove
lista.remove('socio')#en este punto eliminamos el string socio, o sea eliminamos un elemento en especifico.
lista.reverse() #metodo .reverse cambia el orden de atras para adelante de la lista 
lista.sort()# este metodo ordena los elementos de la lista pero solo puede ordenar elementos del mismo tipo

# los siguientes son metodos que se pueden aplicar a las listas 
lista = [1,3,5,7,9,10]
lista.append(3)#puedes agregar un elemento al final puede ser cualquier tipo de dato
lista.clear()#eliminas todos los elementos de la lista dejando una lista vacia
lista.extend(lista2)#sirve para unir listas como si se estuvieran sumando las dos, en el ejemplo se muestra como se suma la lista 1 con la 2
lista.count(10)#cuenta el numero de veces que se encuentran en la lista en el ejemplo pongo el numero 10 que seria el elemento que quiero ver cuantas veces aparece que seria 1 
lista.index(3)#retorna el indice en el que se encuentra ubicado el elemento que buscamos en elejemplo seria el indice 1
lista.insert(0,0)#agrega un elemento en la posicion de indice que se especifica en el ejemplo se agrega el 0 en el indice 0 quedando en la primera posicion
                 # (0,0) agrega el 0 en el indice 0 posicionandolo  de primeras 
                 # (-1,0) 'penultima posicion' pone el elemento en la penultima posicion 
                 # (999,35) si el indice esta fuera de rango o sea que no existe el elemento se pone al final de la lista
lista.pop() #pop elimina el ultimo elemento de la lista y tambien como funciona el indice, si pones el numero del indice que quieras borrar lo borra ()
lista.reverse() #metodo .reverse cambia el orden de atras para adelante de la lista pero si el elemento esta repetido borra el primero
lista.reverse() #metodo .reverse cambia el orden de atras para adelante de la lista 
lista.sort()# este metodo ordena los elementos de la lista pero solo puede ordenar elementos del mismo tipo
            #podemos utilizar el argumento reverse=true para que lo ordene al reves lista.sort(reverse=True)
            

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

#tambien podemos acceder a los elementos de un arreglo en una lista 
print(lista[4])
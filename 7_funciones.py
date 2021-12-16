""" def mensaje_funciones(): esta es al forma de declarar las funciones para no repetir
    print ("hola como estas ")
    print ("estas aprendiendo funciones")

mensaje_funciones()
mensaje_funciones()
mensaje_funciones()
"""
""" # crear la funcion se declaran las funciones antes del codigo 
def mensaje_entrada(opcion_elegida): # se debe escribir def y luego el nombre de la funcion, los parametros van dentro del parentesis y van en orden de llegada para la ejecucion
    print("hola")
    print("como estas")
    print(opcion_elegida) #el parametro senalado aqui es el mismo que esta en los parentesis de las funciones 
    print("adios")

opcion = int(input("escoge una opcion (1,2,3): " ))

if opcion == 1:
    mensaje_entrada("elegiste la opcion 1") #la forma de usar la funcion para no repetir codigo es pegando el nombre de la funcion que pusiomos cuando la declaramos con los parentesis y sin los puntos
elif opcion == 2:
    mensaje_entrada("elegiste la opcion 2") #el parametro que esta dentro de los parentesis seran reemplazados arriba en la declaracion de la funcion en su respectivo orden
elif opcion == 3:
    mensaje_entrada("elegiste la opcion 3")
else:
    print("escribe una opcion correcta") """

# built in funciones que ya vienen con python como lo son print() float() y otras https://docs.python.org/3/library/functions.html
 




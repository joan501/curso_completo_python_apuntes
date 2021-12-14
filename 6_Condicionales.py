def conversor(tipo_de_pesos, valor_dolar):
    pesos = float(input("cuantos pesos" + tipo_de_pesos +  " tienes?:   "))
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print ("tienes $" +  dolar + " dolares" )
    



menu = """Bienvenido al conversor de monedas mas chingon de todos, a continuacion vas a tener un menu 

          1-pesos colombianos a dolar
          2-pesos argentinos a dolar
          3-pesos mexicanos a dolar 

Elige una opcion: """       
opcion = int(input(menu))

if opcion == 1:
    conversor(" colombianos", 3700)
elif opcion == 2:
    conversor(" argentinos", 74)
elif opcion == 3:
    conversor(" mexicanos", 24)
else:
    print("escriba una opcion correcta")    
     







"""

if opcion == 1: #if significa la condicion de si->seguido de la condicion que se usaria, ejemplo si la opcion 1 es igual a 1 debes hacer lo siguiente
    pesos = float(input("cuantos pesos Colombianos tienes?:  "))
    valor_dolar = 3776.05
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print ("tienes $" +  dolar + " dolares" )
elif opcion == 2: #elif signidfica sino si o sea si no se usa la de arriba pero si se da esta condicion se salta la de arriba y ejecuta la de abajo
    pesos = float(input("cuantos pesos Argentinos tienes?:  "))
    valor_dolar = 0.010
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print ("tienes $" +  dolar + " dolares" )
elif opcion == 3:
    pesos = float(input("cuantos pesos Mexicanos tienes?:  "))
    valor_dolar = 0.20
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print ("tienes $" +  dolar + " dolares" )
else: # la condicion else significa si no o sea si no cumple con nimguna de las condiciones anteriores deberia hacer esta 
    print("Elige una opcion valida") """




































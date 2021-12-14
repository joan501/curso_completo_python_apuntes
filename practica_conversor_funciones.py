

def conv_mone(tipo_pesos, valor_dolar):
    pesos = float(input("cuantos pesos" + tipo_pesos + " tienes?:  "))
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print ("tienes $" +  dolar + " dolares" )



menu =  """Bienvenido al conversor de monedas mas chingon de todos, a continuacion vas a tener un menu 

          1-pesos colombianos a dolar
          2-pesos argentinos a dolar
          3-pesos mexicanos a dolar 

Elige una opcion: """       
opcion = int(input(menu))

if opcion == 1:
    conv_mone("pesos colombianos", 3891)
elif opcion == 2: 
    conv_mone("pesos argentinos", 101.26)
elif opcion == 3:
    conv_mone("pesos mexicanos", 20.88)
else: 
    print("Elige una opcion valida")
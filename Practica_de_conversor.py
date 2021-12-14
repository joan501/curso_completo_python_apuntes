pesos = float(input("cuantos pesos colombianos tienes?:  "))
valor_dolar = 3776.05
dolar = pesos / valor_dolar
dolar = round(dolar, 2)
dolar = str(dolar)
print ("tienes $" +  dolar + " dolares" )



print(""" hola ya sabes cuantos dolares tienes pero en marte debes pagar por tu peso""")
peso_tierra = float(input("escribe tu peso actual en kilogramos:  "))
gravedad_tierra = 9.8
gravedad_marte = 3.711
peso_marte = peso_tierra / gravedad_tierra * gravedad_marte
peso_marte = round(peso_marte,2)
peso_marte = str(peso_marte)
print("tu peso en marte es " + peso_marte + " kilos")

if peso_marte >= "100":
    print("estas gordo y pagas recargo")

else:
    print("estas bien no pagas nada")


         

                                                                                         
                                                                            
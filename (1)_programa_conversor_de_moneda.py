pesos = float(input("cuantos pesos colombianos tienes?: "))
valor_dolar = 3872
dolares = pesos / valor_dolar
dolares = round( dolares ,2)
dolares = str(dolares)
print("tienes $" + dolares + "dolares")



print("quieres saber tu peso en marte, escribe tu peso en la tierra a continuacion >>>")
peso_tierra = int(input("escribe tu peso en la tierra kilos:   ")) 
gravedad_tierra = 9.81
gravedad_marte = 3.711
peso_marte = peso_tierra / gravedad_tierra * gravedad_marte
peso_marte = round(peso_marte,2)
peso_marte = str(peso_marte)
print( "tu peso en marte es: " + peso_marte + " kilos"  )
print("Porque en marte peses menos no quiere decir que no estas gordo-(a) en la tierra")

if peso_marte > "50":
    print("estas gordo papa")

else:
    print("tu peso esta bien bye")








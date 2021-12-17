""" # bucle "while" es el mas importante

contador = 0 #la variables cotador seria la potencia 
print("2 elavado a " + str(contador) + "es igual a :" + str(2**contador)) # en bucles tratamos de hacer el proceso sin repetir el codigo  """

def run():
    LIMITE = 1000000000000 # AL cambiar la variable por mayuscula se vuelve una constante que nunca cambia este es el limite y esta variable no deberia cambiar, a lo largo del programa esta variable siempre sera 1000, las potencias no deberian sr mas de mil
    
    contador = 0 # esta seria la que va a ir aumentando para multiplicar el exponencte del programa
    potencia_2 = 2**contador # la variable potencia 2 llevara la variable contador que es la que ira aumentando
    while potencia_2 < LIMITE: # WHILE es el ciclo y nos dice: mientras la variable potencia_2 (que es la que se va a multiplicar por el contador) sea menor 
        print("2 elavado a " + str(contador) + " es igual a :" + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador   

if __name__ == "__main__":#recuerda el entripoint simepre, empezara corriendo nuestra funcion principal
    run()
    

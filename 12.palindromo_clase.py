      #""" debemos crear una funcion principal que corra el programa puede ser (run) o (main) como se encuentra a continuacion """

def palindromo(palabra):#5 creo la funcion palindromo 
    palabra = palabra.replace(" ","")#6 reemplazo los espacion por sin espacion  usando el metodo .replace (" ","") asi se quita el espacio
    palabra = palabra.lower() #7 la variable palabra la la paso a minusculacon el .lower
    palabra_inver = palabra[::-1] #8  uso el indice que es[] no pongo numeros pero si pongo el -1 para que la palabra se lea al dercho y al reves 
    if palabra == palabra_inver: # escribo los condicionales si es vedadeo o falso y listo
       return True
    else:
        return False


def run(): # pasos asi: 1 empezamos con la funcion pincipal
    palabra = input("escrie una palabra: ") # 2 la variabale palabra  pide que escribas una palabra mediante un input 
    es_palindromo = palindromo(palabra) #3 creo una funcion para saber si es palindromo con los parametros de su funcionalidad que seria la funcion de arrriba 
    if es_palindromo == True:#4 creo una condicional que printe si es_palindromo es verdad o falso me diga es o no es palindromo  
        print("es palindromo")
    else:
        print("no es palindromo")
# el entripoint es el punto de entrada de un progrma de python, ahi es donde se empieza y se debe escribir asi como esta
# se pone if __name__(dos guiones bajos antes y despues) == "__main__" cuando pytho lee esto empieza a correr todo lo que se ecuenrra abajo de el
if __name__ == "__main__":
    run()





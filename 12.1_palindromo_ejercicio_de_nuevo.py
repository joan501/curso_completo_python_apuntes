def es_pal(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else: False


def run():
    palabra = input("escribe ua palabra: ")
    es_palindromo = es_pal(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ == "__main__":
    run()

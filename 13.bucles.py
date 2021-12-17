def main():
    print("deseas continuar con el  programa?")
    palabra_si = input("escribe Y para continuar o N para parar: ")

    while palabra_si == "y":
        palabra_si = input("escribe Y para continuar o N para parar: ")
    print("fin del programa")

if __name__=="__main__":
    main()

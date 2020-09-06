def caracteres(letras):

    primero = letras[0]
    ultimo = letras[len(letras) - 1]
    return(primero,ultimo)

def main():

    letras = input("Introduzca una la palabra deseada: ")
    (Uno,Dos) = caracteres(letras)
    print("Primer caracter: ",Uno)
    print("Ultimo caracter: ",Dos)

if __name__ == '__main__':
    main()
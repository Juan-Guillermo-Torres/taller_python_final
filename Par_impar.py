def par_impar(num):

    if num % 2 == 0:
        return True
    else:
        return False

def main():

    num = int(input("Introduzca un numero deseado: "))
    print("Numero par" if par_impar(num) is True else "Numero impar")

if __name__ == '__main__':
    main()
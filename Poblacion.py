def main():

    primeraPoblacion = 35
    segundaPoblacion = 19.9
    primeraTasa = 0.02
    segundaTasa = 0.03

    while primeraPoblacion > segundaPoblacion:
        primeraPoblacion = primeraPoblacion + (primeraPoblacion * primeraTasa)
        segundaPoblacion = segundaPoblacion + (segundaPoblacion * segundaTasa)


    print("Sera superior a los ",segundaPoblacion," millones de habitantes")

if __name__ == "__main__":
    main()
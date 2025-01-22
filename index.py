valore = input("Che operazione vuoi fare : \n 1) Somma \n 2) Sottrazione \n 3) Moltiplicazione \n 4) Divisione \n")

numero1 = input("Inserisci il primo numero: ")
numero2 = input("Inserisci il secondo numero: ")

numero1 = int(numero1)

numero2 = int(numero2)

match valore:
    case "1":
        print(numero1+numero2)
    case "2":
        print(numero1-numero2)
    case "3":
        print(numero1*numero2)
    case "4":
        print(numero1/numero2)
    

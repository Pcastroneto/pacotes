# AO inves de usarmos varias linhas para um erro podemos por varios erros em uma linha só

while True:
    try:
        numero = int(input("Enter an int numero: "))
        print(5/numero)
        break
    except(ValueError, ZeroDivisionError):
        print("Valor errado ou Não é possivel dividir por zero.")
    except:
        print("Desuclpe, algo errado aconteceu...")

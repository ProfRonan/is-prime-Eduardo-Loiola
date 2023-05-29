num = int(input("Digite um número inteiro: "))
if num <= 0:
    print("Número inválido")
else:
    is_prime = True
    if num == 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print("Primo")
    else:
        print("Não primo")

número = int(input("Digite um número inteiro: "))
while número <= 0:
    print("Número inválido")
    número = int(input("Digite um número inteiro: "))
ser_primo = True
i = 2
while i < número:
    if número % i == 0:
        ser_primo = False
        break
    i += 1
if ser_primo:
    print("Primo.")
else:
    print("Não primo.")
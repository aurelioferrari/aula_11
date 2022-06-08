n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 == n2:
    print("Os valores são iguais.")
elif n1 > n2:
    print("O \033[1:31mprimeiro\033[m número é maior.")
elif n2 > n1:
    print("O segundo número é maior.")
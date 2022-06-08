preco = float(input("Qual o preço do produto? "))

print("Digite 1 para ver o preço à vista no dinheiro ou cheque.")
print("Digite 2 para ver o preço à vista no cartão.")
print("Digite 3 para ver o preço pagando em 2x no cartão.")
print("Digite 4 para ver o preço pagando em 3x ou mais no cartão.\n")

opcao = int(input("Digite a opção desejada: "))

while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    print("Você digitou uma opção inválida.")
    opcao = int(input("Digite a opção desejada: "))


while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        valor = preco*0.9
        print("O preço final é: R${:.2f}".format(valor))
        opcao = 5
    elif opcao == 2:
        valor = preco*0.95
        print("O preço final é: R${:.2f}".format(valor))
        opcao = 5
    elif opcao == 3:
        valor = preco
        print("O preço final é: R${:.2f}".format(valor))
        opcao = 5
    elif opcao == 4:
        valor = preco*1.2
        print("O preço final é: R${:.2f}".format(valor))
        opcao = 5

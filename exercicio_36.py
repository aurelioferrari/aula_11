valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos você quer pagar? "))
meses = anos*12

prestacao = valor_casa / meses
salario_30 = salario*0.3

if prestacao <= salario_30:
    print("O valor da prestação é: \033[1mR${:.2f}".format(prestacao))
else:
    print("Você não poderá financiar a casa.")
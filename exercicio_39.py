from datetime import date

nascimento = int(input("Em qual ano você nasceu? "))

data_atual = date.today().year

idade = data_atual - nascimento

if idade == 18:
    print("Gora de se alistar!")
elif idade < 18:
    print("Você ainda vai se alistar!")
    print("Você vai se alistar daqui a {} anos".format(18 - idade))
elif idade > 18:
    print("Você passou do tempo se alistar!")
    print("Você deveria ter se alistado há {} anos".format(idade - 18))
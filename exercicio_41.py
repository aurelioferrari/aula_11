from datetime import date

nascimento = int(input("Em qual ano você nasceu? "))

data_atual = date.today().year

idade_atleta = data_atual - nascimento

if idade_atleta <= 9:
    print("Categoria Mirim.")
elif idade_atleta > 9 and idade_atleta <= 14:
    print("Categoria Infantil.")
elif idade_atleta > 14 and idade_atleta <= 19:
    print("Categoria Junior.")
elif idade_atleta == 20:
    print("Categoria Sênior.")
elif idade_atleta > 20:
    print("Categoria Master.")
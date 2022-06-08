n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print("\033[1:31mReprovado.")
elif media >= 5 and media < 7:
    print("Você está de recuperação!")
elif media >= 7:
    print("Você foi aprovado.")
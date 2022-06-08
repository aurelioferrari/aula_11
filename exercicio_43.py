peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual a sua altura em metros? "))

imc = peso / (altura**2)

print("O seu IMC é {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <25:
    print("Você está no peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso")
elif imc >= 30 and imc < 40:
    print("Você está com obesidade.")
elif imc >= 40:
    print("Você está com obesidade mórbida.")
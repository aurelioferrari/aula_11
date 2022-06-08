import random
from time import sleep
lista = ["pedra", "papel", "tesoura"]

jogador = str(input("Digite a opção que você quer (pedra / papel / tesoura): "))

print("Hmm...")
sleep(1)
print("Você sabe que eu sei o que você escolheu, né? ")
sleep(2)
print("Brincadeirinha.")

i = random.randint(0, 2)

pc = lista[i]

print("Eu escolhi \033[1:31m{}\033[m".format(pc))

sleep(1)
# o jogador perde

if pc == "tesoura" and jogador == "papel":
    print("Haha Você perdeu!")
if pc == "pedra" and jogador == "tesoura":
    print("Haha Você perdeu!")
if pc == "papel" and jogador == "pedra":
    print("Haha Você perdeu!")

# o jogador ganha

if pc == "tesoura" and jogador == "pedra":
    print("Você ganhou. Parabéns!")
if pc == "papel" and jogador == "tesoura":
    print("Você ganhou. Parabéns!")
if pc == "pedra" and jogador == "papel":
    print("Você ganhou. Parabéns!")

# empate

if pc == jogador:
    print("Copião. Empatamos")
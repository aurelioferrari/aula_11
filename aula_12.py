nome = str(input("Qual é o seu nome? "))

if nome == "chico":
    print("que nome bonito!")
elif nome == "Pedro" or nome == "Maria":
    print("Seu nome é popular!")
elif nome in "Ana Jessica Daphne":
    print("Baita nome")
else:
    print("seu nome é normal")

print("tenha um bom dia, {}".format(nome))
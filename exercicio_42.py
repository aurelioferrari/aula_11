r1 = int(input("Reta 1: "))
r2 = int(input("Reta 2: "))
r3 = int(input("Reta 3: "))

modulo = abs(r2 - r3)
soma = r2 + r3

if r1 > modulo and r1 < soma:
	print("Formam um triângulo.")
if r1 == r2 and r1 == r3 and r2 == r3:
    print("O triângulo é equilátero.")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("O triângulo é isósceles.")
elif r1 != r2 and r1 != r3 and r2 != r3:
    print("O triângulo é escaleno.")
else:
	print("Não formam um triângulo.")
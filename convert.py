numero = int(input())

rest = []
while numero>=1:
	resto = numero%2
	numero = int(numero/2)
	rest.append(resto)

rest.reverse()
x = len(rest)

for i in range(x):
	print(rest[i], end='')


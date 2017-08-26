soma = 0

for i in range(3):
	nome = input()
	distancia = int(input())
	soma = soma + distancia
media = float(soma/3)
print("%.1f" % media)		
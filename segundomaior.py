#imprimir o segundo maior elemento da lista
numero = int(input("entre com quantos numero voce deseja: "))

vet = []
for i in range(1,numero+1):
	x = int(input("Entre com um numero para por no vetor: "))
	vet.append(x)
vet.sort(reverse=True)
i=0
while i<numero:
	if vet[i]!=vet[i+1]:
		print(vet[i+1])
		break
	elif vet[i]==vet[i+1]:
		i+=1

print("\n", vet)










t = int(input("entre com o numero de testes: "))

for i in range(1, t+1):
	v = int(input("entre com o numero de candidatos e numero de zoanas eleitorais: "))
	n,m = split(v)
	n = int(n)
	m = int(m)
	total = [0]*n
	for j in range(1,m):
		s = int(input("entre com os votos aqui: "))
		votos = map(int, split())
		k=0
		while k < n:
			total[k] += votos[k]
			k += 1

		print(total.index(max(total))+1)	

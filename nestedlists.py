n = int(input("entre com o numero de alunos: "))

d = []
for i in range(1, n+1):
	nome = input("entre com o nome do aluno: ")
	nota = int(input("entre com a nota do aluno: "))

	d.append(nome)
	d.append(nota)
	
	print (d[i])




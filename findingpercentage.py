n = int(input())
materias = 3
notas_alunos = {}
for i in range(n):
	nome, *lista = input().split()
	notas = list(map(float, lista))
	notas_alunos[nome] = notas
escolha_aluno = input()
nota_escolhida = sum(notas_alunos[escolha_aluno])
media = float(nota_escolhida/3)
print("%.2f"% media)
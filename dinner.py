s = input()
n,d = map(int, s.split())
n = int(n)
d = int(d)
soma = 0

for i in range(d):
	x = input()
	x = list(map(int,x.split()))

for j in range(d):
	soma = soma + x[j]
	if soma == n:
		print("yes")
		break
		

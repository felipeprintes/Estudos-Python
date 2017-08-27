s = input()
n,d = map(int, s.split())
n = int(n)
d = int(d)
soma = 0
aux = 0
for i in range(d):
	x = input()
	x = list(map(int,x.split()))
	soma = sum(x)
	if soma == n:
		aux = soma
if soma == aux:
	print("Yes")
else:
	print("no")			

haha	

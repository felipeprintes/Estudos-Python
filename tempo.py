h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

hora1 = h1*60 + m1
hora2 = h2*60 + m2

if hora2 < hora1:
	hora2 = (h2+24)*60 + m2

tempo = hora2 - hora1

print(tempo)
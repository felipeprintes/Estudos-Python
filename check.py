nome = input("Entre com seu nome: ")

def entradaEmail():
	email = input("Entre com seu email: ")

entradaEmail()				
		
senha = input("Entre com sua senha: ")
conf_senha = input("Confirme sua senha: ")

while senha != conf_senha:
	print("Senha inválida, tente de novo")
	conf_senha = input("Confirme sua senha: ")	

if senha == conf_senha:
	print("Seja bem vindo!")
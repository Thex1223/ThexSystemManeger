from app import *
from venda import *

comandos = """
================ Comandos ================

exit		: Sair
login		: Login do sistema
creditos 	: Acessa tela creditos
estoque 	: acessa estoque
config 		: Acessar configurações
app 		: Acessa App

================ -------- ================
"""
tentativa = 0
while True:

	print(comandos)

	ent = "estoque"

	if ent == None:
		ent = input("Digite o módulo a EXECUTAR ==> ")

	else:
		if tentativa > 0:
			break
		tentativa+=1

	if ent == "exit":
		break

	elif ent == "login":
		Login().execute()

	elif ent == "creditos":
		Tela_Creditos().execute()

	elif ent == "estoque":
		Cadastro_Produtos().execute()

	elif ent == "config":
		from config import *
		App_Config().execute()

	elif ent == "app":
		App().execute()

	else:
		print("Comando não reconhecido!")
		continue

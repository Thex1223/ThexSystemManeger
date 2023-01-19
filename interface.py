import tkinter as tk
from functions import *

def login_mal_sucedido():
	janela_mal_sucedido = tk.Tk()
	janela_mal_sucedido.title("Login :(")
	janela_mal_sucedido.geometry("200x30")
	janela_mal_sucedido.resizable(0,0)

	txt_mal_sucedido = tk.Label(janela_mal_sucedido, text="Login não realizado! \n:(")
	txt_mal_sucedido.pack()

def executa_login(user_get, chave_get, db_funcionarios, janela, txt_info):
	if acessa_sistema(user_get, chave_get, db_funcionarios):
		janela.destroy()
	else:
		txt_info["text"] = "Login não realizado!"
		txt_info['fg'] = "red"
		log('==== ATENÇÃO | LOGIN NÃO REALIZADO! ====')

# ==============================================
#
# INTERFACE GRAFICA DA TELA DE LOGIN
#
# ==============================================

class App_Login():
	def __init__(self, db_app, db_func):
		self.app_db = db_app
		self.funcionarios_db = db_func
		self.janela = None
		self.txt_info = None

	def execute(self):
		self.janela = tk.Tk()
		self.janela.title(f'Login | {self.app_db["app_name"]}')
		self.janela.geometry("235x180")
		self.janela.resizable(0, 0)

		frm_login = tk.LabelFrame(text=f'{self.app_db["nome_da_empresa"]}')
		frm_login.grid(column=0, row=0,padx=10, pady=10)
		# --------------------------------------------
		txt_user = tk.Label(frm_login, text="User:")
		txt_user.grid(column=0, row=0, padx=10, pady=10)

		inp_user = tk.Entry(frm_login)
		inp_user.grid(column=1, row=0, padx=10, pady=10)

		# ---------------------------------------------
		txt_chave = tk.Label(frm_login, text="Chave:")
		txt_chave.grid(column=0, row=1, padx=10, pady=10)

		inp_chave = tk.Entry(frm_login)
		inp_chave.grid(column=1, row=1, padx=10, pady=10)
		# ------------------------------------
		btn_login = tk.Button(frm_login, text="Login", command=lambda: executa_login(inp_user.get(), inp_chave.get(), self.funcionarios_db, self.janela, self.txt_info))
		btn_login.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)
		# ---------------------------------------------
		self.txt_info = tk.Label(text=self.app_db["txt_credit"])
		self.txt_info.grid(column=0, row=1)
		# ______________________________________
		self.janela.mainloop()

class App():
	def __init__(self, db_app, db_func):
		self.app_db = db_app
		self.funcionarios_db = db_func

	def execute(self):
		self.janela = tk.Tk()
		self.janela.title(f'{self.app_db["app_name_system"]} | {self.app_db["app_name"]}')
		self.janela.geometry("1440x1024")
		self.janela.resizable(0, 0)

		print("Entrado no sistema")

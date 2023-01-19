import json
import tkinter as tk
import datetime as dt

def data_hora(mode="all"):
    data = dt.datetime.now()
    if mode == "all":
        formato_de_data = data.strftime("%d/%m/%Y | %H:%M:%S")
        return f'[{formato_de_data}]'

    elif mode == "data-log":
        formato_de_data = data.strftime("%d_%m_%Y")
        return formato_de_data

def log(msg):
    file_log = open(f'logs/{data_hora("data-log")}.txt', "a", encoding='utf8')
    file_log.write(f'{data_hora()} {msg}\n')
    file_log.close()

def acessa_arquivo_json(arquivo, modo='r'):
    with open(arquivo, modo, encoding='utf8') as file:
        data = json.load(file)
        return data

def login_bem_sucedido():
    janela_bem_sucedido = tk.Tk()
    janela_bem_sucedido.title("Login :)")
    janela_bem_sucedido.geometry("200x30")
    janela_bem_sucedido.resizable(0,0)

    txt_bem_sucedido = tk.Label(janela_bem_sucedido, text="Login realizado com sucesso! \n:)")
    txt_bem_sucedido.pack()

def acessa_sistema(nomeDoFuncionario, identificador, db_funcionarios):
    cont = 0
    while cont < len(db_funcionarios):
        if nomeDoFuncionario == db_funcionarios[cont]["nome_do_funcionario"]:

            if identificador == db_funcionarios[cont]["identificador"]:
                log('==== Logado no sistema! ====')
                log(f'User: {nomeDoFuncionario}')
                log(f'Chave: {identificador}')
                return True

        cont = cont+1

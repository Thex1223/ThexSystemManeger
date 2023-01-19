from functions import *
from interface import App_Login
data_software = acessa_arquivo_json("dados/data.json")

data_funcionarios = acessa_arquivo_json("dados/funcionarios.json")

app_login_janela = App_Login(data_software, data_funcionarios).execute()





# acessa_sistema("Kainan Henrique", "10002", data_funcionarios)

# -----------------------------------------------------------------------------
#     $$$$$$\                                              $$\
#     \_$$  _|                                             $$ |
#       $$ |  $$$$$$\$$$$\   $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\
#       $$ |  $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\\_$$  _|
#       $$ |  $$ / $$ / $$ |$$ /  $$ |$$ /  $$ |$$ |  \__| $$ |
#       $$ |  $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |       $$ |$$\
#     $$$$$$\ $$ | $$ | $$ |$$$$$$$  |\$$$$$$  |$$ |       \$$$$  |
#     \______|\__| \__| \__|$$  ____/  \______/ \__|        \____/
#                           $$ |
#                           $$ |
#                           \__|
# -----------------------------------------------------------------------------

import json
import tkinter as tk
import datetime as dt
import PySimpleGUI as psg
import os


def acessa_arquivo_json(arquivo, modo='r'):
    if os.path.getsize(arquivo) == 0:
        arquivo_dado = open(arquivo, "w")
        arquivo_dado.write("[]")
        arquivo_dado.close()

    with open(arquivo, modo, encoding='utf8') as file:
        data = json.load(file)
        return data


db_software = acessa_arquivo_json("dados/data.json")


def acessa_estoque():
    if os.path.getsize(db_software["db_estoque"]) == 0:
        arquivo_dado = open(db_software["db_estoque"], "w")
        arquivo_dado.write("[]")
        arquivo_dado.close()

    return acessa_arquivo_json(db_software["db_estoque"])


# -----------------------------------------------------------------------------
#      $$$$$$\
#     $$  __$$\
#     $$ /  \__| $$$$$$\ $$\    $$\  $$$$$$\
#     \$$$$$$\   \____$$\\$$\  $$  |$$  __$$\
#      \____$$\  $$$$$$$ |\$$\$$  / $$$$$$$$ |
#     $$\   $$ |$$  __$$ | \$$$  /  $$   ____|
#     \$$$$$$  |\$$$$$$$ |  \$  /   \$$$$$$$\
#      \______/  \_______|   \_/     \_______|
# -----------------------------------------------------------------------------

# _nome_funcionarios = None
# _identificador_funcionarios = None
# _login_realizado = None
#
#
# def credenciais(tipo):
#     if tipo == "nome":
#         return _nome_funcionarios
#
#     elif tipo == "identificador":
#         return _identificador_funcionarios
#
#     elif tipo == "login":
#         return _login_realizado


# -----------------------------------------------------------------------------
#     $$$$$$$$\                              $$\     $$\
#     $$  _____|                             $$ |    \__|
#     $$ |   $$\   $$\ $$$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$$\
#     $$$$$\ $$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|
#     $$  __|$$ |  $$ |$$ |  $$ |$$ /        $$ |    $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\
#     $$ |   $$ |  $$ |$$ |  $$ |$$ |        $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\
#     $$ |   \$$$$$$  |$$ |  $$ |\$$$$$$$\   \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
#     \__|    \______/ \__|  \__| \_______|   \____/ \__| \______/ \__|  \__|\_______/
#
#      $$$$$$\                        $$\
#     $$  __$$\                       $$ |
#     $$ /  \__|$$\   $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\$$$$\
#     \$$$$$$\  $$ |  $$ |$$  _____|\_$$  _|  $$  __$$\ $$  _$$  _$$\
#      \____$$\ $$ |  $$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ / $$ / $$ |
#     $$\   $$ |$$ |  $$ | \____$$\   $$ |$$\ $$   ____|$$ | $$ | $$ |
#     \$$$$$$  |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ | $$ | $$ |
#      \______/  \____$$ |\_______/    \____/  \_______|\__| \__| \__|
#               $$\   $$ |
#               \$$$$$$  |
#                \______/
# -----------------------------------------------------------------------------

def data_hora(mode="all"):
    """
    all = [D/M/A | H:M:S]
    data = D/M/A
    data-log = D_M_A
    """
    data = dt.datetime.now()
    if mode == "all":
        formato_de_data = data.strftime("%d/%m/%Y | %H:%M:%S")
        return f'[{formato_de_data}]'

    if mode == "data":
        formato_de_data = data.strftime("%d/%m/%Y")
        return f'{formato_de_data}'

    elif mode == "data-log":
        formato_de_data = data.strftime("%d_%m_%Y")
        return formato_de_data

def log(msg):

    if db_software["system_options"]["log"] == True:

        file_log = open(f'logs/{data_hora("data-log")}.txt', "a", encoding='utf8')
        file_log.write(f'{data_hora()} {msg}\n')
        file_log.close()

def acessa_arquivo_json(arquivo, modo='r'):
    with open(arquivo, modo, encoding='utf8') as file:
        data = json.load(file)
        return data

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def tema():
    return psg.theme(
        db_software["system_options"]["theme"][db_software["system_options"]["theme_select"]]), psg.set_options(
        font=db_software["system_options"]["font"])

def janela(title, layout, resizable=False, use_custom_titlebar=False,no_titlebar=False, force_toplevel=False, keep_on_top=True, modo=""):
    janela = psg.Window(
        title="{} | {}".format(title, db_software["nome_da_empresa"]),
        layout=layout,
        use_custom_titlebar=use_custom_titlebar,
        icon=db_software["system_options"]["icon"],
        font=db_software["system_options"]["font"],
        resizable=resizable,
        finalize=True,
        return_keyboard_events=True,
        force_toplevel=force_toplevel,
        keep_on_top=keep_on_top,
        no_titlebar=False
    )
    return janela

def janela_cadastro_produto(title="Produto", mode="criar", nome="", codigo=100000000, quantidade=0, valor_custo=0.0, perc_margem=0.0, valor_venda=0.0, descricao="", peso=0.1, marca=""):
    size_text = [15, 1]
    layout_tela = [
        [
            psg.Text(text="Nome do Produto", size=size_text),
            psg.Input(key="-input_nome_do_produto-", border_width=0, default_text=nome)
        ],
        [
            psg.Text(text="Código", size=size_text),
            psg.Input(key="-input_codigo_do_produto-", border_width=0, default_text=codigo)
        ],
        [
            psg.Text(text="Quantidade", size=size_text),
            psg.Input(key="-input_quantidade_do_produto-", border_width=0, default_text=quantidade)
        ],
        [
            psg.Text(text="Valor Custo R$", size=size_text),
            psg.Input(key="-input_valor_do_produto_custo-", border_width=0, default_text=valor_custo)
        ],
        [
            psg.Text(text="% (0-*)", size=size_text),
            psg.Input(key="-input_percentual_margem_do_produto-", border_width=0, default_text=perc_margem)
        ],
        [
            psg.Text(text="Valor Venda R$", size=size_text),
            psg.Input(
                key="-input_valor_do_produto_venda-",
                border_width=0,
                default_text=valor_venda,
                disabled=db_software["system_options"]["auto_calcule_venda"],
                font=(db_software["system_options"]["font"], 12, "bold")
            )
        ],
        [
            psg.Text(text="Descrição", size=size_text),
            psg.Multiline(key="-input_descricao_do_produto-", size=(43, 5), border_width=0, default_text=descricao)
        ],
        [
            psg.Text(text="Peso", size=size_text),
            psg.Input(key="-input_peso_do_produto-", border_width=0, default_text=peso)
        ],
        [
            psg.Text(text="Marca", size=size_text),
            psg.Input(key="-input_marca_do_produto-", border_width=0, default_text=marca)
        ],
        [
            psg.Button(button_text="Cancelar", key="-cancel-", size=size_text, border_width=0),
            psg.Button(button_text=mode, key=f"-{mode}-", size=size_text, border_width=0)
        ]
    ]
    if mode  == "Salvar" or mode == "save":
        layout_tela[9].append(psg.Button(button_text="Excluir", key=f"-excluir-", size=size_text, border_width=0))

    tela_cadastro = [
        [
            psg.Frame(title=title.upper(), pad=[10, 10], layout=layout_tela)
        ]
    ]
    return tela_cadastro


def popup_atencao(msg):
    psg.Popup(
        msg,
        title="Atenção!",
        keep_on_top=True,
        font=db_software["system_options"]["font"],
        icon=db_software["system_options"]["icon"]
    )


def popup_msg(msg, title=""):
    psg.Popup(
        msg,
        title=title,
        keep_on_top=True,
        font=db_software["system_options"]["font"],
        icon=db_software["system_options"]["icon"]
    )


def tabela_produtos():
    db_estoque = acessa_estoque()
    produtos = []
    cont = 0
    while cont < len(db_estoque):
        produtos.append(
            [
                db_estoque[cont]["nome_do_produto"].upper(),
                db_estoque[cont]["codigo"],
                db_estoque[cont]["quantidade"],
                db_estoque[cont]["valor_custo"],
                db_estoque[cont]["perc_margem"],
                db_estoque[cont]["valor_venda"],
                db_estoque[cont]["peso"],
                db_estoque[cont]["marca"],
                int(db_estoque[cont]["quantidade"]) * float(db_estoque[cont]["valor_custo"]),
                int(db_estoque[cont]["quantidade"]) * float(db_estoque[cont]["valor_venda"]),
                float(db_estoque[cont]["valor_venda"]) - float(db_estoque[cont]["valor_custo"])
            ]
        )
        cont += 1
    return produtos

def calculo_criar_margem(custo, margem, saida_normal):
    if saida_normal == 0.0:
        porcentagem = custo * margem / 100
        resultado = custo + porcentagem
        return resultado
    else:
        return saida_normal



def edita_produto(value, data, index):
    if value["-input_quantidade_do_produto-"] != "" and value["-input_valor_do_produto_custo-"] != '' and value["-input_nome_do_produto-"] != '':
        if value["-input_quantidade_do_produto-"].isnumeric() or isfloat(value["-input_quantidade_do_produto-"].replace(",", ".")):
            if value["-input_valor_do_produto_custo-"].isnumeric() or isfloat(value["-input_valor_do_produto_custo-"].replace(",", ".")):
                if value["-input_valor_do_produto_venda-"].isnumeric() or isfloat(value["-input_valor_do_produto_venda-"].replace(",", ".")):
                    if value["-input_percentual_margem_do_produto-"].isnumeric() or isfloat(value["-input_percentual_margem_do_produto-"].replace(",", ".")):
                        if value["-input_peso_do_produto-"].isnumeric() or isfloat(value["-input_peso_do_produto-"].replace(",", ".")) or value["-input_peso_do_produto-"] == "":

                            data[index]["nome_do_produto"] = value["-input_nome_do_produto-"].upper()
                            data[index]["codigo"] = value["-input_codigo_do_produto-"]
                            data[index]["quantidade"] = float(value["-input_quantidade_do_produto-"].replace(",", "."))
                            data[index]["valor_custo"] = float(value["-input_valor_do_produto_custo-"].replace(",", "."))
                            data[index]["perc_margem"] = float(value["-input_percentual_margem_do_produto-"].replace(",", "."))


                            data[index]["valor_venda"] = (
                                float(value["-input_valor_do_produto_custo-"].replace(",", ".")),
                                float(value["-input_percentual_margem_do_produto-"].replace(",", ".")),
                                float(value["-input_valor_do_produto_venda-"])
                            )

                            data[index]["valor_venda"] = float(value["-input_valor_do_produto_venda-"].replace(",", "."))
                            data[index]["descricao"] = value["-input_descricao_do_produto-"]
                            data[index]["peso"] = transform_float(value["-input_peso_do_produto-"])
                            data[index]["marca"] = value["-input_marca_do_produto-"]

                            popup_msg("Podruto EDITADO com sucesso!")
                            return True

                        else:
                            popup_atencao("O valor do PESO do produto, precisa ser um NÚMERO!")
                    else:
                        popup_atencao("A entrada do PERCENTUAL DE MARGEM do produto, precisa ser um NÚMERO!")
                else:
                    popup_atencao("O valor do CUSTO do produto, precisa ser um NÚMERO!")
            else:
                popup_atencao("O valor de VENDA do produto, precisa ser um NÚMERO!")
        else:
            popup_atencao("O valor do QUANTIDADE do produto, precisa ser um NÚMERO INTEIRO!")
    else:
        popup_atencao("Preencha os campos OBRIGATÓRIOS! \nNome, Valor, Quantidade...")


def get_quantidade(data, index):
    return data[index]["quantidade"]

def edita_quantidade(value, data, index):
    data[index]["quantidade"] = value


def transform_float(arg):
    if arg == None or arg == "":
        return 0
    else:
        return float(arg.replace(",", "."))

def acessa_nome_do_produto():
    dados = acessa_arquivo_json(db_software["db_estoque"])

    nomes = []
    cont =0
    while cont < len(dados):
        nomes.append(f'{(dados[cont]["nome_do_produto"]+(" "*50))[:50]} {(dados[cont]["codigo"]+(" "*20))[:20]} {(str(dados[cont]["peso"])+" Kg "+" "*18)[:18]} {("R$ "+str(dados[cont]["valor_venda"])+" "*18)[:18]} {dados[cont]["marca"]}')
        cont+=1
    return nomes

def mostra_clientes(mode="all"):
    dados = acessa_arquivo_json(db_software["db_clientes"])

    clientes = []
    cont = 0
    while cont < len(dados):

        if mode == "all":
            clientes.append(dados[cont])
        elif mode == "nome":
            clientes.append(dados[cont]["nome"].upper())
        elif mode == "cpf":
            clientes.append(dados[cont]["cpf"])
        elif mode == "telefone":
            clientes.append(dados[cont]["telefone"])

        cont+=1
    return clientes


def mostra_atalhos(mode="atalhos_pdv"):
    if db_software["info_atalhos"] == True:

        atalhos = db_software["mensagens"][mode]
        atalhos_saida = []

        cont = 0
        while cont < len(atalhos):
            atalhos_saida.append([psg.Text(text=atalhos[cont], pad=[10,10])])
            cont+=1
        return atalhos_saida

    else:
        return []

def popup_valor():
    layout = [
        [
            psg.Text(text="Insira o valor:")
        ],
        [
            psg.Input(key="-input_valor-", font=(db_software["system_options"]["font"], 20, "bold"), enable_events=True)
        ]
    ]
    popup_valor_janela = psg.Window(
        title="",
        layout=layout,
        return_keyboard_events=True,
        finalize=True,
        keep_on_top=True
    )
    popup_valor_janela["-input_valor-"].bind("<Return>", "_Enter")
    popup_valor_janela.bind("<Escape>", "_Esc")

    valor_saida = 0

    while True:
        event, value = popup_valor_janela.read()

        if event == psg.WIN_CLOSED or event == "_Esc":
            break
        if value["-input_valor-"] != "":
            if event == "-input_valor-" + "_Enter":

                try:
                    valor_saida = float(value["-input_valor-"].replace(",", "."))
                    popup_valor_janela.close()
                    return valor_saida

                except ValueError:
                    continue
# -----------------------------------------------------------------------------
#     $$$$$$\            $$\                          $$$$$$\
#     \_$$  _|           $$ |                        $$  __$$\
#       $$ |  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ /  \__|$$$$$$\   $$$$$$$\  $$$$$$\
#       $$ |  $$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ $$$$\     \____$$\ $$  _____|$$  __$$\
#       $$ |  $$ |  $$ | $$ |    $$$$$$$$ |$$ |  \__|$$  _|    $$$$$$$ |$$ /      $$$$$$$$ |
#       $$ |  $$ |  $$ | $$ |$$\ $$   ____|$$ |      $$ |     $$  __$$ |$$ |      $$   ____|
#     $$$$$$\ $$ |  $$ | \$$$$  |\$$$$$$$\ $$ |      $$ |     \$$$$$$$ |\$$$$$$$\ \$$$$$$$\
#     \______|\__|  \__|  \____/  \_______|\__|      \__|      \_______| \_______| \_______|
# -----------------------------------------------------------------------------
def acessa_sistema(nomeDoFuncionario, identificador, db_funcionarios):
    cont = 0
    while cont < len(db_funcionarios):

        if nomeDoFuncionario == db_funcionarios[cont]["nome_do_funcionario"]:

            if identificador == db_funcionarios[cont]["identificador"]:
                log('==== Logado no sistema! ====')
                log(f'User: {nomeDoFuncionario}')
                log(f'Chave: {identificador}')
                _nome_funcionarios = nomeDoFuncionario
                _identificador_funcionarios = identificador
                _login_realizado = True
                return True

        cont = cont + 1


class Tela_Creditos:
    def __init__(self):
        self.db_app = acessa_arquivo_json("dados/data.json")
        self.tela_creditos = None

    def execute(self):
        text_creditos = f"""
    		Thex System Maneger

    		Versão: {self.db_app["version"]}
    		Última Atualização: {self.db_app["data_ultima_version"]}

    		Todos os direitos reservados. Copyrigth Kainan H. & Thex 1223 [Brazil]

    		==== Equipe Responsável ====

    		- Kainan H. [GitHub: Na18k]	

    	"""
        layout_creditos = [
            [
                psg.Multiline(default_text=text_creditos, disabled=True, size=(80, 20), justification="center")
            ]
        ]
        self.tela_creditos = psg.Window(title="Creditos", layout=layout_creditos, keep_on_top=True)

        while True:
            event, value = self.tela_creditos.read()
            if event == psg.WIN_CLOSED:
                break

    def close(self):
        self.tela_creditos.close()

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def inicio(acao0, acao1, acao2):
    layout = [
        [
            psg.Text("Sistemas:")
        ],
        [
            psg.Button("PDV", key="-pdv-"),
            psg.Button("Estoque", key="-estoque-"),
            psg.Button("Vendas", key="-registro_vendas-")
        ]
    ]
    janela_inicio = janela("Inicio", layout=layout)
    while True:
        event, value = janela_inicio.read()
        if event == psg.WIN_CLOSED:
            break

        elif event == "-pdv-":
            acao0.execute()

        elif event == "-estoque-":
            acao1.execute()

        elif event == "-registro_vendas-":
            acao2.execute()



# -----------------------------------------------------------------------------
#      $$$$$$\                  $$\                       $$\
#     $$  __$$\                 $$ |                      $$ |
#     $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\
#     $$ |       \____$$\ $$  __$$ | \____$$\ $$  _____|\_$$  _|  $$  __$$\ $$  __$$\
#     $$ |       $$$$$$$ |$$ /  $$ | $$$$$$$ |\$$$$$$\    $$ |    $$ |  \__|$$ /  $$ |
#     $$ |  $$\ $$  __$$ |$$ |  $$ |$$  __$$ | \____$$\   $$ |$$\ $$ |      $$ |  $$ |
#     \$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |$$$$$$$  |  \$$$$  |$$ |      \$$$$$$  |
#      \______/  \_______| \_______| \_______|\_______/    \____/ \__|       \______/
# -----------------------------------------------------------------------------

class Cliente:
    def __init__(self, clientes_db):
        self.db_clientes = clientes_db

    @property
    def carrega_clientes(self):
        return self.db_clientes

    def criar_cliente(self, nome, telefone, cpf, rua, numero, complemento, bairro, cidade):
        data_saida = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "endereco": {
                "rua": rua,
                "numero": numero,
                "complemento": complemento,
                "bairro": bairro,
                "cidade": cidade
            }
        }

# -----------------------------------------------------------------------------
#     $$$$$$$$\ $$\
#     \__$$  __|$$ |
#        $$ |   $$$$$$$\   $$$$$$\  $$\   $$\
#        $$ |   $$  __$$\ $$  __$$\ \$$\ $$  |
#        $$ |   $$ |  $$ |$$$$$$$$ | \$$$$  /
#        $$ |   $$ |  $$ |$$   ____| $$  $$<
#        $$ |   $$ |  $$ |\$$$$$$$\ $$  /\$$\
#        \__|   \__|  \__| \_______|\__/  \__|
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
#     $$\      $$\
#     $$$\    $$$ |
#     $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\
#     $$\$$\$$ $$ | \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\
#     $$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
#     $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |
#     $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$\ $$ |
#     \__|     \__| \_______|\__|  \__| \_______| \____$$ | \_______|\__|
#                                                $$\   $$ |
#                                                \$$$$$$  |
#                                                 \______/
# -----------------------------------------------------------------------------
#   Creator By: Thex 1223
#   Equip: Kainan H. (na18k)
#
#   Created in: 2023    //      Lasted Update:  25/01/2023
#
#   Version: v0.0.1-alpha
# -----------------------------------------------------------------------------

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
from functions import *
import json
import PySimpleGUI as psg
import os
from PIL import Image
from test import *

# -----------------------------------------------------------------------------
#     $$\                          $$\
#     $$ |                         \__|
#     $$ |      $$$$$$\   $$$$$$\  $$\ $$$$$$$\
#     $$ |     $$  __$$\ $$  __$$\ $$ |$$  __$$\
#     $$ |     $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |
#     $$ |     $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |
#     $$$$$$$$\\$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |
#     \________|\______/  \____$$ |\__|\__|  \__|
#                        $$\   $$ |
#                        \$$$$$$  |
#                         \______/
# -----------------------------------------------------------------------------

class Login:
    def __init__(self, db_app="dados/data.json"):
        self.db_app = acessa_arquivo_json(db_app)

        tema()

        layout_manin = [
            [
                psg.Text(text="User:", size=(15, 1), pad=(20, 10)),
                psg.Input(key="-user-", size=(45, 2), pad=(20, 10), border_width=0)
            ],
            [
                psg.Text(text="Identificador:", size=(15, 1), pad=(20, 10)),
                psg.Input(password_char="X", key="-identificador-", size=(45, 1), pad=(20, 10), border_width=0)
            ],
            [
                psg.Button(button_text="Creditos", key="-creditos-", size=(15, 1), pad=(20, 20), border_width=0),
                psg.Button(button_text="Login", key="-login-", size=(44, 1), pad=(20, 20), border_width=0)
            ]
        ]
        layout_image_main = [
            [
                psg.Image("assets/icon.png")
            ],
        ]
        layout_frame = [
            [
                psg.Frame(title="", border_width=0, layout=layout_image_main),
                psg.Frame(title="Login", layout=layout_manin, pad=(20, 20))
            ]
        ]
        self.tela_login = janela("Login", layout_frame)

    def execute(self):
        log("Login iniciado...")
        while True:

            events, value = self.tela_login.read()

            if events == psg.WIN_CLOSED:
                log("Login encerrado...")
                break

            elif events == "-login-":
                if acessa_sistema(value["-user-"], value['-identificador-'], acessa_arquivo_json(self.db_app["db_funcionarios"])):
                    self.tela_login.close()

                # ====================================
                # LOGIN
                # ====================================
                App(user=value["-user-"],identificador=value['-identificador-'])

            elif events == "-creditos-":
                Tela_Creditos().execute()

# -----------------------------------------------------------------------------
# 	$$$$$$$$\             $$\
# 	$$  _____|            $$ |
# 	$$ |       $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\
# 	$$$$$\    $$  _____|\_$$  _|  $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\
# 	$$  __|   \$$$$$$\    $$ |    $$ /  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |
# 	$$ |       \____$$\   $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|
# 	$$$$$$$$\ $$$$$$$  |  \$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$  |\$$$$$$$\
# 	\________|\_______/    \____/  \______/  \____$$ | \______/  \_______|
# 												  $$ |
# 												  $$ |
# 												  \__|
# -----------------------------------------------------------------------------
class Cadastro_Produtos:
    def __init__(self, db_app="dados/data.json"):
        self.db_app = acessa_arquivo_json(db_app)
        self.events = None
        self.value = None

        # Info
        self.valor_total = 0
        self.quantidade_total = 0

        tema()

        menu = [["Produto", ["Criar"]], ["Atualizar"]]

        layout = [
            [
                psg.Button(button_text="Novo", key="-novo-", border_width=0, focus=False),
                psg.Button(button_text="Atualizar", key="-atualizar-", border_width=0)
            ]
        ]
        valores_tabela = ["Nome do Produto", "Código", "Quantidade", "Valor", "Peso", "Marca", "Valor Total" ]
        layout_main = [
            [
                psg.Table(
                    values="",
                    headings=valores_tabela,
                    key="tabela_saida_produtos",
                    auto_size_columns=False,
                    num_rows=28,
                    max_col_width=95,
                    row_height=20,
                    font=f"{self.db_app['system_options']['font']} 12",
                    col_widths=[40, 25, 12, 8, 8, 20, 20],
                    header_border_width=1,
                    enable_click_events=True,
                    enable_events=True,
                    selected_row_colors="white on black"
                )
            ]
        ]
        layout_footer = [
            [
                psg.Text(text="Valor Total:"),
                psg.Text(text=f'', key="-valor_total_produtos-")
            ],
            [
                psg.Text(text="Quantidade Total:"),
                psg.Text(text=f'', key="-quantidade_total_produtos-")
            ]
        ]
        layout_frame = [
            [psg.Frame(title="", layout=layout, border_width=0)],
            [psg.Frame(title="", layout=layout_main, border_width=0)],
            [psg.Frame(title="Info:", layout=layout_footer)]
        ]

        self.janelas_cadastro_produtos = janela("Estoque", layout_frame)

    def execute(self):
        log("Estoque aberto...")
        while True:
            self.janelas_cadastro_produtos["tabela_saida_produtos"].update(values=tabela_produtos())
            self.atualiza_info()
            self.events, self.value = self.janelas_cadastro_produtos.read()

            if self.events == psg.WIN_CLOSED:
                log("Painel do estoque fechado...")
                break

            elif self.events == "-novo-" or self.events == "Criar":
                self.tela_cadastro()

            elif self.events == "-atualizar-" or self.events == "Atualizar":
                self.janelas_cadastro_produtos["tabela_saida_produtos"].update(values=tabela_produtos())

            elif self.events == "tabela_saida_produtos":
                location_table = self.janelas_cadastro_produtos["tabela_saida_produtos"].get_last_clicked_position()
                location_row_select = location_table[0]

                self.editar_produto(location_row_select)

    def tela_cadastro(self):
        janela_cadastro_novo_produto = janela("Novo", janela_cadastro_produto(title="Cadastrar Novo Produto"))

        while True:
            events, value = janela_cadastro_novo_produto.read()

            if events == psg.WIN_CLOSED or events == "-cancel-":
                janela_cadastro_novo_produto.close()
                break
            elif events == "-criar-":

                if value["-input_quantidade_do_produto-"] != "" and value["-input_valor_do_produto-"] != '' and value["-input_nome_do_produto-"] != '':

                    if value["-input_quantidade_do_produto-"].isnumeric() or isfloat(value["-input_quantidade_do_produto-"].replace(",", ".")):
                        if value["-input_valor_do_produto-"].isnumeric() or isfloat(value["-input_valor_do_produto-"].replace(",", ".")):
                            if value["-input_peso_do_produto-"].isnumeric() or isfloat(value["-input_peso_do_produto-"].replace(",", ".")) or value["-input_peso_do_produto-"] == "":
                                self.cadastrar(
                                    value["-input_nome_do_produto-"].upper(),
                                    value["-input_codigo_do_produto-"],
                                    float(value["-input_quantidade_do_produto-"].replace(",", ".")),
                                    float(value["-input_valor_do_produto-"].replace(",", ".")),
                                    value["-input_descricao_do_produto-"].upper(),
                                    transform_float(value["-input_peso_do_produto-"]),
                                    value["-input_marca_do_produto-"]
                                )
                                popup_msg("Podruto cadastrado com sucesso!")
                                janela_cadastro_novo_produto.close()

                            else:
                                popup_atencao("O valor do PESO do produto, precisa ser um NÚMERO!")
                        else:
                            popup_atencao("O valor do VALOR do produto, precisa ser um NÚMERO!")
                    else:
                        popup_atencao("O valor do QUANTIDADE do produto, precisa ser um NÚMERO INTEIRO!")
                else:
                    popup_atencao("Preencha os campos OBRIGATÓRIOS! \nNome, Valor, Quantidade...")

    def cadastrar(self, nome_do_produto, codigo_do_produto, quantidade, valor, descricao, peso, marca):
        dados_preset = {
            "nome_do_produto": nome_do_produto,
            "codigo": codigo_do_produto,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao,
            "peso": peso,
            "marca": marca
        }
        if os.path.getsize(self.db_app["db_estoque"]) == 0:
            arquivo = open(self.db_app["db_estoque"], "w")
            arquivo.write("[]")
            arquivo.close()

        with open(f'{self.db_app["db_estoque"]}', "r", encoding='utf8') as file:
            dados = json.load(file)

        dados.append(dados_preset)

        with open(f'{self.db_app["db_estoque"]}', "w", encoding='utf8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        log(" ")
        log("---------------- Novo Produto Cadastrado no Estoque ----------------")
        log(f"Local: {self.db_app['db_estoque']}")
        log(f"==> Nome do Produto: {nome_do_produto}")
        log(f"==> Código do Produto: {codigo_do_produto}")
        log(f"==> Quantidade do Produto: {quantidade}")
        log(f"==> Valor do Produto: {valor}")
        log(f"==> Descrição do Produto: {descricao}")
        log(f"==> Peso do Produto: {peso}")
        log(f"==> Marca do Produto: {marca}")
        log(" ")

    def editar_produto(self, index):
        dados = acessa_arquivo_json(self.db_app["db_estoque"])

        if os.path.getsize(self.db_app["db_estoque"]) < 160:
            psg.Popup(
                "Não existe nenhum produto no estoque atual! \nPor favor, crie um produto para poder edita-lo.",
                title="Atenção!",
                keep_on_top=True
            )
        else:
            layout = janela_cadastro_produto(
                title="Editar Produto",
                mode="Salvar",
                nome=dados[index]["nome_do_produto"],
                codigo=dados[index]["codigo"],
                quantidade=dados[index]["quantidade"],
                valor=dados[index]["valor"],
                descricao=dados[index]["descricao"],
                peso=dados[index]["peso"],
                marca=dados[index]["marca"]
            )
            janela_editar = janela(
                title="Editar Produto",
                layout=layout
            )
            while True:
                events, value = janela_editar.read()

                if events == psg.WIN_CLOSED or events == "-cancel-":
                    janela_editar.close()
                    break

                elif events == "-Salvar-":

                    with open(self.db_app["db_estoque"], "r", encoding="utf8") as jsonFile:
                        data = json.load(jsonFile)

                    if edita_produto(value, data, index) == True:
                        janela_editar.close()
                        self.atualiza_info()

                    with open(self.db_app["db_estoque"], "w", encoding="utf8") as jsonFile:
                        json.dump(data, jsonFile, indent=4)


                    # -----------------------------------------------------
                    # Log Sistema
                    # -----------------------------------------------------
                    with open(self.db_app["db_estoque"], "r") as jsonFile:
                        data = json.load(jsonFile)
                    log(" ")
                    log("---------------- PRODUTO EDITADO ----------------")
                    log(f"Local: {self.db_app['db_estoque']}")
                    log(f"==> Nome do Produto: {data[index]['nome_do_produto']}")
                    log(f"==> Código do Produto: {data[index]['codigo']}")
                    log(f"==> Quantidade do Produto: {data[index]['quantidade']}")
                    log(f"==> Valor do Produto: {data[index]['valor']}")
                    log(f"==> Descrição do Produto: {data[index]['descricao']}")
                    log(f"==> Peso do Produto: {data[index]['peso']}")
                    log(f"==> Marca do Produto: {data[index]['marca']}")
                    log(" ")
                    # -----------------------------------------------------

                elif events == "-excluir-":
                    pop_up_confirm_delete = psg.popup_ok_cancel("Você quer EXCLUIR este item?")

                    if pop_up_confirm_delete == "OK":

                        with open(self.db_app["db_estoque"], "r") as jsonFile:
                            data = json.load(jsonFile)

                            # -----------------------------------------------------
                            # Log Sistema
                            # -----------------------------------------------------
                            log(" ")
                            log("---------------- PRODUTO EXCLUIDO ----------------")
                            log(f"Local: {self.db_app['db_estoque']}")
                            log(f"==> Nome do Produto: {data[index]['nome_do_produto']}")
                            log(f"==> Código do Produto: {data[index]['codigo']}")
                            log(f"==> Quantidade do Produto: {data[index]['quantidade']}")
                            log(f"==> Valor do Produto: {data[index]['valor']}")
                            log(f"==> Descrição do Produto: {data[index]['descricao']}")
                            log(f"==> Peso do Produto: {data[index]['peso']}")
                            log(f"==> Marca do Produto: {data[index]['marca']}")
                            log(" ")
                            # -----------------------------------------------------

                        del data[index]
                        janela_editar.close()
                        self.atualiza_info()

                        with open(self.db_app["db_estoque"], "w") as jsonFile:
                            json.dump(data, jsonFile, indent=4)

    def atualiza_info(self):
        self.valor_total = 0
        cont_valor = 0
        while cont_valor < len(tabela_produtos()):
            tabela_valor = tabela_produtos()
            self.valor_total += tabela_valor[cont_valor][6]
            self.quantidade_total += tabela_valor[cont_valor][2]
            cont_valor += 1
            self.janelas_cadastro_produtos["-valor_total_produtos-"].update(f'R$ {self.valor_total}')
            self.janelas_cadastro_produtos["-quantidade_total_produtos-"].update(self.quantidade_total)

# produto = Cadastro_Produtos()
# produto.execute()




class App:
    def __init__(self, db_app="dados/data.json", user=None, identificador=None):
        self.db_app = acessa_arquivo_json(db_app)
        self.nome_do_funcionario = user
        self.produtos = acessa_nome_do_produto()
        self.list_produtos_venda = []
        self.valor_total = 0.0


        tema()

        layout_app_header = [
            [
                psg.Text(text=self.db_app["nome_da_empresa"], font=f"{self.db_app['system_options']['font']} 20"),
                psg.Input(
                    key="-input_pesquisa_produto-",
                    border_width=0,
                    font=f"{self.db_app['system_options']['font']} 20",
                    size=(70,20),
                    enable_events=True
                )
            ],
            [
                psg.Listbox(values=self.produtos, key="-list-", size=(150,3))
            ]
        ]
        layout_app_main = [
            [
                psg.Text(f"Atendente: {self.nome_do_funcionario}", size=(30,1)),
                psg.Text(f"Data: {data_hora('data')}")
            ],
            [
                psg.Table(
                    values="",
                    headings=["Código do Produto", "Nome do Produto", "Quantidade", "Valor"],
                    key="-tabela_saida_vendas-",
                    auto_size_columns=False,
                    num_rows=28,
                    max_col_width=95,
                    row_height=20,
                    font=f"{self.db_app['system_options']['font']} 12",
                    col_widths=[20, 45, 12, 20],
                    header_border_width=1,
                    enable_click_events=True,
                    enable_events=True,
                    selected_row_colors="white on black"
                )
            ]
        ]
        layout_app_main_2 = [
            [
                psg.Text(text="TOTAL", font=f'self.db_app["system_option"]["font"] 16')
            ],
            [
                psg.Input(
                    default_text="",
                    font=f'self.db_app["system_option"]["font"] 40',
                    disabled=True,
                    text_color="black",
                    key="-saida_valor_total-"
                )
            ]
        ]
        menu_bar = [
            ["&App", ["App", "Configurações"]],
            ["&Sistema", "Estoque", "Clientes"]
        ]
        layou_app_frame = [
            [
                psg.Menu(menu_definition=menu_bar, key="-menu_bar-")
            ],
            [psg.Frame(title="", border_width=0, layout=layout_app_header)],
            [
                psg.Frame(title="", border_width=0, layout=layout_app_main),
                psg.Frame(title="info", border_width=2, layout=layout_app_main_2)
            ]
        ]
        self.janela_app = janela(f"System | {self.db_app['nome_da_empresa']}", layout=layou_app_frame)
        self.janela_app.maximize()
        self.janela_app['-input_pesquisa_produto-'].bind("<Return>", "_Enter")
        self.janela_app['-input_pesquisa_produto-'].bind("<Delete>", "_Delete")

    def execute(self):
        log("App iniciado...")

        self.produtos = acessa_nome_do_produto()

        while True:
            event, value = self.janela_app.read()
            # self.janela_app['-input_pesquisa_produto-'].set_focus(True)

            if event == psg.WIN_CLOSED:
                log("App encerrado...")
                break

            elif event == "Estoque":
                print("llaosiwi")
                Cadastro_Produtos().execute()
            else:
                self.janela_app['-list-'].update(self.produtos)

            if value['-input_pesquisa_produto-'] != '':

                search = value['-input_pesquisa_produto-'].upper()
                new_values = [x for x in self.produtos if search in x]
                self.janela_app['-list-'].update(new_values)

                if event == '-input_pesquisa_produto-' + "_Enter" and new_values != []:
                    self.realiza_compra()

                if event == '-input_pesquisa_produto-' + "_Delete" and new_values != []:
                    self.retira_produto_compra()

            elif value['-input_pesquisa_produto-'] == '':
                if event == '-input_pesquisa_produto-' + "_Enter"\
                        :
                    self.realiza_compra()

    def atualiza_tabela_venda(self):

        dados_produtos = acessa_arquivo_json(self.db_app["db_estoque"])
        tabela_saida = []
        cont = 0
        while cont < len(self.list_produtos_venda):
            tabela_venda_produto = [
                dados_produtos[self.list_produtos_venda[cont]]["codigo"],
                dados_produtos[self.list_produtos_venda[cont]]["nome_do_produto"],
                1,
                dados_produtos[self.list_produtos_venda[cont]]["valor"],
            ]
            tabela_saida.append(tabela_venda_produto)
            cont+=1

        self.janela_app["-tabela_saida_vendas-"].update(values=tabela_saida)
        self.janela_app["-saida_valor_total-"].update("R$ {:.2f}".format(self.valor_total))

    def realiza_compra(self):
        list = self.janela_app['-list-'].get_list_values()
        cont = 0
        dados_produtos = acessa_arquivo_json(self.db_app["db_estoque"])

        while cont < len(self.produtos):
            if list[0] == self.produtos[cont]:
                self.list_produtos_venda.append(cont)
                self.valor_total += float(dados_produtos[cont]["valor"])
            cont += 1

        self.atualiza_tabela_venda()

    def retira_produto_compra(self):
        list = self.janela_app['-list-'].get_list_values()
        dados_produtos = acessa_arquivo_json(self.db_app["db_estoque"])

        print(self.produtos)

        cont = 0
        while cont < len(self.produtos):
            if list[0] == self.produtos[cont]:
                if cont == self.list_produtos_venda[cont]:
                    del self.list_produtos_venda[cont]
                    self.valor_total -= float(dados_produtos[cont]["valor"])
            cont+=1
        self.atualiza_tabela_venda()


        #     Parou aqui
        # ========-=-=-=======================-----
        #
        #  Problema com o deletar dos produtos, varios são deletados sem ser eles proprios
        #   valor divergente toda vez que retira produtos
        #
        # Erro de última hora: Caso o produto não exista dá ERRO ao tentar procurar


    def encerrar_venda(self):
        log("Venda Finalizada...")

        # Limpar saidas
        self.list_produtos_venda = []
        self.janela_app["-tabela_saida_vendas-"].update(values=[])

app = App()
app.execute()
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
from PIL import Image
from venda import *

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
        self.tela_login['-user-'].bind("<Return>", "_Enter")
        self.tela_login['-identificador-'].bind("<Return>", "_Enter")

    def execute(self):
        log("Login iniciado...")
        while True:

            events, value = self.tela_login.read()

            if events == psg.WIN_CLOSED:
                log("Login encerrado...")
                break
            elif events == "-identificador-" + "_Enter" or events == "-user-" + "_Enter":
                if acessa_sistema(value["-user-"], value['-identificador-'], acessa_arquivo_json(self.db_app["db_funcionarios"])):
                    self.tela_login.close()

                    app = App(user=value["-user-"], identificador=value['-identificador-'])
                    app.execute()

            elif events == "-login-":
                if acessa_sistema(value["-user-"], value['-identificador-'], acessa_arquivo_json(self.db_app["db_funcionarios"])):
                    self.tela_login.close()

                    app = App(user=value["-user-"],identificador=value['-identificador-'])
                    app.execute()

                else:
                    popup_atencao(msg="User ou Identificador incorreto, tente novamente!")

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
        self.valor_total_venda = 0
        self.valor_total_custo = 0
        self.quantidade_total = 0

        tema()

        menu = [["Produto", ["Criar"]], ["Atualizar"]]

        layout = [
            [
                psg.Button(button_text="Novo", key="-novo-", border_width=0, focus=False),
                psg.Button(button_text="Atualizar", key="-atualizar-", border_width=0),
            ]
        ]
        valores_tabela = [
            "Nome do Produto",
            "Código",
            "Quantidade",
            "Uni. Custo",
            "%",
            "Uni. Venda",
            "Peso",
            "Marca",
            "T. Custo",
            "T. Venda",
            "T. Lucro"
        ]
        layout_main = [
            [
                psg.Table(
                    values=[[]],
                    headings=valores_tabela,
                    key="tabela_saida_produtos",
                    auto_size_columns=False,
                    num_rows=28,
                    max_col_width=95,
                    row_height=20,
                    font=f"{self.db_app['system_options']['font']} 12",
                    col_widths=[40, 15, 12, 12, 6, 12, 8, 8, 12],
                    header_border_width=1,
                    enable_click_events=True,
                    enable_events=True,
                    selected_row_colors="white on black",
                    expand_x=False,
                    expand_y=False,
                    alternating_row_color="gray20"
                )
            ]
        ]
        layout_footer = [
            [
                psg.Text(text="Valor Total Venda:"),
                psg.Text(text=f'', key="-valor_total_venda-")
            ],
            [
                psg.Text(text="Valor Total Custo:"),
                psg.Text(text=f'', key="-valor_total_custo-")
            ],
            [
                psg.Text(text="Quantidade Total:"),
                psg.Text(text=f'', key="-quantidade_total_produtos-")
            ],
            [
                psg.Text(text="Total Lucro:"),
                psg.Text(text=f'', key="-valor_total_lucro-")
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

                if value["-input_quantidade_do_produto-"] != "" and value["-input_valor_do_produto_custo-"] != '' and value["-input_nome_do_produto-"] != '':

                    if value["-input_quantidade_do_produto-"].isnumeric() or isfloat(value["-input_quantidade_do_produto-"].replace(",", ".")):
                        if value["-input_valor_do_produto_venda-"].isnumeric() or isfloat(value["-input_valor_do_produto_venda-"].replace(",", ".")):
                            if value["-input_valor_do_produto_custo-"].isnumeric() or isfloat(value["-input_valor_do_produto_custo-"].replace(",", ".")):
                                if value["-input_percentual_margem_do_produto-"].isnumeric() or isfloat(value["-input_percentual_margem_do_produto-"].replace(",", ".")):
                                    if value["-input_peso_do_produto-"].isnumeric() or isfloat(value["-input_peso_do_produto-"].replace(",", ".")) or value["-input_peso_do_produto-"] == "":
                                        self.cadastrar(
                                            value["-input_nome_do_produto-"].upper(),
                                            value["-input_codigo_do_produto-"],
                                            float(value["-input_quantidade_do_produto-"].replace(",", ".")),
                                            float(value["-input_valor_do_produto_custo-"].replace(",", ".")),
                                            float(value["-input_percentual_margem_do_produto-"].replace(",", ".")),
                                            calculo_criar_margem(
                                                float(value["-input_valor_do_produto_custo-"].replace(",", ".")),
                                                float(value["-input_percentual_margem_do_produto-"].replace(",", ".")),
                                                float(value["-input_valor_do_produto_venda-"].replace(",", "."))
                                            ),
                                            value["-input_descricao_do_produto-"].upper(),
                                            transform_float(value["-input_peso_do_produto-"]),
                                            value["-input_marca_do_produto-"]
                                        )
                                        popup_msg("Podruto cadastrado com sucesso!")
                                        janela_cadastro_novo_produto.close()

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

    def cadastrar(self, nome_do_produto, codigo_do_produto, quantidade, valor_custo, perc_margem, valor_venda, descricao, peso, marca):
        dados_preset = {
            "nome_do_produto": nome_do_produto,
            "codigo": codigo_do_produto,
            "quantidade": quantidade,
            "valor_custo": valor_custo,
            "perc_margem": perc_margem,
            "valor_venda": valor_venda,
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
        log(f"==> Valor do Custo: {valor_custo}")
        log(f"==> Percentual de Margem: {perc_margem}")
        log(f"==> Valor da Venda: {valor_venda}")
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
                valor_custo=dados[index]["valor_custo"],
                perc_margem=dados[index]["perc_margem"],
                valor_venda=dados[index]["valor_venda"],
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
                    log(f"==> Valor do Custo: {data[index]['valor_custo']}")
                    log(f"==> Percentual de Margem: {data[index]['perc_margem']}")
                    log(f"==> Valor da Venda: {data[index]['valor_venda']}")
                    log(f"==> Descrição do Produto: {data[index]['descricao']}")
                    log(f"==> Peso do Produto: {data[index]['peso']}")
                    log(f"==> Marca do Produto: {data[index]['marca']}")
                    log(" ")
                    # -----------------------------------------------------

                elif events == "-excluir-":
                    pop_up_confirm_delete = psg.popup_ok_cancel("Você quer EXCLUIR este item?", keep_on_top=True)

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
                            log(f"==> Valor do Custo: {data[index]['valor_custo']}")
                            log(f"==> Percentual de Margem: {data[index]['perc_margem']}")
                            log(f"==> Valor da Venda: {data[index]['valor_venda']}")
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
        self.valor_total_venda = 0
        self.valor_total_custo = 0
        self.valor_total_lucro = 0
        self.quantidade_total = 0
        cont_valor = 0
        while cont_valor < len(tabela_produtos()):
            tabela_valor = tabela_produtos()
            self.valor_total_venda += tabela_valor[cont_valor][5]
            self.valor_total_custo += tabela_valor[cont_valor][8]
            self.valor_total_lucro += tabela_valor[cont_valor][10]
            self.quantidade_total += tabela_valor[cont_valor][2]
            cont_valor += 1

        self.janelas_cadastro_produtos["-valor_total_venda-"].update(f'R$ {(self.valor_total_venda)}')
        self.janelas_cadastro_produtos["-valor_total_custo-"].update(f'R$ {self.valor_total_custo}')
        self.janelas_cadastro_produtos["-valor_total_lucro-"].update(f'R$ {self.valor_total_lucro}')
        self.janelas_cadastro_produtos["-quantidade_total_produtos-"].update(self.quantidade_total)

# -----------------------------------------------------------------------------
#      $$$$$$\
#     $$  __$$\
#     $$ /  $$ | $$$$$$\   $$$$$$\
#     $$$$$$$$ |$$  __$$\ $$  __$$\
#     $$  __$$ |$$ /  $$ |$$ /  $$ |
#     $$ |  $$ |$$ |  $$ |$$ |  $$ |
#     $$ |  $$ |$$$$$$$  |$$$$$$$  |
#     \__|  \__|$$  ____/ $$  ____/
#               $$ |      $$ |
#               $$ |      $$ |
#               \__|      \__|
# -----------------------------------------------------------------------------
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
                psg.Text(text='{}'.format((self.db_app["nome_da_empresa"]+" "*30)[:30]), font=f"{self.db_app['system_options']['font']} 20"),
                psg.Input(
                    key="-input_pesquisa_produto-",
                    border_width=0,
                    font=f"{self.db_app['system_options']['font']} 20",
                    size=(70,20),
                    enable_events=True
                )
            ],
            [
                psg.Listbox(values=self.produtos, key="-list-", size=(153,3))
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
                    headings=["Código do Produto", "Nome do Produto", "Quantidade", "Valor Uni.", "TOTAL"],
                    key="-tabela_saida_vendas-",
                    auto_size_columns=False,
                    num_rows=28,
                    max_col_width=95,
                    row_height=20,
                    font=(self.db_app['system_options']['font'], 12, "bold"),
                    col_widths=[20, 45, 12, 12, 12],
                    header_border_width=1,
                    enable_click_events=True,
                    enable_events=True,
                    selected_row_colors="white on black"
                )
            ]
        ]
        layout_app_main_2 = [
            [
                psg.Text(text="TOTAL", font=f'{self.db_app["system_options"]["font"]} 16')
            ],
            [
                psg.Input(
                    default_text="",
                    font=(self.db_app["system_options"]["font"], 40, "bold"),
                    disabled=True,
                    text_color="black",
                    key="-saida_valor_total-"
                )
            ],
            [
                psg.Frame(title="Atalhos:", border_width=1, layout=mostra_atalhos(), pad=[10,40])
            ]
        ]
        menu_bar = [
            ["&App", ["App", "Configurações"]],
            ["&Sistema", ["Estoque", "Clientes", "Registro de Vendas"]]
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
        self.janela_app = janela(
            f"System",
            layout=layou_app_frame,
            modo="fullscreen"
        )
        self.janela_app.maximize()
        self.janela_app['-input_pesquisa_produto-'].bind("<Return>", "_Enter")
        self.janela_app['-input_pesquisa_produto-'].bind("<Delete>", "_Delete")
        self.janela_app['-input_pesquisa_produto-'].bind("<F2>", "_F2")
        self.janela_app['-input_pesquisa_produto-'].bind("<F1>", "_F1")
        self.janela_app['-input_pesquisa_produto-'].bind("<End>", "_End")
        self.janela_app['-input_pesquisa_produto-'].bind("<Insert>", "_Insert")



    def execute(self):
        log("App iniciado...")

        self.produtos = acessa_nome_do_produto()

        while True:
            event, value = self.janela_app.read()

            if event == psg.WIN_CLOSED:
                log("App encerrado...")
                break

            elif event == "Estoque":
                Cadastro_Produtos().execute()

            elif event == "Registro de Vendas":
                App_Venda().execute()

            else:
                self.janela_app['-list-'].update(self.produtos)

            if event == '-input_pesquisa_produto-' + "_End" and self.valor_total != 0.00:
                self.encerrar_venda()

            if value['-input_pesquisa_produto-'] != '':

                search = value['-input_pesquisa_produto-'].upper()
                new_values = [x for x in self.produtos if search in x]
                self.janela_app['-list-'].update(new_values)

                if event == '-input_pesquisa_produto-' + "_Enter" and new_values != []:
                    self.realiza_compra()

                elif event == '-input_pesquisa_produto-' + "_F2" and new_values != []:
                        self.retira_produto_compra(mode="all")

                elif event == '-input_pesquisa_produto-' + "_F1":
                    if psg.popup_ok_cancel("Tem certeza que dejesa cancelar a venda?", keep_on_top=True) == "OK":
                        self.limpa_venda()

                elif event == '-input_pesquisa_produto-' + "_Delete" and new_values != []:
                    self.retira_produto_compra()

                elif event == '-input_pesquisa_produto-' + "_End":
                    self.encerrar_venda()

                elif event == '-input_pesquisa_produto-' + "_Insert":
                    self.add_avulso()

            elif value['-input_pesquisa_produto-'] == "":
                if event == '-input_pesquisa_produto-' + "_Delete":
                    self.retira_produto_compra(mode="fim")

                elif event == '-input_pesquisa_produto-' + "_Insert":
                    self.add_avulso()

            elif value['-input_pesquisa_produto-'] == '' and event == '-input_pesquisa_produto-' + "_Enter":
                self.realiza_compra()

            self.janela_app['-input_pesquisa_produto-'].set_focus(True)


    def atualiza_tabela_venda(self):

        dados_produtos = acessa_arquivo_json(self.db_app["db_estoque"])
        tabela_saida = []
        cont = 0
        while cont < len(self.list_produtos_venda):
            tabela_venda_produto = [
                self.list_produtos_venda[cont]["codigo"],
                self.list_produtos_venda[cont]["nome_do_produto"],
                self.list_produtos_venda[cont]["quantidade"],
                self.list_produtos_venda[cont]["valor_unitario"],
                f"{self.list_produtos_venda[cont]['valor_total']:.2f}"
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

                semelhante = False
                index_semelhante = 0
                while index_semelhante < len(self.list_produtos_venda):
                    if cont == self.list_produtos_venda[index_semelhante]["id"]:

                        self.list_produtos_venda[index_semelhante]["quantidade"]+=1
                        self.list_produtos_venda[index_semelhante]["valor_total"]+=dados_produtos[cont]["valor_venda"]
                        semelhante = True
                        break
                    index_semelhante+=1

                if semelhante == False:
                    quantidade_itens = 1
                    preset_produto = {
                        "id": cont,
                        "nome_do_produto": dados_produtos[cont]["nome_do_produto"],
                        "codigo": dados_produtos[cont]["codigo"],
                        "valor_unitario": dados_produtos[cont]["valor_venda"],
                        "quantidade": quantidade_itens,
                        "valor_total": dados_produtos[cont]['valor_venda']
                    }
                    self.list_produtos_venda.append(preset_produto)

                self.valor_total += float(dados_produtos[cont]["valor_venda"])
                self.janela_app['-input_pesquisa_produto-'].update(value="")
            cont += 1

        self.atualiza_tabela_venda()

    def add_avulso(self):

        valor_avulso = popup_valor()

        if valor_avulso == None:
            pass
        else:
            preset_produto = {
                "id": "avulso",
                "nome_do_produto": "Valor Avulso",
                "codigo": 000000000000,
                "valor_unitario": valor_avulso,
                "quantidade": 1,
                "valor_total": valor_avulso
            }
            self.list_produtos_venda.append(preset_produto)
            self.valor_total += valor_avulso
            self.atualiza_tabela_venda()

    def retira_produto_compra(self, mode=""):

        list = self.janela_app['-list-'].get_list_values()
        cont = 0
        dados_produtos = acessa_arquivo_json(self.db_app["db_estoque"])

        if mode == "fim":
            self.valor_total -= self.list_produtos_venda[len(self.list_produtos_venda)-1]["valor_total"]
            del self.list_produtos_venda[len(self.list_produtos_venda)-1]

        else:
            while cont < len(self.produtos):

                if list[0] == self.produtos[cont]:

                    index_semelhante = 0
                    while index_semelhante < len(self.list_produtos_venda):
                        if cont == self.list_produtos_venda[index_semelhante]["id"]:

                            if mode == "all":

                                self.valor_total -= self.list_produtos_venda[index_semelhante]["valor_total"]
                                del self.list_produtos_venda[index_semelhante]
                                break

                            elif self.list_produtos_venda[index_semelhante]["quantidade"] != 1:

                                self.list_produtos_venda[index_semelhante]["quantidade"] -= 1
                                self.list_produtos_venda[index_semelhante]["valor_total"] -= dados_produtos[cont]["valor_venda"]
                                self.valor_total -= dados_produtos[cont]["valor_venda"]
                                break

                            elif self.list_produtos_venda[index_semelhante]["quantidade"] == 1:

                                self.valor_total -= self.list_produtos_venda[index_semelhante]["valor_total"]
                                del self.list_produtos_venda[index_semelhante]
                                break

                        index_semelhante += 1

                    cont_2 = 0
                    while cont_2 < len(self.list_produtos_venda):

                        if cont == self.list_produtos_venda[cont_2]:
                            if self.list_produtos_venda != []:
                                self.list_produtos_venda.remove(cont)
                                self.valor_total -= float(dados_produtos[cont]["valor_venda"])
                                break
                        cont_2+=1

                cont += 1
        self.atualiza_tabela_venda()


    def encerrar_venda(self):
        log("Venda finalizada...")

        layout_forma_de_pagamento = [
            [psg.Text(text="Forma de Pagamento")],
            [
                psg.Listbox(
                    values=[
                        "Dinheiro",
                        "Cartão - Debito",
                        "Cartão - Credito",
                        "PIX",
                        "Boleto",
                        "Vale",
                        "Ticket"
                    ],
                    size=(20,7),
                    key="-escolha_pagamento-",
                    bind_return_key=True,
                    enable_events=True,
                    select_mode="LISTBOX_SELECT_MODE_SINGLE",
                    change_submits=True,
                    no_scrollbar=True,
                    pad=[100, 100],
                    font=(f'{self.db_app["system_options"]["font"]}', 20, "bold")

                )
            ]
        ]
        layout_info_pagamento = [
            [psg.Text(text="Total da Compra:", font=(self.db_app["system_options"]["font"], 20, "bold"))],
            [
                psg.Input(
                    default_text=f"R$ {self.valor_total:.2f}",
                    font=(f'{self.db_app["system_options"]["font"]}', 30, "bold"),
                    key="-output_preco_total-",
                    disabled=True,
                    size=[15,1],
                    text_color="black"
                )
            ],
            [psg.Text(text="Troco:", font=(self.db_app["system_options"]["font"], 20, "bold"))],
            [
                psg.Input(
                    default_text="R$ 0.00",
                    font=(f'{self.db_app["system_options"]["font"]}', 30, "bold"),
                    key="-output_troco_total-",
                    disabled=True,
                    size=[15,1],
                    text_color = "black"
                )
            ]

        ]
        clientes = mostra_clientes(mode="nome")
        layout_frame_forma_de_pagamento = [
            [
                psg.Frame(title="", border_width=0, layout=layout_forma_de_pagamento),
                psg.Frame(title="", border_width=0, layout=layout_info_pagamento, pad=[100, 100],)
            ],
            [
                psg.Frame(title="Atalhos:", border_width=1, layout=mostra_atalhos(mode="atalhos_end"), pad=[10, 0]),
            ]
        ]

        janela_forma_de_pagamento = janela(title="Finalizar Venda", layout=layout_frame_forma_de_pagamento)
        janela_forma_de_pagamento.bind("<Escape>", "_Esc")

        metodo_de_pagamento = ""

        while True:
            event, value = janela_forma_de_pagamento.read()
            troco_element = janela_forma_de_pagamento["-output_troco_total-"]
            janela_forma_de_pagamento["-escolha_pagamento-"].set_focus()

            if event == psg.WIN_CLOSED:
                break

            elif event == "-escolha_pagamento-":
                db_software = acessa_arquivo_json("dados/data.json")

                if value[event] == ["Dinheiro"]:
                    valor_troco = popup_valor()

                    if valor_troco == None:
                        troco_element.update(value=0.0)
                    else:
                        if valor_troco < self.valor_total:
                            pass
                        else:
                            saida_troco_valor = self.valor_total - valor_troco
                            troco_element.update(value=f'R$ {saida_troco_valor:.2f}')
                            metodo_de_pagamento = "Dinheiro"

                elif value[event] == ["PIX"]:

                    config_pagamentos = acessa_arquivo_json("dados/app_config_pay.json")
                    chave = str(config_pagamentos["chave"])
                    nome = config_pagamentos["nome_do_destinatario"]
                    cidade = config_pagamentos["cidade"]
                    saida_qr = ''

                    from pixqrcodegen import Payload

                    payload = Payload(nome, chave, str(self.valor_total), cidade, "transferencia")
                    saida_qr = payload.gerarPayload()
                    log("QRCode PIX foi gerado.")

                    layout_img_pix = [
                        [psg.Image("assets/pix_qr.png")],
                        [mostra_atalhos(mode="atalhos_img_pix")]
                    ]

                    janela_img_pix = janela(title="QRCode PIX", layout=layout_img_pix, force_toplevel=True, keep_on_top=True)
                    janela_img_pix.force_focus()
                    janela_img_pix.bind("<Escape>", "_Esc")
                    janela_img_pix.bind("<BackSpace>", "_BackSpace")

                    while True:
                        event, velue = janela_img_pix.read()

                        if event == psg.WIN_CLOSED or event == "_BackSpace":
                            janela_img_pix.close()
                            break
                        if event == "_Esc":
                            self.guarda_venda(
                                metodo_de_pagamento,
                                self.nome_do_funcionario,
                                value["-output_troco_total-"]
                            )
                            janela_img_pix.close()
                            janela_forma_de_pagamento.close()
                            self.limpa_venda()
                            break

            elif event == "_Esc":
                if metodo_de_pagamento != "":
                    self.guarda_venda(
                        metodo_de_pagamento,
                        self.nome_do_funcionario,
                        value["-output_troco_total-"]
                    )
                    janela_forma_de_pagamento.close()
                    self.limpa_venda()
                    break


    def guarda_venda(self, metodo_de_pagamento, vendedor, troco=0.0, cliente=""):

        psg.popup_no_buttons(
            "Compra finalizada!",
            keep_on_top=True,
            auto_close=True,
            auto_close_duration=1.5,
            font=(f'{self.db_app["system_options"]["font"]}', 30, "bold"),
            no_titlebar=True
        )

        preset_dados_venda = {
            "data": data_hora(mode="all"),
            "vendedor": vendedor,
            "cliente": cliente,
            "metodo_de_pagamento": metodo_de_pagamento,
            "total": float(truncate(self.valor_total, 2)),
            "troco": troco,
            "list_produtos": []
        }

        cont = 0
        while cont < len(self.list_produtos_venda):

            preset_dados_venda["list_produtos"].append(self.list_produtos_venda[cont])

            with open(self.db_app["db_estoque"], "r", encoding="utf8") as jsonFile:
                data = json.load(jsonFile)

            quantidade_item = data[self.list_produtos_venda[cont]["id"]]["quantidade"] - self.list_produtos_venda[cont]["quantidade"]
            data[self.list_produtos_venda[cont]["id"]]["quantidade"] = quantidade_item

            with open(self.db_app["db_estoque"], "w", encoding="utf8") as jsonFile:
                json.dump(data, jsonFile, indent=4)

            cont+=1

        while True:
            if os.path.isfile(f"dados/pdv/{data_hora(mode='data-log')}_pdv.json"):

                with open(f"dados/pdv/{data_hora(mode='data-log')}_pdv.json", "r", encoding='utf8') as file:
                    dados = json.load(file)

                dados["vendas"].append(preset_dados_venda)

                with open(f"dados/pdv/{data_hora(mode='data-log')}_pdv.json", "w", encoding='utf8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                break

            else:
                # Cria o arquivo de venda que está inexistente
                dados_pdv = {
                    "data": data_hora("data"),
                    "primeira_venda": data_hora("all"),
                    "vendas": []
                }
                with open(f"dados/pdv/{data_hora(mode='data-log')}_pdv.json", "w", encoding='utf8') as arquivo:
                    json.dump(dados_pdv, arquivo, indent=4, ensure_ascii=False)
                continue

    #
    def limpa_venda(self):
        self.list_produtos_venda = []
        self.valor_total = 0
        self.janela_app["-tabela_saida_vendas-"].update(values=[])
        self.janela_app["-saida_valor_total-"].update(value="")
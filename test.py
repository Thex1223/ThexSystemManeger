from functions import *
import json
import PySimpleGUI as psg
import os
from PIL import Image
from app import *


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
        self.janela_app = janela(f"System | {self.db_app['nome_da_empresa']}", layout=layou_app_frame)
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
                        self.list_produtos_venda[index_semelhante]["valor_total"]+=dados_produtos[cont]["valor"]
                        semelhante = True
                        break
                    index_semelhante+=1

                if semelhante == False:
                    quantidade_itens = 1
                    preset_produto = {
                        "id": cont,
                        "nome_do_produto": dados_produtos[cont]["nome_do_produto"],
                        "codigo": dados_produtos[cont]["codigo"],
                        "valor_unitario": dados_produtos[cont]["valor"],
                        "quantidade": quantidade_itens,
                        "valor_total": dados_produtos[cont]['valor']
                    }
                    self.list_produtos_venda.append(preset_produto)

                self.valor_total += float(dados_produtos[cont]["valor"])
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
                                self.list_produtos_venda[index_semelhante]["valor_total"] -= dados_produtos[cont]["valor"]
                                self.valor_total -= dados_produtos[cont]["valor"]
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
                                self.valor_total -= float(dados_produtos[cont]["valor"])
                                break
                        cont_2+=1

                cont += 1
        self.atualiza_tabela_venda()


    def encerrar_venda(self):
        log("Venda finalizada...")

        clientes = mostra_clientes(mode="nome")

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
        layout_frame_forma_de_pagamento = [
            [
                psg.Frame(title="", border_width=0, layout=layout_forma_de_pagamento),
                psg.Frame(title="", border_width=0, layout=layout_info_pagamento, pad=[100, 100],)
            ],
            [
                psg.Frame(title="Atalhos:", border_width=1, layout=mostra_atalhos(mode="atalhos_end"), pad=[10, 0])
            ]
        ]

        janela_forma_de_pagamento = janela(title="Finalizar Pagamento", layout=layout_frame_forma_de_pagamento)
        janela_forma_de_pagamento.bind("<Escape>", "_Esc")

        metodo_de_pagamento = ""

        while True:
            event, value = janela_forma_de_pagamento.read()
            troco_element = janela_forma_de_pagamento["-output_troco_total-"]

            print(event)

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

        psg.popup_auto_close("Compra finalizada", auto_close_duration=2, keep_on_top=True)

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

    def limpa_venda(self):
        self.list_produtos_venda = []
        self.valor_total = 0
        self.janela_app["-tabela_saida_vendas-"].update(values=[])
        self.janela_app["-saida_valor_total-"].update(value="")


app = App()
app.execute()

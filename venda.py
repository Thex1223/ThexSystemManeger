from functions import *


class App_Venda:
    def __init__(self):
        self.diretory = "dados/pvd"

        tema()

        layout_header = [
            [
                psg.Text(text="...")
            ]
        ]
        treedata = psg.TreeData()
        file_data = []

        pasta = './dados/pdv' # ALTERAR PARA DATA.JSON
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                file_data.append(f'{os.path.join(diretorio, arquivo)[len(pasta) + 1:]}')
        tree_data_preset = []

        if file_data == []:
            tree_data_preset.append(["", "-", "Nenhum registro encontrado", "Faça uma venda!"])

        index_arquivo = 0
        while index_arquivo < len(file_data):
            with open(f'{pasta}/{file_data[index_arquivo]}', "r", encoding="utf8") as file:
                arquivo = json.load(file)

            # Header
            tree_data_preset.append(["", f"{file_data[index_arquivo][:5]}", f"{file_data[index_arquivo][:10]}", "Fechado"])
            # Main
            tree_data_preset.append([f"{file_data[index_arquivo][:5]}", "data", "Data:", arquivo["data"]])
            tree_data_preset.append([f"{file_data[index_arquivo][:5]}", "primeira_venda", "Primeira Venda:", arquivo["primeira_venda"]])
            tree_data_preset.append([f"{file_data[index_arquivo][:5]}", "vendas", "Vendas:", "[Clique para mostrar]"])

            index_vendas = 0
            vendas = arquivo["vendas"]
            while index_vendas < len(vendas):
                tree_data_preset.append(["vendas", "--", "__________________________________", "__________________________________"])
                tree_data_preset.append([
                    "vendas",
                    f"vendas_sub{index_vendas}",
                    f"Venda: {index_vendas}",
                    (
                        f"{vendas[index_vendas]['total']:.2f} | {(vendas[index_vendas]['data'])[14:22]}"
                    )
                ])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "data_hora", "Data e Hora:", vendas[index_vendas]["data"]])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "vendedor", "Vendedor:", vendas[index_vendas]["vendedor"]])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "cliente", "Cliente:", vendas[index_vendas]["cliente"]])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "metodo_de_pagamento", "Metodo de pagamento:", vendas[index_vendas]["metodo_de_pagamento"]])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "total", "Total:", f'{float(vendas[index_vendas]["total"]):.2f}'])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "troco", "Troco:", vendas[index_vendas]["troco"]])
                tree_data_preset.append([f"vendas_sub{index_vendas}", "list_produtos", "Produtos vendidos:", "..."])

                # Produtos
                index_produtos_venda = 0
                while index_produtos_venda < len(vendas[index_vendas]["list_produtos"]):
                    tree_data_preset.append(["list_produtos", "--", "", ""])
                    tree_data_preset.append([
                        "list_produtos",
                        "id",
                        "ID:",
                        vendas[index_vendas]["list_produtos"][index_produtos_venda]["id"]
                    ])
                    tree_data_preset.append([
                        "list_produtos",
                        "nome",
                        "Nome do Produto:",
                        vendas[index_vendas]["list_produtos"][index_produtos_venda]["nome_do_produto"]
                    ])
                    tree_data_preset.append([
                        "list_produtos",
                        "codigo",
                        "Código:",
                        vendas[index_vendas]["list_produtos"][index_produtos_venda]["codigo"]
                    ])
                    tree_data_preset.append([
                        "list_produtos",
                        "quantidade",
                        "Quantidade",
                        vendas[index_vendas]["list_produtos"][index_produtos_venda]["quantidade"]
                    ])
                    tree_data_preset.append([
                        "list_produtos",
                        "valor_total",
                        "Valor Total:",
                        vendas[index_vendas]["list_produtos"][index_produtos_venda]["valor_total"]
                    ])
                    index_produtos_venda+=1

                index_vendas+=1

            index_arquivo+=1


        for row in tree_data_preset:
            treedata.Insert(row[0], row[1], row[2], row[3:])
        layout_frame = [
            [
                psg.Tree(
                    data=treedata,
                    headings=["Info"],
                    col0_heading="",
                    col0_width=25,
                    col_widths=[80],
                    row_height=40,
                    font=(db_software["system_options"]["font"], 12, "bold"),
                    num_rows=30,
                    expand_x=True,
                )
            ]
        ]

        self.janela_app_vendas = psg.Window(
            title="Registro de Vendas",
            layout=layout_frame,
            size=[1000,800],
            force_toplevel=True,
            keep_on_top=True
        )

    def execute(self):
        log("Registro de vendas ACESSADO")
        while True:
            event, value = self.janela_app_vendas.read()
            if event == psg.WIN_CLOSED:
                log("Registro de vendas FECHADO")
                break
import PySimpleGUI

from functions import *
db_software = acessa_arquivo_json("dados/data.json")

class App_Config:
    def __init__(self):
        tema()

        layout_main_geral = [
            [
                psg.Text(text="Nome da empresa:", size=(25,1)),
                psg.Input(default_text=db_software["nome_da_empresa"], key="-nome_da_empresa-", size=(25,1))
            ],
            [
                psg.Text(text="Tema:", size=(25,1)),
                psg.Combo(
                    values=db_software["system_options"]["theme"],
                    default_value=db_software["system_options"]["theme"][0],
                    key="-tema-",
                    size=(24,1),
                    enable_events=True
                )
            ],
            [
                psg.Text(text="Habilitar Log:", size=(25,1)),
                psg.Checkbox(default=True, key="-log-", text="")
            ]
        ]
        layout_main_dados = [
            [
                psg.Text(text="CONFIGURAÇÕES SENSIVEIS, CUIDADO!", text_color="red")
            ],
            [
                psg.Text(text="Não alterar, se não souber!", text_color="red")
            ]
        ]
        layout_main = [
            [
                psg.Tab(title="Geral", layout=layout_main_geral),
                psg.Tab(title="Dados", layout=layout_main_dados)
            ]
        ]
        layout_footer = [
            [
                psg.Button(button_text="Cancelar", key="-cancelar-"),
                psg.Button(button_text="Salvar", key="-salvar-")
            ]
        ]

        layout_frame = [
            [
                psg.TabGroup(layout=layout_main)
            ],
            [
                psg.Frame(title="", layout=layout_footer, border_width=0)
            ]
        ]

        self.janela_config = psg.Window(title="Configurações", layout=layout_frame)

    def execute(self):
        while True:
            event, value = self.janela_config.read()
            print(event)

            if event == psg.WIN_CLOSED or event == "-cancelar-":
                break

            if event == "-salvar-":
                # Atualiza Geral
                db_software["nome_da_empresa"] = value["-nome_da_empresa-"]
                cont = 0
                while cont < len(db_software["system_options"]["theme"]):
                    if value['-tema-'] == db_software["system_options"]["theme"][cont]:
                        db_software["system_options"]["theme_select"] = cont
                    cont+=1
                db_software["nome_da_empresa"] = value["-log-"]

                # Atualiza Dados

                print(db_software)

            if event == "-tema-":
                psg.theme(value["-tema-"])




App_Config().execute()
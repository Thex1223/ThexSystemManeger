# -----------------------------------------------------------------------------
#     $$$$$$\                 $$\
#     \_$$  _|                $$ |
#       $$ |  $$$$$$$\   $$$$$$$ | $$$$$$\  $$\   $$\
#       $$ |  $$  __$$\ $$  __$$ |$$  __$$\ \$$\ $$  |
#       $$ |  $$ |  $$ |$$ /  $$ |$$$$$$$$ | \$$$$  /
#       $$ |  $$ |  $$ |$$ |  $$ |$$   ____| $$  $$<
#     $$$$$$\ $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$  /\$$\
#     \______|\__|  \__| \_______| \_______|\__/  \__|
#
#     $$$$$$$$\ $$\
#     \__$$  __|$$ |
#        $$ |   $$$$$$$\   $$$$$$\  $$\   $$\
#        $$ |   $$  __$$\ $$  __$$\ \$$\ $$  |
#        $$ |   $$ |  $$ |$$$$$$$$ | \$$$$  /
#        $$ |   $$ |  $$ |$$   ____| $$  $$<
#        $$ |   $$ |  $$ |\$$$$$$$\ $$  /\$$\
#        \__|   \__|  \__| \_______|\__/  \__|
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
#
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
# -----------------------------------------------------------------------------
#   Creator By: Thex 1223
#   Equip: Kainan H (na18k)
#
#   Creted in: 2023    // Lasted Update:  25/01/2023
#
#   Version: v0.0.1-alpha
# -----------------------------------------------------------------------------


from functions import *
from app import *


tela_login = Login()
tela_login.execute()



































# -----------------------------------------------------------------------------
#     $$$$$$$\             $$\               $$\
#     $$  __$$\            $$ |              $$ |
#     $$ |  $$ | $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\
#     $$ |  $$ | \____$$\\_$$  _|   \____$$\ $$  __$$\  \____$$\ $$  _____|$$  __$$\
#     $$ |  $$ | $$$$$$$ | $$ |     $$$$$$$ |$$ |  $$ | $$$$$$$ |\$$$$$$\  $$$$$$$$ |
#     $$ |  $$ |$$  __$$ | $$ |$$\ $$  __$$ |$$ |  $$ |$$  __$$ | \____$$\ $$   ____|
#     $$$$$$$  |\$$$$$$$ | \$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\
#     \_______/  \_______|  \____/  \_______|\_______/  \_______|\_______/  \_______|
# -----------------------------------------------------------------------------

data_software = acessa_arquivo_json("dados/data.json")
# data_funcionarios = acessa_arquivo_json("dados/funcionarios.json")
# data_clientes = acessa_arquivo_json("dados/clientes.json")
# data_estoque = acessa_arquivo_json("dados/estoque.json")

# -----------------------------------------------------------------------------
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

# cliente = Cliente(data_clientes)
# print(cliente.carrega_clientes)
# cliente.criar_cliente("Mario", "91892939939", "999.999.999-01", "sla", 90, "a", "Gralha", "FRG")
#
# app_login_janela = App_Login(data_software, data_funcionarios).execute()
#
#
# if credenciais("login") == True:
#     app = App(
#         data_software,
#         data_funcionarios,
#         data_clientes,
#         data_estoque,
#         data_software["system_options"]["width"],
#         data_software["system_options"]["heigt"]
#     ).execute()





# acessa_sistema("Kainan Henrique", "10002", data_funcionarios)

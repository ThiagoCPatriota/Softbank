from defs.instalação_bibliotecas import instalacao_bibliotecas

instalacao_bibliotecas()

import flet as ft
from defs.cadastro_login import *

def main(page :ft.Page):
    page.controls.clear()
    page.window_width = 1080  
    page.window_height = 720

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.ACCOUNT_BALANCE_SHARP),
        title = ft.Text('Softbank'),
        center_title = True,
        bgcolor = '#46295A', #roxo
    )

    Cadslog(page)
    page.update()

ft.app(target=main)



#                           19497681046
#Outro Cartão               5473048247691013



#                           64042544096
#Cartao para testes:        4532015112830366
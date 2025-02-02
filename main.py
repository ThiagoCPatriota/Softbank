from defs.instalação_bibliotecas import instalacao_bibliotecas

instalacao_bibliotecas()

import flet as ft
from defs.cadastro_login import *

def main(page :ft.Page):
    page.controls.clear()
    page.window.width = 1080  
    page.window.height = 720
    

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.Icons.ACCOUNT_BALANCE_SHARP),
        title = ft.Text('Softbank'),
        center_title = True,
        bgcolor = '#46295A', #roxo
    )

    Cadslog(page)
    page.update()

ft.app(target=main)



#     CPF1                  19497681046
#Outro Cartão               5473048247691013



#     CPF2                  64042544096
#Cartao para testes:        4532015112830366
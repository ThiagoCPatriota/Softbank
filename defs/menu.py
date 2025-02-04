import flet as ft
from interface.depo import Deposito
from interface.moeda import Moedas
from interface.pessoa import Perfil
from interface.saque import Retirar
from interface.area_pix import area_pix
def Menu_principal(page, conta):
    page.controls.clear()
    page.appbar.actions = [
        ft.PopupMenuButton(
            items = [
                ft.PopupMenuItem(
                    icon = ft.Icons.LOGOUT_SHARP,
                    text='Sair',
                    on_click = lambda e: page.window.close()
                )
            ]
        )
    ]
    page.window.width = 400  
    page.window.height = 800
    Perfil(page, conta)
    Nav(page, conta)
    page.update()

def Nav(page, conta):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label='Perfil'),
            ft.NavigationBarDestination(icon=ft.Icons.CURRENCY_BITCOIN_SHARP, label='Moeda'),
            ft.NavigationBarDestination(icon=ft.Icons.ATTACH_MONEY_SHARP, label='Saque'),
            ft.NavigationBarDestination(icon=ft.Icons.MOVE_TO_INBOX_ROUNDED, label='Deposito'),
            ft.NavigationBarDestination(icon=ft.Icons.PIX, label='Área pix'),
        ],
        on_change=lambda e: hot_bar(e, page, conta),
    )
    page.update()

def hot_bar(e, page, conta):
    if e.control.selected_index == 0:
        Perfil(page, conta) 
    elif e.control.selected_index == 1:
        Moedas(page)
    elif e.control.selected_index == 2:
        Retirar(page, conta)
    elif e.control.selected_index == 3:
        Deposito(page, conta)
    elif e.control.selected_index == 4:
        area_pix(page, conta)
    page.update()



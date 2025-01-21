import flet as ft
from interface.depo import Deposito
from interface.moeda import Moedas
from interface.pessoa import Perfil
from interface.saque import Retirar

def Nav(page, conta):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PERSON, label='Perfil'),
            ft.NavigationDestination(icon=ft.icons.CURRENCY_BITCOIN_SHARP, label='Moeda'),
            ft.NavigationDestination(icon=ft.icons.ATTACH_MONEY_SHARP, label='Saque'),
            ft.NavigationDestination(icon=ft.icons.MOVE_TO_INBOX_ROUNDED, label='Deposito'),
        ],
        on_change=lambda e: hot_bar(e, page, conta),
    )





def hot_bar(e, page, conta):
    if e.control.selected_index == 0:
        Perfil(page, conta) 
    elif e.control.selected_index == 1:
        Moedas(page)
    elif e.control.selected_index == 2:
        Retirar(page, conta)
    elif e.control.selected_index == 3:
        Deposito(page, conta)
    page.update()


def Menu_principal(page, conta):
    page.controls.clear()
    page.appbar.actions = [
        ft.PopupMenuButton(
            items = [
                ft.PopupMenuItem(
                    icon = ft.Icons.LOGOUT_SHARP,
                    text='Sair',
                    on_click = lambda e: page.window_close()
                )
            ]
        )
    ]
    page.window_width = 400  
    page.window_height = 800
    Nav(page, conta)
    Perfil(page, conta)
    page.update()

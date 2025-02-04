import flet as ft
from defs.utilitarios import obter_cotacao_bitcoin
def Moedas(page):
    page.controls.clear()
    cotacao = obter_cotacao_bitcoin()
    container_Moeda = ft.Container(
        content = ft.Stack(
            controls=[
                ft.Container(
                    ft.Image(
                        src = 'imgs/all_menu_bg.jpg',
                        fit = ft.ImageFit.COVER
                    ),
                    expand=True,
                    opacity = 0.2
                ),
                ft.Container(
                    content = ft.Column(
                        controls = [
                            ft.Image(
                                src = 'imgs/bitcoin.png',
                                width=100,  
                                height=100,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text(
                                value = f'A cotação do Bitcoin hoje é:\n R$ {cotacao}',
                                size = 24,
                                weight = 'bold'
                            )
                        ],
                        spacing=10,  # Espaçamento vertical entre os itens
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                )
            ],
            alignment=ft.alignment.center, 
        )
    )

    page.add(container_Moeda)
    page.update()
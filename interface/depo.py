import flet as ft

def Deposito(page, conta):
    page.controls.clear()
    dep = ft.TextField(label='Quanto deseja Depositar: ')
    mensagem = ft.Text(value='')
    mensagem.color='RED'
    def confirmar_deposito(e):

        if not dep.value:
            mensagem.value = 'Valor inválido.'
        else:
            try:
                valor_saque = float(dep.value)
                conta.saldo += valor_saque
                conta.save()
                mensagem.color = 'green'
                mensagem.value = f'Foram depositados na conta {conta.usuario}, R${dep.value}'
                page.update()
            except ValueError:
                mensagem.value = 'Valor inválido. Por favor, insira um número.'
        page.update()
    container_Deposito = ft.Container(
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
                            dep,
                            ft.ElevatedButton(
                            'Depositar',
                            on_click = lambda e: confirmar_deposito(page)
                            ),
                            mensagem
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

    page.add(container_Deposito)
    page.update()
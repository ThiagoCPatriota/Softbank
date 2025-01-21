import flet as ft

def Retirar(page, conta):
    page.controls.clear()
    saq = ft.TextField(label='Quanto deseja Sacar: ')
    mensagem = ft.Text(value='')
    mensagem.color='RED'
    def confirmar_saque(e):
        valor_saque = float(saq.value)
        if valor_saque > conta.saldo:
            mensagem.value = 'Saque maior que o saldo da conta, tentativa negada!'
        elif not saq.value:
            mensagem.value = 'Valor inválido.'
        elif valor_saque > 10000:
            mensagem.value = 'Saque maior que R$10000, tentativa negada!'
        else:
            try:
                conta.saldo -= valor_saque
                conta.save()
                mensagem.color = 'green'
                mensagem.value = f'Foi sacado da conta {conta.usuario}, R${saq.value}'
                page.update()
            except ValueError:
                mensagem.value = 'Valor inválido. Por favor, insira um número.'
        page.update()
    container_saque = ft.Container(
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
                            saq,
                            ft.ElevatedButton(
                            'Sacar',
                            on_click = lambda e: confirmar_saque(page)
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

    page.add(container_saque)
    page.update()
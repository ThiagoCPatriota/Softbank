import flet as ft
def Perfil(page, conta):
    page.controls.clear()
    container_pessoa = ft.Container(
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
                    expand = True,
                    content = ft.Column(
                        controls = [
                            ft.Text(
                                value = f'Perfil do(a) {conta.usuario}',
                                size = 24,
                                weight = 'bold',
                                color = "#FFFFFF", #roxo
                                text_align = 'center'
                            ),
                            ft.Image(
                                src = 'imgs/teste.png',
                                width=100,  
                                height=100,
                                fit=ft.ImageFit.CONTAIN, #Ajusta a img ao tamanho defi. mat. propor.
                            ),
                            ft.Text(
                                value=f"NOME: {conta.usuario}\nEMAIL: {conta.email}\nSALDO: {conta.saldo}\nCartão: {conta.cartao}",
                                color="#FFFFFF",
                                weight = 'bold',
                                size=16,
                                text_align="center"
                            )
                        ],
                        spacing=10,  # Espaçamento vertical entre os itens
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                    )
                )
            ],
            alignment=ft.alignment.center
        )
    )
    page.add(container_pessoa)
    page.update()
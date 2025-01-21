import flet as ft
from eldatabase.database import Account
from peewee import DoesNotExist
from defs.utilitarios import verificar_senha
def area_pix(page, conta):
    page.controls.clear()

    destino = ft.TextField(label='Destinatário do Pix(CPF):')
    pix = ft.TextField(label='Valor do Pix:')
    senha = ft.TextField(label='Sua senha:')
    confirmar_checkbox = ft.Checkbox(label="Confirmo que desejo efetuar esta transação", value=False)
    mensagem = ft.Text(value='')
    def enviar_pix(e):
        mensagem.color = 'red'
        valor_pix = float(pix.value)
        if not confirmar_checkbox.value:
            mensagem.value = 'Confirme a transação!'
        elif not destino.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not pix.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not senha.value:
            mensagem.value = 'Preencha todos os campos!'
        elif (valor_pix > conta.saldo):
            mensagem.value = 'Saldo insuficiente!'
        else:
            try:
                if verificar_senha(senha.value, conta.senha):
                    Usuario_destinatario = Account.get(Account.cpf == destino.value)
                    Usuario_destinatario.saldo += valor_pix
                    conta.saldo -= valor_pix
                    Usuario_destinatario.save()
                    conta.save()
                    mensagem.value = f'Foram tranferidos R${valor_pix} para {Usuario_destinatario.usuario}'
                    mensagem.color = 'green'
                else:
                    mensagem.value = 'Senha incorreta!'
            except DoesNotExist:
                mensagem.value = 'Usuário ou cpf incorretos!'
            except Exception as ex:
                mensagem.value = f'Erro ao cadastrar: {ex}'
                mensagem.color = 'red'
        page.update()
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
                                    value = 'Área PIX',
                                    size = 24,
                                    weight = 'bold',
                                    color = "#6C63FF", #roxo
                                    text_align = 'center'
                                ),
                                destino,
                                pix,
                                senha,
                                confirmar_checkbox,
                                mensagem,
                                ft.ElevatedButton(
                                    'Efetuar Pix',
                                    on_click = lambda e: enviar_pix(page)
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
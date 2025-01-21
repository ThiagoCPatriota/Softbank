import flet as ft
from peewee import DoesNotExist
from eldatabase.database import db, User, Account
from defs.utilitarios import *
from defs.menu import Menu_principal



db.connect()
db.create_tables([User, Account])


def Cadslog(page):
    page.controls.clear()

    container_principal = ft.Container(
        expand = True,
        content = ft.Stack(
            controls = [
                ft.Container(
                    ft.Image(
                        src = 'imgs/logincad_bg.jpg',
                        fit = ft.ImageFit.COVER
                    ),
                opacity = 0.2
                ),
                ft.Container(
                    width = 400,
                    height = 350,
                    bgcolor = ft.colors.with_opacity(0.5, '#000000'),
                    border_radius = 15,
                    padding = 20,
                    content = ft.Column(
                        controls = [

                            ft.Text(
                                value = 'Bem-vindo(a) ao \nSoftBank',
                                size = 24,
                                weight = 'bold',
                                color = "#6C63FF", #roxo
                                text_align = 'center'
                            ),
                            ft.CupertinoButton(
                                content = ft.Text(
                                    'Cadastrar',
                                    color = 'white',
                                ),
                                bgcolor = '#6C63FF', #roxo
                                on_click= lambda e: Cadastro(page)

                            ),
                            ft.CupertinoButton(
                                content = ft.Text(
                                    'Login',
                                    color = 'white'
                                ),
                                bgcolor = '#6C63FF', #roxo
                                on_click = lambda e: Login(page)
                            ),
                            ft.CupertinoButton(
                                content = ft.Text(
                                    'Sair',
                                    color = 'white'
                                ),
                                bgcolor = '#6C63FF', #roxo
                                on_click = lambda e: page.window_close()
                            ),   
                        ],
                        spacing=10,  # Espaçamento vertical entre os itens
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                    ),
                    
                ),
            ],
            alignment=ft.alignment.center,
        ),
    )
  
    page.add(container_principal)
    page.update()

###

def Cadastro(page):
    page.controls.clear()
    nome = ft.TextField(label='Digite seu nome:')
    email = ft.TextField(label='Digite seu email:')
    senha = ft.TextField(label='Digite sua senha:', password=True)
    cpf = ft.TextField(label='Digite seu cpf (apenas números):', max_length=11)
    cartao = ft.TextField(label='Digite o numero do seu cartão:', max_length=16)
    mensagem = ft.Text(value='')
    def Confirmar_Cadastro(e):
        mensagem.color='RED'
        if not nome.value:
            mensagem.value = 'Porfavor, Preencha um nome válido!'
        elif not email.value:
            mensagem.value = 'Porfavor, Preencha um email válido!'
        elif not senha.value:
            mensagem.value = 'Porfavor, Preencha uma senha válida!'
        elif not cpf.value:
            mensagem.value = 'Porfavor, Preencha um CPF válido!'
        elif not cartao.value:
            mensagem.value = 'Porfavor, Preencha um Cartão válido!'
        else:
            try:
                if validador_cpf(cpf.value) and validar_cartao(cartao.value):
                    usuario = User.create(nome=nome.value, email=email.value, senha=codificar_senha(senha.value), cpf=cpf.value)
                    Account.create(email=email.value, usuario=nome.value, saldo=0, cartao=cartao.value, senha=usuario.senha, cpf = cpf.value)
                    mensagem.value = 'Cadastro Realizado com Sucesso!'
                    mensagem.color = 'green'
                    Cadslog(page)
                    page.add(mensagem)
            except Exception as ex:
                mensagem.value = f'Erro ao cadastrar: {ex}'
                mensagem.color = 'red'
        page.update()
    container_cadastro = ft.Container(
        expand = True,
        content = ft.Stack(
            controls = [
                ft.Container(
                    ft.Image(
                        src = 'imgs/cadastro_bg.jpg',
                        fit = ft.ImageFit.COVER
                    ),
                    opacity = 0.2
                ),
                    ft.Container(
                        width = 400,
                        height = 500,
                        bgcolor = ft.colors.with_opacity(0.5, '#000000'),
                        border_radius = 15,
                        padding = 20,
                        content = ft.Column(
                            controls= [
                                ft.Text(
                                    value = 'Bem-Vindo ao Cadastro:',
                                    size = 24,
                                    weight = 'bold',
                                    color = "#6C63FF", #roxo
                                    text_align = 'center'
                                ),
                                nome,
                                email,
                                senha,
                                cpf,
                                cartao,
                                mensagem,
                                ft.Row(
                                    controls = [
                                        ft.ElevatedButton(
                                        'Cadastrar',
                                        on_click = lambda e: Confirmar_Cadastro(e)
                                        ),
                                        ft.ElevatedButton(
                                            'Voltar',
                                            on_click = lambda e: Cadslog(page)
                                        ),
                                    ]
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
    page.add(
        container_cadastro,
    )

def Login(page):
    page.controls.clear()

    email = ft.TextField(label='Digite seu email:')
    senha = ft.TextField(label='Digite sua senha:', password=True)
    cpf = ft.TextField(label='Digite seu cpf (apenas números):', max_length=11)
    mensagem = ft.Text(value='')
    def Confirma_login(e):
        mensagem.color='RED'
        if not email.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not senha.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not cpf.value:
            mensagem.value = 'Preencha todos os campos!'
        else:

            try: #tente
                usuario = User.get((User.email == email.value) & (User.cpf == cpf.value))
                if verificar_senha(senha.value, usuario.senha):
                    conta = Account.get(Account.email == email.value)
                    mensagem.value = 'Login Realizado com Sucesso!'
                    mensagem.color = 'green'
                    Menu_principal(page, conta)
                else:
                    mensagem.value = 'Senha incorreta!'
            except DoesNotExist:
                mensagem.value = 'Usuário ou cpf incorretos!'
            except Exception as ex:
                mensagem.value = f'Erro ao cadastrar: {ex}'

        page.update()

    container_login = ft.Container(
        expand = True,
        content = ft.Stack(
            controls=[
                ft.Container(
                    ft.Image(
                        src = 'imgs/login_bg.jpg',
                        fit = ft.ImageFit.COVER
                    ),
                    opacity = 0.2
                ),
                ft.Container(
                    width = 400,
                    height = 450,
                    bgcolor = ft.colors.with_opacity(0.5, '#000000'),
                    border_radius = 15,
                    padding = 20,
                    content = ft.Column(
                        controls= [
                            ft.Text(
                                value = 'Bem-Vindo ao Login:',
                                size = 24,
                                weight = 'bold',
                                color = "#6C63FF", #roxo
                                text_align = 'center'
                            ),
                            email,
                            cpf,
                            senha,
                            mensagem,
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        'Logar',
                                        on_click = lambda e: Confirma_login(e)
                                    ),
                                    ft.ElevatedButton(
                                        'Voltar',
                                        on_click = lambda e: Cadslog(page)  
                                    )
            
                                ]
                            ),
                            ft.TextButton(
                                'Esqueceu sua senha?',
                                on_click = lambda e: esq_senha(page)
                            ),
                        ],
                        spacing=10,  # Espaçamento vertical entre os itens
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )

            ],
            alignment=ft.alignment.center, 
        ),

    )
    page.update()

    page.add(
        container_login
    )


def esq_senha(page):
    page.controls.clear()


    cpf = ft.TextField(label='Digite seu cpf (apenas números):', max_length = 11)
    email = ft.TextField(label='Digite seu email:')
    nova_senha = ft.TextField(label='Digite sua nova senha:', password = True)
    conf_nova_senha = ft.TextField(label='Confirme a nova senha:', password = True)
    mensagem = ft.Text(value='')

    def confirmar_troca_senha(e):
        mensagem.color = 'RED'
        if not cpf.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not email.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not nova_senha.value:
            mensagem.value = 'Preencha todos os campos!'
        elif not conf_nova_senha.value:
            mensagem.value = 'Preencha todos os campos!'
        elif nova_senha.value != conf_nova_senha.value:
            mensagem.value = 'Senhas diferentes digitadas!'
        else:
            try:
                usuario = User.get((User.cpf == cpf.value) & (User.email == email.value))
                usuario.senha = codificar_senha(conf_nova_senha.value)
                usuario.save()
                Cadslog(page)  
            except DoesNotExist:
                mensagem.value = 'Usuário não encontrado'
        page.update()
    container_esq_senha = ft.Container(
        expand = True,
        content = ft.Stack(
            controls = [
                ft.Container(
                    ft.Image(
                        src = 'imgs/login_bg.jpg',
                        fit = ft.ImageFit.COVER
                    ),
                    opacity = 0.2
                ),
                ft.Container(
                    width = 400,
                    height = 450,
                    bgcolor = ft.colors.with_opacity(0.5, '#000000'),
                    border_radius = 15,
                    padding = 20,
                    content = ft.Column(
                        controls = [
                            ft.Text(
                                value = 'Redefinir senha',
                                size = 24,
                                weight = 'bold',
                                color = "#6C63FF", #roxo
                                text_align = 'center'
                            ),
                            cpf,
                            email,
                            nova_senha,
                            conf_nova_senha,
                            mensagem,
                            ft.Row(
                                controls = [
                                    ft.ElevatedButton(
                                        'Redefinir',
                                        on_click = lambda e: confirmar_troca_senha(page)
                                    ),
                                    ft.ElevatedButton(
                                        'Voltar',
                                        on_click = lambda e: Cadslog(page)
                                    ),
                                ],
                            ),

                        ],
                        spacing=10,  # Espaçamento vertical entre os itens
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),

                    
                ),
            ],
            alignment=ft.alignment.center, 
        )

    )

    page.add(
        container_esq_senha
    )
    page.update()
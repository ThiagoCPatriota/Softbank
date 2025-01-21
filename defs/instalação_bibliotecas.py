import os

def verificar_e_instalar(biblioteca):
    try:
        __import__(biblioteca)
        print(f'A biblioteca {biblioteca} já está instalada.')
    except ImportError:
        print(f'A biblioteca {biblioteca} não está instalada. Instalando agora...')
        os.system(f'pip install {biblioteca}')
        print(f'A instalação de {biblioteca} foi concluída.')

def instalacao_bibliotecas():
    bibliotecas = ['flet', 'peewee', 'requests', 'bcrypt']

    for biblioteca in bibliotecas:
        verificar_e_instalar(biblioteca)
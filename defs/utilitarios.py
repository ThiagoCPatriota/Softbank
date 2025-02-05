import requests
import bcrypt
import random
def validador_cpf(cpf):
    cpf_c = ''
    aux = 10
    result = 0
    for i in range(9):
        cpf_c += cpf[i]
    for i in range(9):
        result += int(cpf_c[i]) * aux
        aux -= 1
    result = (result*10)%11
    result = result if result < 10 else 0
    cpf_c += str(result)

    result = 0
    aux = 11
    for i in range(10):
        result += int(cpf_c[i]) * aux
        aux -= 1
    result = (result*10)%11
    result = result if result < 10 else 0
    cpf_c += str(result)
    if cpf_c == cpf:
        return True
    return False

#CPF VALIDO PARA TESTES:    64042544096
#Cartao para testes:        4532015112830366
def obter_cotacao_bitcoin():
    url = "https://economia.awesomeapi.com.br/last/BTC-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao_dolar = dados['BTCBRL']['bid']

        return cotacao_dolar
    else:

        return "Erro ao obter a cotação"

import random
def criar_cartao():
    while True:
        cartao = [random.randint(1, 9) for i in range(16)]
        num_cartao = ''
        for i in cartao:
            num_cartao += str(i)
        soma = 0
        tamanho = len(cartao)
        for i in range(tamanho):
            digito = cartao[-(i + 1)]
            if i % 2 == 1: 
                digito *= 2
                if digito > 9: 
                    digito -= 9
            soma += digito
        if soma%10 ==0:
            return num_cartao
        else:
            continue

def codificar_senha(senha):
    # Converter a senha para bytes
    senha_bytes = senha.encode("utf-8")
    # Gerar o salt e criar o hash
    hash_senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
    return hash_senha.decode("utf-8")

# Verificar a senha
def verificar_senha(senha, hash_senha):
    # Converter a senha para bytes
    senha_bytes = senha.encode("utf-8")
    hash_senha_bytes = hash_senha.encode("utf-8")

    # Comparar a senha fornecida com o hash armazenado
    return bcrypt.checkpw(senha_bytes, hash_senha_bytes)

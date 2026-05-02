import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    resposta = resposta.json()
    return resposta

if __name__ == '__main__':
    cep_digitado = int(input("Digite o CEP (somente números): "))
    dados_cep = buscar_endereco(cep_digitado)
    print(dados_cep['logradouro'], dados_cep['localidade'])

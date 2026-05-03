import requests

def buscar_endereco(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)

        resposta = resposta.json()
        return resposta
    except:
        print("Erro: Não foi possível conectar ao viacep.")

if __name__ == '__main__':
    cep_digitado = (input("Digite o CEP (somente números): "))
    dados_cep = buscar_endereco(cep_digitado)
    if dados_cep:
        if 'erro' in dados_cep:
            print("CEP não encontrado")
        else:
            print(dados_cep['logradouro'])
            print(dados_cep['localidade'])
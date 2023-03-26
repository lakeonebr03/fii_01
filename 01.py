import requests
from bs4 import BeautifulSoup
import os

lista = ['mxrf11','vgia11','kisu11','vghf11','mcci11','rzag11','game11','aazq11']

try:
    for i in lista:
        url = f"https://www.fundsexplorer.com.br/funds/{i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        vlr = soup.find("span", {"class": "price"}).text.strip()
        titulo = soup.find_all("span", {"class": "indicator-title"})
        valor = soup.find_all("span", {"class": "indicator-value"})
        nome = soup.find("h1", {"class": "section-title"}).text
        
        nome_ = f'Nome: {nome}'
        valor_cota = f'Valor da Cota: {vlr}'
        div = f'{titulo[1].text.strip()} {valor[1].text.strip()}'
        yd = f'{titulo[2].text.strip()} {valor[2].text.strip()}'
        pvp = f'{titulo[6].text.strip()} {valor[6].text.strip()}'

        ###############
        token = os.getenv('TOKEN_01')
        chat_id = os.getenv('TOKEN_02')
        msg = (f'{nome}\n{valor_cota}\n{div}\n{yd}\n{pvp}')
        url_tel = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")
        respost = requests.get(url_tel)
        ###############
        
except:
    ###############
    token = os.getenv('TOKEN_01')
    chat_id = os.getenv('TOKEN_02')
    msg = ('Código com problemas !')
    url_tel = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")
    respost = requests.get(url_tel)
    ###############

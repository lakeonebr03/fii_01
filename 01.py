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
        liq = f'{titulo[0].text.strip()} {valor[0].text.strip()} negociações'
        div = f'{titulo[1].text.strip()} {valor[1].text.strip()}'
        yd = f'{titulo[2].text.strip()} {valor[2].text.strip()}'
        patr_liq = f'{titulo[3].text.strip()} {valor[3].text.strip()}'
        vlr_pat = f'{titulo[4].text.strip()} {valor[4].text.strip()}'
        rent_mes = f'{titulo[5].text.strip()} {valor[5].text.strip()}'
        pvp = f'{titulo[6].text.strip()} {valor[6].text.strip()}'

        ###############
        token = os.getenv('TOKEN_01')
        chat_id = os.getenv('TOKEN_02')
        msg = (f'{nome}\n{valor_cota}\n{liq}\n{div}\n{yd}\n{patr_liq}\n{vlr_pat}\n{rent_mes}\n{pvp}')
        url_tel = ("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+msg)
        respost = requests.get(url_tel)
        ###############
        
except:
    ###############
    token = os.getenv('TOKEN_01')
    chat_id = os.getenv('TOKEN_02')
    msg = ('Código com problemas !')
    url_tel = ("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+msg)
    respost = requests.get(url_tel)
    ###############
    
    ###############
    token = '6128272966:AAG_ifgQKabRLjqafqkJV0xWHMx7qaD2Qs4' #os.getenv('TOKEN_01')
    chat_id = '-634202755' #os.getenv('TOKEN_02')
    msg = (f'{nome}\n{valor_cota}\n{liq}\n{div}\n{yd}\n{patr_liq}\n{vlr_pat}\n{rent_mes}\n{pvp}')
    url_tel = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg})
    respost = requests.get(url_tel)
    ###############

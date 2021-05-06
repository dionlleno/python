import requests
from bs4 import BeautifulSoup


def moldura(text):
    text = text[9:]
    lar = len(text)
    alt = 5
    print('#' * (lar + 4))
    print('#', ' ' * lar, '#')
    print('#', text, '#')
    print('#', ' ' * lar, '#')
    print('#' * (lar + 4))


host = 'https://www.meuip.com.br/'
ip = BeautifulSoup(requests.get(host).text, 'lxml').h3.text
moldura(ip)

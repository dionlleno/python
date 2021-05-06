import requests,lxml
from bs4 import BeautifulSoup

host = 'https://df.olx.com.br/?q='
params = {'q': input("Pesquisar: ")}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(host+params['q'],headers=headers)
soup = BeautifulSoup(page.text, 'lxml')
print(soup.find_all('div',class_="fnmrjs-6 iNpuEh")[0])
print(soup.find_all('div',class_="fnmrjs-6 iNpuEh")[1])
print(soup.find_all('div',class_="fnmrjs-6 iNpuEh")[2])
#print(soup.find_all('li',class_="sc-1fcmfeb-2 OgCqv"))

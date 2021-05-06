from urllib.error import HTTPError
from urllib.error import URLError
import requests, lxml
from bs4 import BeautifulSoup

try:
    host = 'https://df.olx.com.br/?q='
    params = {'q': input("Pesquisar: ")}
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    page = requests.get(host + params['q'], headers=headers)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
  res = BeautifulSoup(page.text, "lxml")
  link = res.findAll('a',{'class':'fnmrjs-0 fyjObc'})
  price = res.findAll('span',{"color":"graphite"})
  title = res.findAll('h2',{'color':"dark"})
  location = res.findAll('div',{'class':'sc-7l84qu-0 gmtqTp'})
  #phone = res.findAll('span',{"color":"graphite"})
  i = 0
  while True:
    print(price[0].getText(),title[0].getText(),location[0].getText(),link.getText())
    i += 1

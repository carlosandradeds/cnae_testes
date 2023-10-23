from bs4 import BeautifulSoup
import requests

url = 'https://dados.rfb.gov.br/CNPJ/'

def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parseia o conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todos os links na página
        links = soup.find_all('a')
        #print(links)

        estabelecimentos = []
        cnaes = []

        for link in links:
            if link.get('href').startswith('Estabelecimentos'):
                estabelecimentos.append(link.text)

            if link.get('href').startswith('Cnaes'):
                cnaes.append(link.text)
        
        return estabelecimentos, cnaes

estabelecimentos, cnaes  = get_url(url)

print(estabelecimentos)
print(cnaes)
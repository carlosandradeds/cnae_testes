import requests

from tqdm import tqdm
from bs4  import BeautifulSoup

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

def get_estabelecimento():
    for estabelecimento in estabelecimentos:
        url = url + f'{estabelecimento}'
        print(url)

        # Realize a solicitação GET para baixar o arquivo
        response = requests.get(url, stream=True)

        # Verifique se a solicitação foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Especifique o caminho onde você deseja salvar o arquivo
            nome_do_arquivo = f'{estabelecimento}'

            # Obtenha o tamanho total do arquivo em bytes
            total_size = int(response.headers.get('content-length', 0))

            # Crie uma barra de progresso usando o tqdm
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

            # Abra um arquivo local para escrever o conteúdo do arquivo
            with open(nome_do_arquivo, 'wb') as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    progress_bar.update(len(data))  # Atualize a barra de progresso

            progress_bar.close()  # Feche a barra de progresso

            return print(f'O arquivo foi baixado com sucesso como {nome_do_arquivo}')
        else:
            return print('A solicitação falhou. Status code:', response.status_code)
        
def get_cnaes():
    url = 'https://dados.rfb.gov.br/CNPJ/'
    for cnae in cnaes:
        url = url + f'{cnae}'
        print(url)

        # Realize a solicitação GET para baixar o arquivo
        response = requests.get(url, stream=True)

        # Verifique se a solicitação foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Especifique o caminho onde você deseja salvar o arquivo
            nome_do_arquivo = f'{cnae}'

            # Obtenha o tamanho total do arquivo em bytes
            total_size = int(response.headers.get('content-length', 0))

            # Crie uma barra de progresso usando o tqdm
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

            # Abra um arquivo local para escrever o conteúdo do arquivo
            with open(nome_do_arquivo, 'wb') as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    progress_bar.update(len(data))  # Atualize a barra de progresso

            progress_bar.close()  # Feche a barra de progresso

            return print(f'O arquivo foi baixado com sucesso como {nome_do_arquivo}')
        else:
            return print('A solicitação falhou. Status code:', response.status_code)


get_cnaes()

#get_estabelecimento()
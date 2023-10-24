import requests
import re

def get_cnpj():
    url = 'http://127.0.0.1:8080/conhecimentos_de_frete/'

    params = {"numero_conhecimento": "CF12345"}

    response = requests.get(url, json=params)

    response_json = response.json()

    n_notas = len(response_json["notas_fiscais"])

    cnpjs_emitente = []
    for i in range(n_notas):
        cnpjs_emitente.append(response_json["notas_fiscais"][i]["cnpj_emitente"])


    return cnpjs_emitente


def get_ncm():
    url = 'http://127.0.0.1:8080/conhecimentos_de_frete/'

    params = {"numero_conhecimento": "CF12345"}

    response = requests.get(url, json=params)

    response_json = response.json()

    n_notas = len(response_json["notas_fiscais"])

    ncm_produtos = []
    for i in range(n_notas):
        for item in response_json["notas_fiscais"][i]["itens"]:
            if "ncm" in item:
                ncm_produtos.append(item["ncm"])


    return ncm_produtos


cnpjs = get_cnpj()
ncms = get_ncm()

def estabelecimento_cnae():
    for i in cnpjs:
        url = 'http://127.0.0.1:8000/search_establishment/'

        i = re.sub("[^0-9]", "", i)
        i = str(i)


        params_ = {"cnpj": i}
        #print(params_)

        response = requests.post(url, json=params_)

        try:
            if response.status_code == 200:
                response_json = response.json()
                return print(response_json)

        except Exception as e:
            return print("CNPJ não encontrado")

estabelecimento_cnae()




def check_ncm():
    for i in ncms:
        url = 'http://127.0.0.1:8000/get_cnaes/'

        i = re.sub("[^0-9]", "", i)
        i = str(i)


        params_ = {"ncm": i}
        print(params_)

        response = requests.post(url, json=params_)

        try:
            if response.status_code == 200:
                response_json = response.json()
                return print(response_json)

        except Exception as e:
            return print("NCM não encontrado")
        
check_ncm()
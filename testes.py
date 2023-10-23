import zipfile
import pandas as pd
from os import listdir, getcwd
from os.path import exists




def estabelecimento():
    diretorio = getcwd()
    for arquivo in listdir(diretorio):

        zip = zipfile.ZipFile(arquivo)

        for filename in zip.namelist():
            if exists(filename == False):
                f = zip.extract(filename)
            
                print("PRE LEITURA")    

            chunksize = 1024*100

            #pjs = pd.DataFrame()
            for  chunk in pd.read_csv(filename, sep= ';', header=None, encoding='latin1', chunksize=chunksize):
                chunk.columns = ["CNPJ_BASICO",
                        "CNPJ_ORDEM",
                        "CNPJ_DV",
                        "MATRIZ_FILIAL",
                        "NOME_FANTASIA",
                        "SITUACAO_CADASTRAL",
                        "DATA_SITUACAO_CADASTRAL",
                        "MOTIVO_SITUACAO_CADASTRAL",
                        "NOME_CIDADE_EXTERIOR",
                        "CODIGO_PAIS",
                        "DATA_INICIO",
                        "CNAE_PRINCIPAL",
                        "CNAE_SECUNDARIA",
                        "TIPO_LOGRADOURO",
                        "LOGRADOURO",
                        "NÚMERO",
                        "COMPLEMENTO",
                        "BAIRRO",
                        "CEP",
                        "UF",
                        "MUNICIPIO",
                        "DDD_1",
                        "TELEFONE_1",
                        "DDD_2",
                        "TELEFONE_2",
                        "DDD_FAX",
                        "FAX",
                        "CORREIO_ELETRONICO",
                        "SITUACAO_ESPECIAL",
                        "DATA_SITUACAO_ESPECIAL"]

                print(chunk['CNAE_SECUNDARIA'])

estabelecimento()
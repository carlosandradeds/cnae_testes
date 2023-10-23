import zipfile
import csv
import numpy as np
import pandas as pd
from os.path import exists
from datetime import datetime
import redis
import re

def getCnaes():
    cnaes = pd.read_csv("F.K03200$Z.D30812.CNAECSV", sep= ';', header=None, encoding='ANSI')
    cnaes.columns = ["CNAE", "DESC"]
    return cnaes

def relCnaesNcms():
    cnaeNcm = pd.read_excel("NCM2012XCNAE20.xls", header=0, converters={'NCM':str,'DESC':str,'CNAE':str})
    #print( cnaeNcm.head(50))
    cnaeNcm['CNAE'] = cnaeNcm['CNAE'].str.split('; ')
    cnaeNcm = cnaeNcm.explode('CNAE').reset_index(drop=True)
    cols = list(cnaeNcm.columns)
    cols.append(cols.pop(cols.index('CNAE')))
    cnaeNcm = cnaeNcm[cols]

    #print( cnaeNcm.loc[cnaeNcm.NCM == '1022990'])
    cnaeNcm = cnaeNcm.groupby('NCM').CNAE.apply(list).reset_index()

    #print( cnaeNcm.loc[cnaeNcm.NCM == '1022990'])

    #start_time = datetime.now()
    #print( cnaeNcm.loc[cnaeNcm.NCM == '1062000'])
    #print( cnaeNcm.head(50) )
    #end_time = datetime.now()
    #print('Duration: {}'.format(end_time - start_time))


    return cnaeNcm


def acessRedis():
    r = redis.Redis(
    host='redis-12795.c246.us-east-1-4.ec2.cloud.redislabs.com',
    port=12795,
    password='zYtFia5AjDAq0O38oPT9fLb0EkPcjzc19')

    #pipe = r.pipeline()
    #for i in range(len(cnaeNcm['NCM'])):
    #    pipe.set(cnaeNcm['NCM'][i], cnaeNcm['CNAE'][i])
    #results = pipe.execute()

def searchCnaeByNcm( searchncm ):
    cnaeNcm = relCnaesNcms()
    canes = getCnaes()
    canes['CNAE'] = canes['CNAE'].map(lambda x: str(x)[:-2])
    print( canes )

    ncms = cnaeNcm.loc[cnaeNcm.NCM == searchncm]
    print( ncms )
    for idx, ncm in ncms.iterrows():
        print( ncm )
        for cnae in ncm['CNAE']:
            cnae = re.sub("[^0-9]", "", cnae)
            print(cnae)
            cnae = cnae[1:] if cnae.startswith('0') else cnae
            cnaesDesc = canes.loc[canes.CNAE == cnae]
            print(cnaesDesc)

    #print( canes )



def estabelecimento():

    zip = zipfile.ZipFile('Estabelecimentos9.zip')

    for filename in zip.namelist():
        if exists(filename == False):
            f = zip.extract(filename)
        
            print("PRE LEITURA")    

        chunksize = 1024*100

        pjs = pd.DataFrame()
        for  
        pd.read_csv(filename, sep= ';', header=None, encoding='ANSI', chunksize=chunksize):

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






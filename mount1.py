import pandas as pd
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
chunksize = 1024*100

class NcmQuery(BaseModel):
    ncm: str

class CnpjSearch(BaseModel):
    cnpj: str

def getCnaes():
    cnaes = pd.read_csv("/home/carlos/projetos/cnae_testes/F.K03200$Z.D31014.CNAECSV", sep= ';', header=None, encoding='latin1')
    cnaes.columns = ["CNAE", "DESC"]
    return cnaes


def relCnaesNcms():
    cnaeNcm = pd.read_excel("/home/carlos/projetos/cnae_testes/NCM2012XCNAE20.xls", header=0, converters={'NCM':str,'DESC':str,'CNAE':str})
    #print( cnaeNcm.head(50))
    cnaeNcm['CNAE'] = cnaeNcm['CNAE'].str.split('; ')
    #print(cnaeNcm)
    
    cnaeNcm = cnaeNcm.explode('CNAE').reset_index(drop=True)
    #print(cnaeNcm.head(50))
    cols = list(cnaeNcm.columns)
    cols.append(cols.pop(cols.index('CNAE')))
    #print(cols)
    cnaeNcm = cnaeNcm[cols]
    cnaeNcm = cnaeNcm.groupby('NCM').CNAE.apply(list).reset_index()
    #print(cnaeNcm)

    return cnaeNcm


def searchCnaeByNcm( searchncm ):
    cnaeNcm = relCnaesNcms()
    canes = getCnaes()
    canes['CNAE'] = canes['CNAE'].map(lambda x: str(x)[:-2])
    #print( canes )

    ncms = cnaeNcm.loc[cnaeNcm.NCM == searchncm]
    #print( ncms )
    for idx, ncm in ncms.iterrows():
        print( ncm )
        for cnae in ncm['CNAE']:
            cnae = re.sub("[^0-9]", "", cnae)
            print(cnae)
            cnae = cnae[1:] if cnae.startswith('0') else cnae
            cnaesDesc = canes.loc[canes.CNAE == cnae]
            #print(cnaesDesc)

            return cnaesDesc
        

@app.post("/search_establishment/")
async def estabelecimento(cnpj: CnpjSearch):
    cnae_principal = []
    cnae_secundario = []
    for  chunk in pd.read_csv('/home/carlos/projetos/cnae_testes/K3241.K03200Y0.D31014.ESTABELE', sep= ';', header=None, encoding='latin1', chunksize=chunksize, dtype = str):
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
        
        # Check for the CNPJ match within the chunk
        cnpj_match = chunk[
            (chunk['CNPJ_BASICO'] == cnpj.cnpj[:8]) &
            (chunk['CNPJ_ORDEM'] == cnpj.cnpj[8:12]) &
            (chunk['CNPJ_DV'] == cnpj.cnpj[12:14])
        ]
        
        if not cnpj_match.empty:
            cnae_principal = cnpj_match.iloc[0]['CNAE_PRINCIPAL']  # Coluna 'CNAE_PRINCIPAL'
            print(f'O CNAE principal da empresa é : {str(cnae_principal)}')  # Coluna 'CNAE_PRINCIPAL'
            cnae_secundario = cnpj_match.iloc[0]['CNAE_SECUNDARIA']
            print(f'O CNAE secundario da empresa é : {str(cnae_secundario)}')
            break


    return {"CNAEs_Principais": [cnae_principal], "CNAEs_Secundarios": [cnae_secundario]}


@app.post("/get_cnaes/")
async def get_cnaes(ncm_query: NcmQuery):
    cnae_list = searchCnaeByNcm(ncm_query.ncm)
    if not cnae_list.empty:
        return {"CNAEs": cnae_list.to_dict(orient='records')}
    else:
        raise HTTPException(status_code=404, detail="No matching CNAEs found.")
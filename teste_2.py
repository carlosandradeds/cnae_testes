import pandas as pd

chunksize = 1024*100

def estabelecimento(cnpj):
    for  chunk in pd.read_csv('K3241.K03200Y0.D31014.ESTABELE', sep= ';', header=None, encoding='latin1', chunksize=chunksize, dtype = str):
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
            (chunk['CNPJ_BASICO'] == cnpj[:8]) &
            (chunk['CNPJ_ORDEM'] == cnpj[8:12]) &
            (chunk['CNPJ_DV'] == cnpj[12:14])
        ]
        
        if not cnpj_match.empty:
            cnae_principal = cnpj_match.iloc[0]['CNAE_PRINCIPAL']  # Coluna 'CNAE_PRINCIPAL'
            print(f'O CNAE principal da empresa é : {str(cnae_principal)}')  # Coluna 'CNAE_PRINCIPAL'
            cnae_secundario = cnpj_match.iloc[0]['CNAE_SECUNDARIA']
            print(f'O CNAE secundario da empresa é : {str(cnae_secundario)}')
            break

    return cnae_principal, cnae_secundario



estabelecimento('07047183000140')
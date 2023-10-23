import pandas as pd
import re
#from fastapi import FastAPI, HTTPException

#app = FastAPI()

def getCnaes():
    cnaes = pd.read_csv("F.K03200$Z.D30812.CNAECSV", sep= ';', header=None, encoding='latin1')
    cnaes.columns = ["CNAE", "DESC"]
    return cnaes


def relCnaesNcms():
    cnaeNcm = pd.read_excel("NCM2012XCNAE20.xls", header=0, converters={'NCM':str,'DESC':str,'CNAE':str})
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


cnae_list = searchCnaeByNcm("1012100")

print(cnae_list)
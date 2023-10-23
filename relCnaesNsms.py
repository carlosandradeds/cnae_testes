import pandas as pd

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
    print(cnaeNcm)

    

relCnaesNcms()
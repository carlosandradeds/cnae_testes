
import pandas as pd

def getCnaes():
    cnaes = pd.read_csv("F.K03200$Z.D30812.CNAECSV", sep= ';', header=None, encoding='latin1')
    cnaes.columns = ["CNAE", "DESC"]
    return cnaes

cnaes = getCnaes()
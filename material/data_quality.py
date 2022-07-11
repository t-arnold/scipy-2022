import pandas as pd

def no_nas(product):
    df = pd.read_parquet(product['df'])
    
    raise ValueError('Things are broken here')
    assert not df.MedHouseVal.isna().sum()
import numpy as np
import pandas as pd
import seaborn as sns

def prepare(df=None, transform=False, encode=False):
    """Prepares diamonds data
    
    Parameters:
    df (pandas.DataFrame): Data structure as seaborn.load_dataset("diamonds")
                           If None, the diamonds data is loaded from seaborn.
    transform: Should diamonds data be prepared for descriptive analysis?
    encode: Should categorical variables be integer coded for modelling?

    Returns:
    pandas.DataFrame: Prepared diamonds data.
    
    """
    
    if df is None:
        df = sns.load_dataset("diamonds")
    
    if transform:
    #  -> handling of categories looks too verbose but allows (A) for safe preparation of a single line
    #     and (B) for the right ordering of levels.
        df = df.assign(depth=df.depth.clip(55, 70),
                       table=df.table.clip(50, 70),
                       carat=df.carat.clip(upper=3),
                       color=pd.Categorical(df.color, categories=['D', 'E', 'F', 'G', 'H', 'I', 'J']),
                       cut=pd.Categorical(df.cut, categories=['Ideal', 'Premium', 'Very Good', 'Good', 'Fair']),
                       clarity=pd.Categorical(df.clarity, categories=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']))
        df = df.drop(list("xyz"), axis=1)

    if encode:
    # Safe way to do integer coding with Pandas
        df = df.copy()
        cats = df.select_dtypes("category").columns
        df[cats] = df[cats].apply(lambda x: x.cat.codes)
    
    return df
    
import pandas as pd
import numpy as np

def label_encode(df,column):
    """
    Label encodes the column passed 
    
    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    column : string, int
        The column selected should be present in the Dataframe passed
    Returns
    -------
    numpy array
    
    """
    label_map = {}
    labels = [x for x in range(0, len(df[column].unique()))]

    for i , j in zip(df[column].unique(),labels):
        label_map[i] = j

    return(np.array(df[column].map(label_map)))
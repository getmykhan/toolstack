import pandas as pd
import numpy as np

def label_encode(df,column):
    """
    Label encodes the column passed 
    
    Parameters
    ----------
    df : DataFrame
        The df to perform label encoding operation on.
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


def count_encode(df,column, log=False):
    """
    Encodes the data based on the count 
    
    Parameters
    ----------
    df : DataFrame
        The df to perform count encoding operation on.
    column : string, int
        The column selected should be present in the Dataframe passed
    log : boolean, default False
        Options: True, False
    Returns
    -------
    numpy array
    """
    count_map = {}
    
    if log == True:
        for i , j in zip(df[column].value_counts().index, df[column].value_counts()):
            count_map[i] = np.log(j)

        return(np.array(df[column].map(count_map)))
    
    else:
        for i, j in zip(df[column].value_counts().index, df[column].value_counts()):
            count_map[i] = j

        return(np.array(df[column].map(count_map)))
            
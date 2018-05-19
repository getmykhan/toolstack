import pandas as pd
import numpy as np

def dataset_names():
    """
    List of available datasets 
    """
    return([
        'Salary',
        'Weather'
    ])

def dataset(data):
    """
    Change the case from upper to lower and vice versa

    Parameters
    ----------
    data : Dataset Name
        The list of datasets can be found calling the util.dataset_names()
    Returns
    -------
    DataFrame

    """
    return(pd.read_csv('https://raw.githubusercontent.com/getmykhan/toolstack/master/Datasets/'+ data +'.csv'))
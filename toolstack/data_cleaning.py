import pandas as pd
import numpy as np

def remove_outliers(df, column, strategy = 'IQR'):
    
    """ 
    Removes outliers from a numerical columns in a dataframe
    
    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    column : float
        The column selected should be present in the Dataframe passed
    strategy : string, default 'IQR'
        Options: 'standard_deviation', 'IQR'

    
    Returns
    -------
    List
    
    """
    
    values = np.array(df[column])
    
    if filter_type == 'standard_deviation':
        col_mean, col_std = values.mean(), values.std()
        limit = col_std * 3
        
        lower, upper = col_mean - limit, col_mean + limit
        
        i=0
        outliers_removed = []
        for value in values:
            if value >= lower and value <= upper:
                outliers_removed.append(value)
                #indexes.append(i)
                i = i+1
                
    if filter_type == 'IQR':
        Quar25, Quar75 = np.percentile(values, 25), np.percentile(values, 75)
        IQR = Quar75 - Quar25
        limit = IQR * 1.5
        
        lower, upper = Quar25 - limit, Quar75 + limit
        
        i=0
        outliers_removed = []
        for value in values:
            if value >= lower and value <= upper:
                outliers_removed.append(value)
                #indexes.append(i)
                i = i+1
    
    return outliers_removed
import pandas as pd


def available_datasets():
    """
    List of available datasets
    """
    return([
        'Salary',
        'Weather'
    ])


def load_dataset(data):
    """
    Change the case from upper to lower and vice versa
    Parameters
    ----------
    data : Dataset Name
        The list of datasets can be found calling the utils.dataset_names()
    Returns
    -------
    DataFrame
    """
    return(pd.read_csv('https://raw.githubusercontent.com/getmykhan/toolstack/master/Datasets/'+ data +'.csv'))


def load_stopwords():
    """

    :return:
    """

    return set(pd.read_csv('https://algs4.cs.princeton.edu/35applications/stopwords.txt', header=-1)[0].values.tolist())

import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import re
from collections import Counter

def text_case(df, column, case='lower'):
    """
    Change the case from upper to lower and vice versa

    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    column : string, int
        The column selected should be present in the Dataframe passed
    case : string, default 'lower'
        Options: 'lower' , 'upper'
    Returns
    -------
    List
    
    """
    if case.lower() == 'lower':
        return [x.lower() for x in df[column]]
    elif case.lower() == 'upper':
        return [x.upper() for x in df[column]]

def stopword_remove(df, column, lang='english', text_lower=True):
    """ 
    Remove stopwords from a corpus

    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    column : string, int
        The column selected should be present in the Dataframe passed
    lang : string, default 'english'
        Options: Languages
    text_lower : boolean, default True
        If False, then the stopwords will be removed without lowercasing the text
    
    Returns
    -------
    List
    
    """
    word_list = []
    if text_lower == True:
        for x in np.array(df[column]):
            x = x.split()
            text = ' '.join([s.lower() for s in x if s.lower() not in set(stopwords.words('english'))])
            word_list.append(text)
        return word_list
               
    elif text_lower == False:
        for x in np.array(df[column]):
            x = x.split()
            text = ' '.join([s for s in x if s.lower() not in set(stopwords.words('english'))])
            word_list.append(text)
        return word_list
        
def punctuations(df, old_column , new_column, regex= r'[^\w\s]'):
    """ 
    Clean text, remove puncutations and symbols
    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    old_column : string, int
        The column on which the operation has to be performed
    new_column : string, int
        The new column to be generated after the operation is performed
    regex : string, default r'[^\w\s]'
        Pass any regex to clean the text (punctuations) else leave default

    """
    df[new_column] = df[old_column].apply(lambda x: re.sub(regex,'',x))


def count_word(df, column, sort='ascending', sw=None, lang='english'):
    """ 
    Take the count of unique words

    Parameters
    ----------
    df : DataFrame
        The df to perform case operation on.
    column : string, int
        The column selected should be present in the Dataframe passed
    sort : string, default ascending
        Options: ascending, descending
        If sorted, it will sort values by the count
    stopwords : boolean, default None
        Options: True, False
        To remove the common stopwords
    lang : string, default 'english'
        Options: Languages 
    
    Returns
    -------
    Dataframe: columns:['Word', 'Count']

    """
    if sw == True:
        word_counter = []
        for x in np.array(df[column]):
            x = x.split()
            for word in x:
                if word.lower() not in set(stopwords.words(lang)):
                    word_counter.append(word.lower())
        k_v = Counter(word_counter)
    
    else:
        word_counter = []
        for x in np.array(df[column]):
            x = x.split()
            for word in x:
                word_counter.append(word.lower())
        k_v = Counter(word_counter)
    
    if sort == 'ascending':
        return(pd.DataFrame({'Word':[x for x in k_v.keys()], 'Count': [x for x in k_v.values()]})).sort_values('Count')
    elif sort == 'descending':
        return(pd.DataFrame({'Word':[x for x in k_v.keys()], 'Count': [x for x in k_v.values()]})).sort_values('Count', ascending = False)
    else:
        return(pd.DataFrame({'Word':[x for x in k_v.keys()], 'Count': [x for x in k_v.values()]}))
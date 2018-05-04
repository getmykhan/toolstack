from packages import *

class text_preprocessing:
        
    def __init__(self):
        pass
    
    def text_case(self, df, column, case='lower'):
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
    
    def stopword_remove(self, df, column, lang='english', text_lower=True):
        """ 
        Remove stopwords from a corpus

        Parameters
        ----------
        df : DataFrame
            The df to perform case operation on.
        column : string, int
            The column selected should be present in the Dataframe passed
        lang : string, default 'english'
            Options: Lnaguages
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
            
    def punctuations(self, df, old_column , new_column, regex= r'[^\w\s]'):
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

    def count_word(self,df, column, sort= None):
        """ 
        Take the count of unique words

        Parameters
        ----------
        df : DataFrame
            The df to perform case operation on.
        column : string, int
            The column selected should be present in the Dataframe passed
        sort : boolean, default None
            Options: True, False
            If sorted, it will sort values by the count
        
        Returns
        -------
        Dataframe: columns:['Word', 'Count']

        """
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
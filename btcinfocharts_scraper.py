def current_date():
    """
        Returns the current date
        in a string format 'yyyy/mm/dd'
    """
    
    
    from datetime import date
    
    # get the current date
    today = date.today()
    return str(today).replace('-', '/')
    




def feats_to_url():
    """
        Takes a list of string features
        and converts to a list of the urls
    """
    
    # the list of features to scrape
    features = ['median_transaction_fee3momUSD',
                'fee_to_reward7momUSD',
                'top100cap30trx',
                'mining_profitability7rsi',
                'top100cap14mom',
                'price3wmaUSD',
                'price30smaUSD',
                'price30emaUSD',
                'hashrate30sma',
                'difficulty30sma',
                'price3rsiUSD',
                'confirmationtime7std']
    
    import re
    
    url_list = []
    
    for feat in features:
   
        regex = re.compile(r'(top100cap|[a-z_]+)(\d+\w+)')
        re_result = regex.search(feat)
        
        feat = re_result.group(1)
        trans = re_result.group(2)
    
        url='https://bitinfocharts.com/comparison/'+feat+'-'+'btc'+'-'+trans+'.html'
        url_list.append(url)
        
 
    return url_list, features
    
    
    
def create_dfs(url_list, features):
    """
        Returns a dataframe of the urls
        And a dataframe of the feature names
    
    """

    import pandas as pd
    
    df_features=pd.DataFrame(features,columns=['Features']) # convert feature list to dataframe
    df_url=pd.DataFrame(url_list,columns=['URL']) # convert url list to dataframe
    
    assert len(df_features) == len(df_url)
    
    return df_url, df_features
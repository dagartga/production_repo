def today():
    """
        Returns the current date
        in a string format 'yyyy/mm/dd'
    """
    
    
    from datetime import date
    
    # get the current date
    today = date.today()
    return str(today).replace('-', '/')
    
    
    
def yesterday():
    """ 
        Returns the date for yesterday
        in a string format 'yyyy/mm/dd
        For when current data is not available
    """
    
    from datetime import date, timedelta
    
    # get the current date
    today = date.today()
    #subtract one day
    yesterday = today - timedelta(days=1)
    
    return str(yesterday).replace('-', '/')




def feats_to_url():
    """
        Takes a list of string features
        and converts to a list of the urls
    """
    
    # the list of features to scrape
    features = [
                'median_transaction_fee3momUSD',
                'fee_to_reward7momUSD',
                'top100cap7mom',
                'mining_profitability7rsi',
                'top100cap14mom',
                'price3wmaUSD',
                'transactionvalue90emaUSD',
                'difficulty30sma',
                'fee_to_reward90smaUSD'
                ]
    
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
    


def scrape_url(url, feature):
    """
        Takes url and a feature name as input
        Scrapes the bitinfocharts.org site to return
        The feature value for today and yesterday
        
        Ouptut is dictionary format:
                    {
                    today_date: 
                            {feature : feature_value},
                    yesterdays_date:
                             {feature : feature_value}
                    }
        
    """
    
    from bs4 import BeautifulSoup #module for web scraping install by pip install beautifulsoup4
    import requests #for requesting html. install by pip install requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    import re #regular expression for data extraction by pattern matching. installed by default.
    
    session = requests.Session()
    retry = Retry(connect=10, backoff_factor=3)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    page=session.get(url)
    #print('Retrieving data from', url)
    
    #create the beautiful soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    # extract the portion with dates and values
    all_soup = soup.find_all('script')[4]
    # convert the data into string format
    soup_string = str(all_soup.string)
    
    # assign current date
    tday = today()
    
    # create a regular expression for extracting the value associated with the date
    regex = tday + '\"\),([0-9\.]+)'
    soup_regex = re.compile(regex)
    # call that regular expression on the html string
    regex_result = soup_regex.search(soup_string)
    
    # create a conditional statement for when current date's data has not been posted
    if regex_result is None:
        today_feat_val = None
    else:
        today_feat_val = regex_result.group(1)
    
    # extract values for yesterday        
    yday = yesterday()
    regex = yday + '\"\),([0-9\.]+)'
    soup_regex = re.compile(regex)
    regex_result = soup_regex.search(soup_string)
                
    # isolate just the feature value for the current date
    yesterday_feat_val = regex_result.group(1)
    
    # create a dictionary for each day and the values
    feat_val_dic = {
                    tday:
                        {feature:today_feat_val},
                    yday:
                        {feature:yesterday_feat_val}
                   }
    
    return feat_val_dic
    

def grab_the_data():
    """ 
        Iterate through a list of features and their urls
        and scrape the data using beautiful soup 
        return the scraped data in the form of a dataframe
    """    
    
    import pandas as pd
    
    url_list, features = feats_to_url() # turn the best features into a list of urls
    
    df_url, df_features = create_dfs(url_list, features) # convert the urls and features into dataframes
    
    current_data = {}
            
    # iterate through the dataframe urls    
    for x in range(len(df_url)):

        url = df_url.iloc[x, 0]
        feature = df_features.iloc[x, 0]
        
        # scrape the website and return a dictionary of feat:values
        date, feature, feat_val = scrape_url(url, feature)
        if x < (len(df_url) - 1):
            current_data[feature] = feat_val
        else:
            current_data[feature] = feat_val
            feature_dic = {date : current_data}
            
            
        # convert the dictionary to dataframe
        df = pd.DataFrame.from_dict(feature_dic)
        # transpose to put the features in the columns and the date as the index
        current_df = df.T
        # re-index to have the date as a column
        current_df.reset_index(inplace=True)
        current_df = current_df.rename(columns={'index' : 'Date'})
        
    print(feature_dic)
    
    return current_df
    
grab_the_data()
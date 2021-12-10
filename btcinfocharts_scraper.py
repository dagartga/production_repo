def current_date():
    
    from datetime import date
    
    # get the current date
    today = date.today()
    return today
    
print(current_date())
    
def scrape_data():
    
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
    
    url_list = [] # create empty list for urls
    
    for feat in features:
        url='https://bitinfocharts.com/comparison/'+feat
        url_list.append(url)
    
    assert 'https://bitinfocharts.com/comparison/median_transaction_fee3momUSD' == url_list[0]
    assert 'https://bitinfocharts.com/comparison/confirmationtime7std' == url_list[-1]
    

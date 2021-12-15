def get_full_dataset():
    """
        Load in the full dataset scraped from btcinfocharts
        Extract and return only a dataframe with the selected features
    """
       
    import pandas as pd

    path = './Merged_Unconverted_BTC_Data.csv'
    full_df = pd.read_csv(path)
    
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
    
    # extract only the data from the features desired
    select_df = full_df[features]
    
    return select_df

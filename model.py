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


def preprocess_the_data():
    """
        Takes in a dataframe of all the data
        to fit the scaler using MinMaxScaler and RobustScaler
        Then transform the new data using the scaler and retun it as a vector
    """
    
    from sklearn.preprocessing import MinMaxScaler, RobustScaler
    from sklearn.pipeline import Pipeline
    from btcinfocharts_scraper import grab_the_data
    

    # scale the data
    estimators = [] # create a list for the scalers
    estimators.append(['minmax', MinMaxScaler()])
    estimators.append(['robust', RobustScaler()])
    
    # add the scalers to the Pipeline
    scale = Pipeline(estimators, verbose=True)
    
    # get the full dataset
    df = get_full_dataset()
    
    # get the new dataset for the most recent data
    new_df = grab_the_data()
    
    # fit the scaler to all old data
    scaled_df = scale.fit(df)
    
    # scale the new data
    transformed_new_data = scale.transform(new_df)
    
    return transformed_new_data
    
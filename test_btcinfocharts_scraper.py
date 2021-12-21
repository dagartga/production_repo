import pytest
from datetime import date, timedelta
from btcinfocharts_scraper import feats_to_url
from btcinfocharts_scraper import create_dfs
from btcinfocharts_scraper import grab_the_data

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

tday = date.today()
yday = tday - timedelta(days=1)
tday = tday.strftime("%Y/%m/%d")
yday = yday.strftime("%Y/%m/%d")



def test_features():

    url_list, feature_list = feats_to_url()

    for feat in features:
        assert feat in feature_list


    # test the urls
    assert 'https://bitinfocharts.com/comparison/median_transaction_fee-btc-3momUSD.html' in url_list
    assert 'https://bitinfocharts.com/comparison/top100cap-btc-14mom.html' in url_list
    assert 'https://bitinfocharts.com/comparison/fee_to_reward-btc-90smaUSD.html' in url_list

    # test all the features were turned into
    assert len(url_list) == len(feature_list)


def test_create_dfs():

    import pandas as pd

    url_list = ['https://bitinfocharts.com/comparison/median_transaction_fee-btc-3momUSD.html', 'https://bitinfocharts.com/comparison/top100cap-btc-14mom.html']
    feat_list = ['median_transaction_fee3momUSD', 'top100cap14mom']

    urls, feats = feats_to_url()

    df_url, df_feats = create_dfs(urls, feats)

    assert len(df_url) == len(df_feats)

    assert df_url.iloc[0,0] == url_list[0]
    assert df_url.iloc[4,0] == url_list[1]
    assert df_feats.iloc[0,0] == feat_list[0]
    assert df_feats.iloc[4,0] == feat_list[1]



def test_scrape_url():

    from btcinfocharts_scraper import scrape_url
    from datetime import date, timedelta

    url='https://bitinfocharts.com/comparison/median_transaction_fee-btc-3momUSD.html'
    feature='median_transaction_fee3momUSD'

    json_scrape = scrape_url(url, feature)

    # check that function scraped two values
    assert len(json_scrape) == 2

    # check that the proper dates are collected
    assert tday in json_scrape
    assert yday in json_scrape

    # check that the feature is a value for each day
    assert feature in json_scrape[tday]
    assert feature in json_scrape[yday]


def test_grab_the_data():

    df = grab_the_data()

    # check that all the features are in the columns
    for i in range(len(features)):
        assert features[i] == df.columns[i]
    # check that the date is either today or yesterday
    assert df.index[0] == tday or df.index[0] == yday

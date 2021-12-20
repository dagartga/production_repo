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
    assert 'blah' in url_list # should fail

    # test all the features were turned into
    assert len(url_list) == len(feature_list)


def test_create_dfs():

    import pandas as pd

    url_list = ['https://bitinfocharts.com/comparison/median_transaction_fee-btc-3momUSD.html',, 'https://bitinfocharts.com/comparison/top100cap-btc-14mom.html']
    feat_list = ['median_transaction_fee3momUSD', 'top100cap14mom']

    df_url, df_feats = create_dfs(url_list, feat_list)

    assert df_url == pd.DataFrame(url_list)
    assert df_feats == pd.DataFrame(feat_list)


def test_scrape_url():

    from btcinfocharts_scraper import scrape_url
    from datetime import date, timedelta

    json_scrape = scrape_url()

    # check that function scraped two values
    assert len(json_scrape) == 2

    # check that the proper date is in the proper location
    assert tday == json_scrape[0]
    assert yday == json_scrape[1]

    # check that all the features were stored
    assert len(json_scrape[tday]) == len(features)
    assert len(json_scrape[yday]) == len(features)

    for feat in features:
        assert feat in json_scrape[tday]
        assert feat in json_scrape[yday]


def test_grab_the_data():

    df = grab_the_data()

    # check that all the features are in the columns
    assert features == df.columns
    # check that the date is either today or yesterday
    assert df.index[0] == yday
    assert df.index[1] == tday


print('Testing')
test_features()
print('Done')

# virtual env ~/.btc-test/Scripts/activate

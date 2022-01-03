import pytest
from model import get_full_dataset
from model import preprocess_the_data
from model import prediction


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



def test_get_full_dataset():

    df = get_full_dataset()
    feats = ['Date'] + features

    # check that the features are in the dataframe
    for i in range(len(feats)):
        assert feats[i] == df.columns[i]

    # check that the data is what is expected
    assert (4104, 10) == df.shape

    # check that no null values are present
    for i in range(len(feats)):
        assert df.iloc[:, i].isnull().sum() == 0



def test_preprocess_the_data():

    array, today_date = preprocess_the_data()

    # check that the shape of the dataframe is correct
    assert (1, 9) == array.shape

    # check that the data is scaled into the appropriate range
    assert array.max() <= 100
    assert array.min() >= -10

    # check that the date is a string format
    assert type(today_date) == str


def test_prediction():

    pred, today_date = prediction()

    # check that only one value is returned
    assert pred.shape == (1,1)

    # check that the value is a positive number
    assert pred[0][0] >= 0

    # check that the date is a string format
    assert type(today_date) == str

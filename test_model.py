import pytest
from model import get_full_dataset, preprocess_the_data



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

    # check that the features are in the dataframe
    assert features == df.columns

    # check that the data is what is expected
    assert (4104, 10) == df.shape

    # check that no null values are present
    assert df.isnull() == 0




def test_preprocess_the_data():

    df = preprocess_the_data()

    # check that 'Date' is dropped
    assert 'Date' not in df.columns

    # check that the shape of the dataframe is correct
    assert (1, 9) == df.shape

    # check that the data is scaled into the appropriate range
    assert df.max() <= 100
    assert df.min() >= -10



def test_prediction():

    pred = prediction()

    # check that only one value is returned
    assert pred.shape == (1,1)

    # check that the value is a positive number
    assert pred[0][0] >= 0

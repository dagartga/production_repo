def model():
    
    """
        Takes in the current data scraped from btcinfocharts.org
        and returns a price prediction for tomorrow
    """
    
    from keras.models import load_model
    import h5py
    
    # load the best model from the training and testing
    model = load_model('ANN4_reg_nextday300Adam0-01relu64Int4_341.hdf5')
    
    
model()
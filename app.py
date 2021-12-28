import pandas as pd
from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    from model import prediction
    next_day_pred = prediction()

    return jsonify({
                    'output':
                    {'BTC_next_day_price': str(next_day_pred[0][0])}
                       })

@app.route('/')
def home():
    return "Welcome to the BTC Next Day Price Predictor"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')

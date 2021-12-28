import pandas as pd
from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    from model import prediction
    next_day_pred = prediction()
    print(next_day_pred)
    return jsonify({'output': {'BTC_next_day_price': next_day_pred}})

@app.route('/')
def home():
    return "Welcome to the BTC Next Day Price Predictor"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')

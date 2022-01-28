[![AWS in Python 3.7.12](https://github.com/dagartga/production_repo/actions/workflows/main.yml/badge.svg)](https://github.com/dagartga/production_repo/actions/workflows/main.yml)

# production_repo
Repo for production level code for my Capstone Project for Springboard ML Engineering

## To use my project you can do this


Fork the repo


**Create a virtual environment in Windows**

$virtualenv ~/.btc-pred


**Activate it in Windows**

$source ~/.btc-pred/Scripts/activate 


### To access the API locally

With the virtual environment activated
cd into production_repo/


**Install the requirements**

$pip install -r requirements.txt


**Run the app using Flask**

$python app.py


**Web browser GET**

First, open a web browser and type

localhost:3000/

This should return "Welcome to the BTC Next Day Price Predictor"

If not then there is an error try starting the process over


Second, in the web browser type

localhost:3000/predict

This will take a while but should return a JSON object wtih the next day predicted price


### To access the API using Docker and Postman


With the virtual environment activated

cd into production_repo/


**Build the Docker image**

$docker build -t btc-prediction:1.0 .


**Run the container**

$docker run -p 5000:3000 btc-prediction:1.0


**Open the Postman app**

Click the + symbol to create a new workspace

Use the drop down to select GET

In the window next to GET type in http://localhost:5000/predict

Click the Send button

After a little while it should return a JSON object with 
```
{
  'output':
    {
    'BTC_next_day_price':'48000'
    }
 }
```

Where '48000' is whatever the prediction price is



### To test the code locally

Run pytest to test the code using command line from the directory production_repo/ on your own machine

$pytest test_btcinfocharts_scraper.py

$pytest test_model.py

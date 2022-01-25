[![AWS in Python 3.7.12](https://github.com/dagartga/production_repo/actions/workflows/main.yml/badge.svg)](https://github.com/dagartga/production_repo/actions/workflows/main.yml)

# production_repo
Repo for production level code for my Capstone Project for Springboard ML Engineering

## To GET request the Bitcoin Next Day Price Prediction model from a web browser

The model is being hosted on an EC2 instance through AWS

1. Test the app is running by typing into the web browser

`ec2-54-176-190-128.us-west-1.compute.amazonaws.com:3000`

2. GET request for next day price prediction by typing into the web browser

`ec2-54-176-190-128.us-west-1.compute.amazonaws.com:3000/predict`


## To use my project on your machine and run locally


1. Fork the repo


2. Create a virtual environment in Windows

`virtualenv ~/.btc-pred`


3. Activate it in Windows

`source ~/.btc-pred/Scripts/activate` 

4. cd into production_repo/


5. Install the requirements

`make install`


6. Run the app using Flask

`python app.py`

7. Open a web browser and type

`localhost:3000/`

This should return "Welcome to the BTC Next Day Price Predictor"

If not, then there is an error. Try starting the process over

8. GET request the prediction model

`localhost:3000/predict`

This will take a while but should return a JSON object wtih the next day predicted price


### Run the model using Docker and Postman


1. Activate the virtual environment as listed above

2. cd into production_repo/

3. Build the Docker image

`docker build -t btc-prediction:1.0 .` Do not forget the `.` at the end of the line of code


4. Run the container

`docker run -p 3000:3000 btc-prediction:1.0`

5. Open the Postman app

6. Click the + symbol to create a new workspace

7. Use the drop down to select GET

8. In the window next to GET type in http://localhost:3000/predict

9. Click the Send button

After a little while it should return a JSON object with 

```
{
  "output":
    {
    "BTC_next_day_price":"39672.203",
    "Today's Date":"2022/01/20"
    }
 }
 ```

Where `39672.203` is whatever the prediction price is for tomorrow with regard to `Today's Date`

Today's Date is in the format of `YYYY/mm/dd`


### To test the code locally

Run pytest to test the code using command line from the directory production_repo/ on your own machine

1. cd into the production_repo directory

2. Run pytest on the web scraper

`pytest test_btcinfocharts_scraper.py`

3. Run pytest on the ML model

`pytest test_model.py`

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt


test:
	python -m pytest -vv --cov=model test_model.py
	python -m pytest -vv --cov=model test_btcinfocharts_scraper.py

deploy:
	echo "Deploying app"
	eb deploy btc-pred-env

import csv
import json
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import requests
from pandas import read_csv

#api_key = os.environ.get("api_key")
api_key = "c4c3cb40b87c5d67f381e5bbdc3763ca"
print(api_key)
request_url = f"https://api.themoviedb.org/3/movie/76341?api_key={api_key}"
response = requests.get(request_url)
print(type(response)) # class 'requests.models.response'
print(response.status_code)
print(response.text)
#    if "Error Message" in response.text:
#        print(f"Error, could not locate url.  Please try again.")
#        continue
#    if "higher API call frequency" in response.text:
#        print("You entered too many stocks.  Please try again.")
#        quit()
#    parsed_response = json.loads(response.text)
#    last_refreshed = parsed_response['Meta Data']['3. Last Refreshed']
#    tsd = parsed_response['Time Series (Daily)']
#    dates = list(tsd.keys()) #TODO sort
#    latest_day = dates[0]
#    latest_close = tsd[latest_day]['4. close']
#
#    high_prices = []
#    low_prices = []
#
#    for date in dates:
#        high_price = tsd[date]["2. high"]
#        high_prices.append(float(high_price))
#        low_price = tsd[date]["3. low"]
#        low_prices.append(float(low_price))
#
#    recent_high = max(high_prices) 
#    recent_low = min(low_prices)
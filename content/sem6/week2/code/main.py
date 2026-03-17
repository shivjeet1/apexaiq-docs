""" Assignment of week2-session2: APIs """

from flask import Flask

app = Flask(__name__)

import api.weather
#import api.github_analytics
#import api.movies_search
#import api.top_headlines
#import api.currency_conv
#import api.holiday_cal
#import api.crypto_price
#import api.quote_daily
#import api.ip_lookup

if __name__ == "__main__":
    app.run()

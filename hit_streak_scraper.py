import requests
import datetime 
from datetime import date
import pandas as pd


def scrape_baseball_musings():
    # get current hit streak data from baseballmusings.com
    today = date.today()
    today = str(today)[-2:]
    url = f'https://www.baseballmusings.com/cgi-bin/CurStreak.py?EndDate=07%2F{today}%2F2022'
    resp = requests.get(url)
    with open('test_mlb_longesthitstreak', 'wb') as f:
        f.write(resp.content)
    df_streaks = pd.read_html('test_mlb_longesthitstreak')
    df_streaks = pd.DataFrame(df_streaks[1])
    return df_streaks

    
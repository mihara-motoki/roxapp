import pandas as pd
import time
import lxml
import requests
import numpy as np
import datetime


url = 'https://reserve.489ban.net/client/hana-mura/0/plan/availability/room/stay?date=2021-04-06'
pd.read_html(url)

html = requests.get(url)
html.encoding = 'EUC-JP'
import requests
from bs4 import BeautifulSoup
import pandas.tseries.offsets as offsets
html.encoding = 'EUC-JP'
soup = BeautifulSoup(html.content, 'html.parser')

#divの指定
divs = soup.select('tbody div')

#関数定義のコード
def div_to_availability(div):
    if div.find(class_='fa-circle-o'):
        return 'o'
    elif div.find(class_='fa-exclamation-triangle'):
        return 't'
    elif div.find(class_='fa-close'):
        return 'c'
    elif div.find(class_='fa-phone-square'):
        return 's'
    elif div.find(class_='fa-minus'):
        return 'm'
    else:
        return str(div.a.string).strip()

#成形する
availabilities = [div_to_availability(div) for div in divs]
pd.DataFrame(np.split(np.array(availabilities), 7))
    

#サーバーに負荷を掛けないように調整

stay_date_list = list(pd.date_range(start=datetime.datetime.now(), periods=3,  freq='14D').strftime('%Y-%m-%d'))
def scrape_hotel_vacancy(stay_date_list):    
    hotel_vacancy = {}
    for stay_date in tqdm(stay_date_list):
        try:
            url = 'https://reserve.489ban.net/client/hana-mura/0/plan/availability/room/stay?date=' + stay_date
            html = requests.get(url)
            html.encoding = 'EUC-JP'
            soup = BeautifulSoup(html.content, 'html.parser')
            divs = soup.select('tbody div')
            availabilities = [div_to_availability(div) for div in divs]
            hotel_vacancy[int(stay_date.replace('-',''))] = pd.DataFrame(np.split(np.array(availabilities), 7))
            time.sleep(1) #スリープ時間
        except IndexError:
            continue
        except:
            break      
    return hotel_vacancy
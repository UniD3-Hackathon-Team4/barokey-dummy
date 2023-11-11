from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import lxml
import xml

OPENAPI_KEY = "6a55716a42706f6f3131367149614876"
KEY = "AREA_CONGEST_LVL"
base_url = "http://openapi.seoul.go.kr:8088/{OPENAPI_KEY}/xml/citydata/4/4/{place}"
places = pd.read_csv("./../data/crowds/places.csv")

def get_crowd_info():
    info = []
    for idx, entry in places.iterrows():
        place_name = entry.AREA_NM
        lat = entry.Latitude
        long = entry.Longitude
        url = base_url.format(OPENAPI_KEY = OPENAPI_KEY, place = place_name)

        response = requests.get(url).text
        print("get")

        parsed = bs(response, 'lxml-xml')
        text = parsed.find(KEY).text

        # text = lxml.etree.fromstring(response).findtext(KEY)
        print(text)
        if text == "붐빔":
            congestion = 100
        elif text == "약간 붐빔":
            congestion = 75
        elif text == "보통":
            congestion = 50
        else:
            congestion = 25
        
        info.append({
            "title" : place_name,
            "geodata" : [lat, long],
            "congestion" : congestion
        })
    
    return info
import requests
import lxml

def get_crowd_info():
    '''url = "http://openapi.seoul.go.kr:8088/sample/xml/citydata/4/4/%EA%B4%91%ED%99%94%EB%AC%B8%C2%B7%EB%8D%95%EC%88%98%EA%B6%81"

    http://openapi.seoul.go.kr:8088/6a55716a42706f6f3131367149614876/xml/citydata/4/4/%EA%B4%91%ED%99%94%EB%AC%B8%C2%B7%EB%8D%95%EC%88%98%EA%B6%81
    
    
    "AREA_CONGEST_LVL"'''
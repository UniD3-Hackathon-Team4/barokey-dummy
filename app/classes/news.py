from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import random
import requests

headers = {
    "X-Naver-Client-Id": "SF21kWPUHuGmay0KHcJw",
    "X-Naver-Client-Secret": "y_7HlIIrpc"
}

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(options = options)

def get_headlines():
    base_url = """https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={section}#&date=%2000:00:00&page=1"""

    section_label_table = [
        (100,"정치"),
        (101,"경제"),
        (102,"사회"),
        (103,"생활/문화"),
        (104,"세계"),
        (105,"IT/과학")
    ]

    headlines = []

    for section_id, headline in section_label_table:
        title_ = headline
        articles_ = []

        url = base_url.format(section = section_id)
        
        driver.get(url)
        
        time.sleep(0.5)

        articles = driver.find_elements(By.CSS_SELECTOR, '#main_content > div > div._persist > div.section_headline > ul > li')

        for article in articles[:5]:
            tag = article.find_elements(By.CSS_SELECTOR, 'div.sh_text')[0]

            a_tag = tag.find_elements(By.CSS_SELECTOR, 'a')[0]
            title = a_tag.text
            link = a_tag.get_attribute("href")
            
            summary = tag.find_elements(By.CSS_SELECTOR, 'div.sh_text_lede')[0].text

            data = {
                "title" : title,
                "type" : random.randint(-1, 4),
                "summary" : summary,
                "link" : link
            }

            articles_.append(data)
        
        headlines.append({
            "title" : title_,
            "articles" : articles_
        })

    return headlines


def get_headlines_v2():
    base_url = "https://openapi.naver.com/v1/search/news.json?query={keyword}&display=5&start=1&sort=sim"

    word_list = [
        "폭우",
        "화재",
        "빈대",
        "칼부림",
        "건물 붕괴",
        "스토킹 범죄",
        "교통사고",
        "폭염",
        "약물 오남용",
        "사람이 붐비다",
        "전염병 전파",
        "실종",
        "성범죄",
        "한파",
        "극단적 선택"
    ]

    headlines = []
    
    for keyword in word_list:
        headlines.append({
            "title" : keyword,
            "ariticles" : get_headlines_v2_keyword(keyword)
        })
    
    return headlines

def get_headlines_v2_keyword(keyword):
    base_url = "https://openapi.naver.com/v1/search/news.json?query={keyword}&display=5&start=1&sort=sim"

    url = base_url.format(keyword = keyword)

    response = requests.get(url, headers = headers).json()

    headlines = []
    for item in response['items']:
        headlines.append({
            "title" : bs(item["title"], 'lxml').text,
            "type" : random.randint(-1, 4),
            "summary" : bs(item["description"], 'lxml').text,
            "link" : item["originallink"]
        })

    return headlines
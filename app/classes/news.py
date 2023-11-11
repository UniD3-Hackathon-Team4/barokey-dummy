from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

base_url = """https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={section}#&date=%2000:00:00&page=1"""

section_label_table = [
    (100,"정치"),
    (101,"경제"),
    (102,"사회"),
    (103,"생활/문화"),
    (104,"세계"),
    (105,"IT/과학")
]

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(options = options)

def get_headlines():
    headlines = []

    for section_id, headline in section_label_table:
        title_ = headline
        articles_ = []

        url = base_url.format(section = section_id)
        
        driver.get(url)
        
        time.sleep(1)

        articles = driver.find_elements(By.CSS_SELECTOR, '#main_content > div > div._persist > div.section_headline > ul > li')

        for article in articles:
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
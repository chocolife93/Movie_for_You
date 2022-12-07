# crawling 작업

# crawling은 각자 진행해보고 빨리 완성되는 코드로 연도를 나눠서 작업하겠습니다.
# 일단 2022년 개봉작만 크롤링해주세요.
# 나머지는 연도별로 나눠서 작업하겠습니다.
# 컬럼명은 ['titles', 'reviews']로 통일해주세요.
# 파일명은 'reviews_{}.csv'.format(연도)로 해주세요.
# crawling 코드 완성되는대로 PR해주세요.


from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

# 네이버영화에서 리뷰를 보면 비슷한 리뷰를 가진 영화를 추천하는 모델
options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)


your_year = 2022
for i in range(1, 32): # page
    url = 'https://movie.naver.com/movie/sdb/browsing/bmovie_open.naver?open={}&page={}'.format(your_year, i)
    titles = []
    reviews = []
    try:
        for j in range(1, 21): # 영화 게시글
            driver.get(url)
            time.sleep(0.1)
            movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(j)
            title = driver.find_element('xpath', movie_title_xpath).text
            driver.find_element('xpath', movie_title_xpath).click()
            time.sleep(0.1)
            try:
                review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'
                driver.find_element('xpath',review_button_xpath).click()
                time.sleep(0.1)
                for k in range(1, 11): # 리뷰 게시글
                    review_title_xpath = '//*[@id="reviewTab"]/div/div/ul/li[{}]/a/strong'.format(k)
                    driver.find_element('xpath', review_title_xpath).click()
                    time.sleep(0.1)
                    review_xpath = '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]/div'
                    review = driver.find_element('xpath', review_xpath).text
                    print(review)
            except:
                print('error', i, j, k)
    except:
        print('error', i, j, k)
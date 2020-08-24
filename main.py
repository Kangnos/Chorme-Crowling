from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('.\chrome crowling test\chromedriver.exe')

delay=3
browser.implicitly_wait(delay)

start_url  = 'https://www.youtube.com'
browser.get(start_url)  
browser.maximize_window()

browser.find_elements_by_xpath('//*[@id="search-input"]')[0].click()
browser.find_elements_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input')[0].send_keys('강노스')#검색창 영역에 원하는 youtuber입력
browser.find_elements_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input')[0].send_keys(Keys.RETURN)#엔터

browser.find_elements_by_xpath('//*[@class="style-scope ytd-channel-renderer"]').click()

browser.find_element_by_xpath('//*[@class="scrollable style-scope paper-tabs"]/paper-tab[2]').click()

body = browser.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출

num_of_pagedowns = 20
#10번 밑으로 내리는 것
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1
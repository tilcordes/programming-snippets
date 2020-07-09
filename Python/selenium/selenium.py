from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
import random

def google_query():
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless') // would hide the browser window
    driver = webdriver.Chrome('chromedriver.exe', options=None)
    driver.get('https://google.de')
    search_field = driver.find_element_by_name('q')
    search_field.send_keys('python')
    time.sleep(1)
    search_field.submit()
    time.sleep(3)
    print('query done')
    driver.quit()

def proxy_request():
    proxy = proxy_scraper()
    print(proxy)
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server={}'.format(proxy))
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get('https://httpbin.org/ip')
    time.sleep(5)
    driver.quit()    
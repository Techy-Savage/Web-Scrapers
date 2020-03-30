import requests
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_youtube(query):
    
    driver=webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query='+'{}'.format(query.replace(' ', '+'))+'&sp=CAI%253D')

    # Render Page For Links

    for i in range(1,10):
        sleep(0.5)
        driver.execute_script("window.scrollTo(0, {})".format(str(5000*i))) 

    # Get Links

    links = [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]

    driver.close()

    def get_email():
        for i in list(set(links)):
            r = requests.get(i)
            email = ''.join(set(re.findall(r"[\w\.]+@[\w\.]+", r.text.lower())))
            if email != '': yield email


    for num, val in enumerate(get_email()):
        print(num, val)


search_youtube('type beat')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Data

count = 0
emc = 0
links_c = 0

def remove_dups():
    with open('emails.txt', 'r+') as file:
        seen = set([line for line in file if line != "\n"]) 
        file.seek(0)
        file.writelines(seen)
        file.truncate() 

def get_emails(search):

    global count,emc,links_c

    # Driver Setup

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    #options.add_argument("--headless")
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
                if "k" in views.lower():
                    views = float(views[:-1]) * 1000
                elif "m" in views.lower():
                    views = float(views[:-1]) * 1000000
                else:
                    views = float(views)
                break
            except:
                time.sleep(1)


        if views == 'no': views = 0

        if int(views) <= 7000:
            
            # Check description for email

            try:
                description_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]/yt-formatted-string')))
                time.sleep(1)
                email = ''.join(re.findall(r"[\w\.]+@[\w\.]+", description_box.text))
                count+=1

                # Save email to file

                with open('emails.txt', 'a') as f:
                    if email != '':
                        f.write(u"{}\n".format(email))
                        emc += 1

            except:
                continue
            


            

def search(the_searches):
    for searches in the_searches:
            get_emails(searches)
    print("Total amount of links:", links_c, '|', 'Amount under 7k views:', count, '|', 'Amount of emails:', emc)
    remove_dups()


#search(['juice wrld type beat','type beat', 'lil tjay type beat', 'lil xan type beat', 'pop smoke type beat', 'drake type beat', 'post malone type beat', 'lil uzi type beat',]) # Search using quotations seperated by a comma eg: search(['type beat', 'lil wayne'])

remove_dups()

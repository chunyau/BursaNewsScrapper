from selenium import webdriver
import bs4 as bs
import pandas as pd
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome)
driver.implicitly_wait(60)


company_link = pd.DataFrame(columns = ['Company Link'])
links = pd.DataFrame(columns = ['Announcement Link'])

#From First Page to Last Page
for i in range(0,48041):
    try:
        driver.get("http://www.bursamalaysia.com/market/listed-companies/company-announcements/#/?category=all&page={}".format(i))
        All_Links = driver.find_elements_by_css_selector('.bm_left a')
        
        for link in All_Links:
            x = link.get_attribute('href')
            if  "company-announcements" in x:
                links =links.append({"Announcement Link":x},ignore_index=True)
            elif "stock_code" in x:
                company_link = company_link.append({"Company Link": x},ignore_index=True)
        print("Page{} Done".format(i))
    except:
        driver.get("http://www.bursamalaysia.com/market/listed-companies/company-announcements/#/?category=all&page={}".format(i))
        All_Links = driver.find_elements_by_css_selector('.bm_left a')
        for link in All_Links:
            x = link.get_attribute('href')
            if  "company-announcements" in x:
                links =links.append({"Announcement Link":x},ignore_index=True)
            elif "stock_code" in x:
                company_link = company_link.append({"Company Link": x},ignore_index=True)
        print("Page{} Done".format(i))
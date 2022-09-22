#     used to diable the SSL error while connected to vpn
# import os
# os.environ['WDM_SSL_VERIFY'] = '0'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def launchremoteWebDriverBrowser():
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.google.com/')
    driver.maximize_window()
    driver.close()
    driver.quit()

launchremoteWebDriverBrowser()
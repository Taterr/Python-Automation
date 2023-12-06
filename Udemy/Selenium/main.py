# this project is meant to scrape websites

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# access to webdriver through selenium

service = Service('F:\\Python-Automation\\Selenium\\chromedriver-win64')

def get_driver():
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")        # disabling infobars, so as not to confuse the automation
    options.add_argument("start-maximized")         # maximizing the window
    options.add_argument("disable-dev-shm-usuage")  # disabling developer mode
    options.add_argument("no-sandbox")              # disabling sandbox mode  
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())

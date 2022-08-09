from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# https://selenium-python.readthedocs.io/locating-elements.html
from selenium.webdriver.common.by import By 

def launchBrowser():
    browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))  # Chrome is a class
    browser.get("https://github.com/login") 
    return browser

# need to save in variable otherwise page appears and quickly disappears... because it gets garbage collected maybe??
browser = launchBrowser()

username_box = browser.find_element(By.ID,"login_field")
username_box.send_keys("type username here") # simulates user typing in input box

password_box = browser.find_element(By.ID,"password")
password_box.send_keys("type password here") 
password_box.submit()

# checks if string is in page source and throws exception if not
assert "type username here" in browser.page_source
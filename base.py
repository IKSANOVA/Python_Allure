"""Базовые настройки и функции, которые понадобятся в тестах."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import random

DRIVER_PATH = os.path.join(os.getcwd(),"chromedriver.exe")
BASE_URL = "http://testingcourse.ru/form/"

def get_driver(maximized=True, incognito=False, headless=False):
    options = webdriver.ChromeOptions()
    if maximized:
        options.add_argument("--start-maximized")
    if incognito:
        options.add_argument("--incognito")
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    #driver.maximize_window()
    driver.get(BASE_URL)
    return driver

def get_random_phone(prefix='381'):
    return prefix + ''.join([str(random.randint(0,9)) for i in range(7)])

login = ""
password = ""
fullName = ""
email = ""
phone = ""

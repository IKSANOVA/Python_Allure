from selenium import webdriver
import os
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from base import get_driver, login, password, DRIVER_PATH
from selenium.webdriver.chrome.options import Options
from base import get_driver, login, password, BASE_URL

class Base:
    def __init__(self, maximized=True, incognito=False, headless=False):
        options = webdriver.ChromeOptions()
        if maximized:
            options.add_argument("--start-maximized")
        if incognito:
            options.add_argument("--incognito")
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(DRIVER_PATH, options=options)

    

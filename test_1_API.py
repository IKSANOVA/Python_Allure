import allure
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from base import get_driver
import requests

@allure.suite("Тестирование API")
@allure.title('Авторизация без указания логина и пароля')
def test_api1():
    url = 'https://restful-booker.herokuapp.com/auth'
    response = requests.post(url)
    assert response.status_code == 200

@allure.suite("Тестирование API")
@allure.title('Авторизация с логином и паролем')
def test_api2():
    url = 'https://restful-booker.herokuapp.com/auth'
    body = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url, data=body)
    assert response.status_code == 200

    
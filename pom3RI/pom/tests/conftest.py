import time

import pytest
from selenium import webdrivers

from pom.pages.ProductPage import ProductPage
from pom.pages.homepage import HomePage
from pom.pages.login_page import LoginPage



@pytest.fixture
def setup_and_teardown(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.implicitly_wait(10)

    request.cls.loginpage=LoginPage(driver)
    request.cls.homepage=HomePage(driver)
    request.cls.productpage=ProductPage(driver)

    request.cls.driver = driver

    yield
    time.sleep(5)
    driver.quit()

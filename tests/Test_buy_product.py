from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_Page
from pages.login_page import LoginPage
from pages.main_page import Main_Page


# from selenium.webdriver.chrome.options import Options

def test_buy_product():
    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    print("Start Test")

    login = LoginPage(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product()

    cp = Cart_Page(driver)
    cp.click_checkout_button()


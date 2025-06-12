from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    print("Start Test")

    login = LoginPage(driver)
    login.authorization()

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    enter_shopping_cart.click()
    print("Click Enter Shopping Cart")


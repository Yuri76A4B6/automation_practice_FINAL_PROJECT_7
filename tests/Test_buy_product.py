from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_Page
from pages.client_info_page import Client_info_Page
from pages.finish_page import Finish_Page
from pages.login_page import LoginPage
from pages.main_page import Main_Page
from pages.payment_page import Payment_Page
import pytest

# from selenium.webdriver.chrome.options import Options
#@pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1():
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product1()

    cp = Cart_Page(driver)
    cp.click_checkout_button()

    cip = Client_info_Page(driver)
    cip.input_information()

    p = Payment_Page(driver)
    p.click_finish_button()

    f = Finish_Page(driver)
    f.finish()
    print("Завершена работа метода test_buy_product_1")
    driver.quit()

#@pytest.mark.run(order=1)
# def test_buy_product_2(set_up):
#     # options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     options.add_argument("--guest")
#     driver = webdriver.Chrome(options=options)
#
#     print("Start Test 2")
#
#     login = LoginPage(driver)
#     login.authorization()
#
#     mp = Main_Page(driver)
#     mp.select_product2()
#
#     cp = Cart_Page(driver)
#     cp.click_checkout_button()
#
#     # cip = Client_info_Page(driver)
#     # cip.input_information()
#     #
#     # p = Payment_Page(driver)
#     # p.click_finish_button()
#     #
#     # f = Finish_Page(driver)
#     # f.finish()
#     print("Завершена работа метода test_buy_product_2")
#     driver.quit()

#@pytest.mark.run(order=2)
# def test_buy_product_3(set_up):
#     # options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     options.add_argument("--guest")
#     driver = webdriver.Chrome(options=options)
#
#     print("Start Test 3")
#
#     login = LoginPage(driver)
#     login.authorization()
#
#     mp = Main_Page(driver)
#     mp.select_product3()
#
#     cp = Cart_Page(driver)
#     cp.click_checkout_button()

    # cip = Client_info_Page(driver)
    # cip.input_information()
    #
    # p = Payment_Page(driver)
    # p.click_finish_button()
    #
    # f = Finish_Page(driver)
    # f.finish()
    #print("Завершена работа метода test_buy_product_3")
    driver.quit()
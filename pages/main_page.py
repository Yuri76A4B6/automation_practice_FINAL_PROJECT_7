import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Main_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    about = "//a[@id='about_sidebar_link']"
    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.about)))
    # ACTIONS

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Выбран товар номер 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Выбран товар номер 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Выбран товар номер 3")

    def click_cart(self):
        self.get_cart().click()
        print("Нажата кнопка для перехода в корзину")

    def click_menu(self):
        self.get_menu().click()
        print("Нажата кнопка для перехода в MENU")

    def click_about(self):
        self.get_about().click()
        print("Нажата кнопка для перехода в ABOUT")

    # METHODS

    def select_product1(self):
        with allure.step("Select product 1"):
            Logger.add_start_step(method="select_product1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product1")

    def select_product2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        with allure.step("Select menu about"):
            self.get_current_url()
            self.click_menu()
            self.click_about()
            self.assert_url('https://saucelabs.com/')
